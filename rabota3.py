import sqlite3
connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()
cursor.execute('CREATE INDEX idx_email ON Users (email)')
connection.commit()
connection.close()