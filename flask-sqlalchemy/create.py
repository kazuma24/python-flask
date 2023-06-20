import sqlite3
conn = sqlite3.connect('Test.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE Shohin (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)')
conn.commit()
conn.close()

