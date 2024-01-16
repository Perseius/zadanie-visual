import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('SELECT MIN(age) FROM Users')
min_age = cursor.fetchone()[0]
print('Минимальный возраст среди пользователей:'. mini_age)
connection.close()