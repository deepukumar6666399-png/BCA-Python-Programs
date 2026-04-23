import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Aman", 22))
    
    # Force an error
    cursor.execute("INSERT INTO students (id, name, age) VALUES (1, 'Error', 25)")
    
    conn.commit()
    print("Transaction successful.")

except:
    conn.rollback()
    print("Transaction failed. Changes rolled back.")

conn.close()