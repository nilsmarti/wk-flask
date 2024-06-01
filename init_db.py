import sqlite3

conn = sqlite3.connect('wanikani.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    api_key TEXT NOT NULL
)
''')

conn.commit()
conn.close()

