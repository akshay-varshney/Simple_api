import sqlite3
conn = sqlite3.connect('books.db')
 
cur = conn.cursor()
results = cur.execute('SELECT * FROM books').fetchall()
print(results)