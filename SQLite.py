import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

print("Table created successfully.")

conn.close()