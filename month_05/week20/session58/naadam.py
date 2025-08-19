"""
1. Configure your python environment
> python3 -m venv .venv

2. Activate your python environment
> source .venv/bin/activate

3. Install postgresql package to connect from python to PostgreSQL
> pip install psycopg2-binary
"""

import psycopg2
from psycopg2 import sql

DB_NAME = "naadam"
DB_USER = "postgres"      # энд өөрийн PostgreSQL хэрэглэгчийн нэрийг оруулна
DB_PASSWORD = ""  # энд өөрийн PostgreSQL нууц үгийг оруулна
DB_HOST = "localhost"
DB_PORT = "5432"


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


def create_database():
    """Мэдээллийн сангийн хүснэгтүүдийг үүсгэнэ."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF EXISTS participants (
            id SERIAL primary key,
            name VARCHAR(255) NOT NULL,
            age INTEGER,
            sport VARCHAR(50) NOT NULL CHECK (sport IN ('Бөх', 'Сур харваа', 'Морин уралдаан'))         
        );
    ''')

    cursor.execute('''
         CREATE TABLE IF NOT EXISTS events (
            id SERIAL PRIMARY KEY,
            sport VARCHAR(255) NOT NULL,
            location VARCHAR(255),
            winner_id INTEGER,
            FOREIGN KEY (winner_id) REFERENCES participants (id)
        );
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    print("PostgreSQL мэдээллийн сангийн хүснэгтүүд бэлэн боллоо.")


def add_participant():
    name = input("Оролцогчийн нэрийг оруулна уу: ")
    age = int(input("Оролцогчийн насыг оруулна уу: "))
    print("Спортын төрлөө сонгоно уу: 1. Бөх, 2. Сур харваа, 3. Морин уралдаан")
    sport_choice = input("Сонголт (1/2/3): ")

    sport_map = {'1': 'Бөх', '2': 'Сур харваа', '3': 'Морин уралдаан'}
    sport = sport_map.get(sport_choice)

    if not sport:
        print("Спортын төрөл буруу байна.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO participants (name, age, sport) VALUES (%s, %s, %s)",
        (name, age, sport)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"{name}-г {sport} төрөлд амжилттай нэмлээ.")


def add_event():
    print("Тэмцээний спортын төрлийг сонгоно уу: 1. Бөх, 2. Сур харваа, 3. Морин уралдаан")
    sport_choice = input("Сонголт (1/2/3): ")
    sport_map = {'1': 'Бөх', '2': 'Сур харваа', '3': 'Морин уралдаан'}
    sport = sport_map.get(sport_choice)

    if not sport:
        print("Спортын төрөл буруу байна.")
        return

    location = input(f"{sport} тэмцээн болох газрыг оруулна уу: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO events (sport, location) VALUES (%s, %s)
        """, (sport, location))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"'{location}'-д {sport} тэмцээнийг амжилттай үүсгэлээ.")


def record_winner():
    view_events()
    event_id = input("Шинэчлэх тэмцээний ID-г оруулна уу: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT sport FROM events WHERE id = %s", (event_id,))
    result = cursor.fetchone()
    if not result:
        print("Тэмцээн олдсонгүй.")
        cursor.close()
        conn.close()
        return

    event_sport = result[0]
    print(f"\n--- {event_sport} төрлийн оролцогчид ---")
    cursor.execute("SELECT id, name, age FROM participants WHERE sport = %s", (event_sport,))
     
    participants = cursor.fetchall()

    if not participants:
        print(f"{event_sport} төрөлд бүртгэлтэй оролцогч олдсонгүй.")
        cursor.close()
        conn.close()
        return

    for p in participants:
        print(f"ID: {p[0]}, Нэр: {p[1]}, Нас: {p[2]}")

    winner_id = input("\nЯлагч оролцогчийн ID-г оруулна уу: ")

    cursor.execute("UPDATE events SET winner_id = %s WHERE id = %s", (winner_id, event_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Ялагчийг амжилттай бүртгэлээ! 🏆")


def view_participants():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM participants ORDER BY sport, name")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    print("\n--- Нийт оролцогчид ---")
    for row in rows:
        print(f"ID: {row[0]}, Нэр: {row[1]}, Нас: {row[2]}, Спорт: {row[3]}")
    print("-" * 26)


def view_events():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT e.id, e.sport, e.location, p.name 
    FROM events e
    LEFT JOIN participants p ON e.winner_id = p.id
    """
    cursor.execute(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    print("\n--- Наадмын тэмцээнүүд ---")
    for row in rows:
        winner = row[3] if row[3] else "Шийдэгдээгүй"
        print(f"Тэмцээний ID: {row[0]}, Спорт: {row[1]}, Байршил: {row[2]}, Ялагч: {winner}")
    print("-" * 21)


def main_menu():
    create_database()

    while True:
        print("\n===== Наадмын Удирдлагын Систем =====")
        print("1. Оролцогч нэмэх")
        print("2. Оролцогчдыг харах")
        print("3. Тэмцээн нэмэх")
        print("4. Тэмцээнүүдийг харах")
        print("5. Тэмцээний ялагчийг бүртгэх")
        print("6. Гарах")
        choice = input("Сонголтоо оруулна уу: ")

        if choice == '1':
            add_participant()
        elif choice == '2':
            view_participants()
        elif choice == '3':
            add_event()
        elif choice == '4':
            view_events()
        elif choice == '5':
            record_winner()
        elif choice == '6':
            print("Програмаас гарч байна. Баяртай!")
            break
        else:
            print("Буруу сонголт, дахин оролдоно уу.")


if __name__ == '__main__':
    main_menu()