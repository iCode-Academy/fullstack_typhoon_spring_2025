import http.server
import socketserver
import json
import psycopg2
import re

# --- Configuration ---
# Database Connection Details
DB_NAME = "session_57"
DB_USER = "postgres"
DB_PASS = ""
DB_HOST = "localhost"
DB_PORT = "5432"
PORT = 8000 # The port your API server will run on

# --- Database Functions ---

def db_connect():
    """Establishes a connection to the database."""
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )

def setup_database():
    """Creates the 'posts' table if it doesn't already exist."""
    print("Checking database setup...")
    # Use IF NOT EXISTS to prevent an error if the table is already there.
    sql = """
    CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        title VARCHAR(255) NOT NULL,
        body TEXT
    );
    """
    conn = None
    try:
        conn = db_connect()
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
            print("✅ Database table 'posts' is ready.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error setting up database: {error}")
        # If the database can't be set up, the server can't run.
        exit(1)
    finally:
        if conn is not None:
            conn.close()

def execute_query(query, params=None, fetch=None):
    """A generic function to execute database queries."""
    conn = None
    try:
        conn = db_connect()
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            if fetch == 'one':
                # Fetch one record with column names
                res = cur.fetchone()
                if res:
                    colnames = [desc[0] for desc in cur.description]
                    return dict(zip(colnames, res))
                return None
            if fetch == 'all':
                # Fetch all records with column names
                res = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                return [dict(zip(colnames, row)) for row in res]
            # For INSERT, UPDATE, DELETE, return row count
            return {"rows_affected": cur.rowcount}
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database Error: {error}")
        return {"error": str(error)}
    finally:
        if conn is not None:
            conn.close()

# --- API Request Handler ---

class MyAPIRequestHandler(http.server.BaseHTTPRequestHandler):
    """Processes incoming HTTP requests for the Posts API."""

    def _send_response(self, status_code, data):
        """Helper to send a JSON response."""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self._send_response(204, {})

    def do_GET(self):
        """Handle GET requests to /posts or /posts/<id>."""
        # Regex to match /posts/ and optionally an ID
        match = re.fullmatch(r'/posts/?(\d*)', self.path)
        if match:
            post_id = match.group(1)
            if post_id: # /posts/<id>
                sql = "SELECT * FROM posts WHERE id = %s;"
                data = execute_query(sql, (post_id,), fetch='one')
                if data and 'error' not in data:
                    self._send_response(200, data)
                else:
                    self._send_response(404, {"error": "Post not found"})
            else: # /posts
                sql = "SELECT * FROM posts ORDER BY id;"
                data = execute_query(sql, fetch='all')
                self._send_response(200, data)
        else:
            self._send_response(404, {"error": "Endpoint not found"})

    def do_POST(self):
        """Handle POST requests to /posts to create a new post."""
        if self.path == '/posts':
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))

            # Basic validation
            if not all(k in post_data for k in ['user_id', 'title', 'body']):
                self._send_response(400, {"error": "Missing required fields: user_id, title, body"})
                return

            sql = "INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s) RETURNING *;"
            params = (post_data['user_id'], post_data['title'], post_data['body'])
            new_post = execute_query(sql, params, fetch='one')

            if 'error' in new_post:
                self._send_response(500, new_post)
            else:
                self._send_response(201, new_post) # 201 Created
        else:
            self._send_response(404, {"error": "Endpoint not found"})

    def do_PUT(self):
        """Handle PUT requests to /posts/<id> to update a post."""
        match = re.fullmatch(r'/posts/(\d+)', self.path)
        if match:
            post_id = match.group(1)
            content_length = int(self.headers['Content-Length'])
            update_data = json.loads(self.rfile.read(content_length))
            
            sql = "UPDATE posts SET user_id = %s, title = %s, body = %s WHERE id = %s RETURNING *;"
            params = (update_data['user_id'], update_data['title'], update_data['body'], post_id)
            updated_post = execute_query(sql, params, fetch='one')

            if updated_post and 'error' not in updated_post:
                self._send_response(200, updated_post)
            else:
                self._send_response(404, {"error": "Post not found or update failed"})
        else:
            self._send_response(404, {"error": "Endpoint not found"})

    def do_DELETE(self):
        """Handle DELETE requests to /posts/<id>."""
        match = re.fullmatch(r'/posts/(\d+)', self.path)
        if match:
            post_id = match.group(1)
            sql = "DELETE FROM posts WHERE id = %s;"
            result = execute_query(sql, (post_id,))
            
            if result.get("rows_affected", 0) > 0:
                self._send_response(204, {}) # 204 No Content
            else:
                self._send_response(404, {"error": "Post not found"})
        else:
            self._send_response(404, {"error": "Endpoint not found"})


# --- Main Execution Block ---
if __name__ == "__main__":
    # Ensure the database table exists before starting the server.
    setup_database()

    with socketserver.TCPServer(("", PORT), MyAPIRequestHandler) as httpd:
        print(f"✅ Full CRUD API server running on http://localhost:{PORT}")
        print("Available endpoints:")
        print("  - GET    /posts")
        print("  - GET    /posts/<id>")
        print("  - POST   /posts")
        print("  - PUT    /posts/<id>")
        print("  - DELETE /posts/<id>")
        print("\nPress Ctrl+C to stop the server.")
        httpd.serve_forever()
