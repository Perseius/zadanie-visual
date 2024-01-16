import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print('Общее количество пользователей:', total_users)
connection.close()