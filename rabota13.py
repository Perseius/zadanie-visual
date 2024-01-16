import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('SELECT AVG(age) FROM Users')
total_age = cursor.fetchone()[0]
print('Средний возраст пользователей:'. average_age)
connection.close()