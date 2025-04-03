import sys
import io

print("Алдааны мессеж", file=sys.stderr)

# Стандарт гаралт (stdout)
sys.stdout.write("Энэ бол стандарт гаралт\n")

# Стандарт алдаа (stderr)
sys.stderr.write("Энэ бол алдааны мессеж\n")

# Стандарт оролт (stdin)
print("Ямар нэгэн зүйл бичээд Enter дарна уу:")
user_input = sys.stdin.readline().strip()
print(f"Та бичсэн: {user_input}")

# stdout-г түр чиглүүлэх
original_stdout = sys.stdout
string_io = io.StringIO()
sys.stdout = string_io

print("Энэ баригдсан")
print("Энэ ч бас")

sys.stdout = original_stdout
captured_output = string_io.getvalue()
print(f"Баригдсан: {captured_output}")