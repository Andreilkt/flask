import sqlite3

connection = sqlite3.connect('static/database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, desk) VALUES (?, ?, ?)",
            ('Кайты', 'Новые', 'Однослойные')
            )

cur.execute("INSERT INTO posts (title, content, desk) VALUES (?, ?, ?)",
            ('Парапланы', 'Новые','Двухслойные')
            )
cur.execute("INSERT INTO posts (title, content, desk) VALUES (?, ?, ?)",
            ('Paraplan', 'Vega 4', 'Двухслойный')
            )

connection.commit()
connection.close()