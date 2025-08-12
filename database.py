import sqlite3

def connect():
    conn = sqlite3.connect('hrms.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            department TEXT,
            salary REAL
        )
    """)
    conn.commit()
    conn.close()

def insert(name, age, gender, department, salary):
    conn = sqlite3.connect('hrms.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL,?,?,?,?,?)",
                (name, age, gender, department, salary))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('hrms.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('hrms.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, age, gender, department, salary):
    conn = sqlite3.connect('hrms.db')
    cur = conn.cursor()
    cur.execute("""UPDATE employee SET name=?, age=?, gender=?, department=?, salary=? WHERE id=?""",
                (name, age, gender, department, salary, id))
    conn.commit()
    conn.close()
