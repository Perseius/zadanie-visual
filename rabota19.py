import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
users_lits = []
for user in users:
    user_dict = {
        'id':user[0],
        'username': user[1],
        'email': user[2],
        'age': user[3]
    }
users_lits.append(user_dict)
for user in users_lits:
    print(user)
connection.close()