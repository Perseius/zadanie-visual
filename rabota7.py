import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results = cursor.fetchall()
for row in results:
    print(row)
connection.close()