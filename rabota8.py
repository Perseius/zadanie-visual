import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
results = cursor.fetchall()
for row in results:
    print(row)
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVF(age) > ?',(30,))
filtered_results = cursor.fetchall()
for row in filtered_results:
    print(row)
connection.close()