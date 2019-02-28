import sqlite3
from db import DB

class UserModel(DB.Model):
    __tablename__ = 'users'


    id = DB.Column(DB.Integer, primary_key = True)
    username = DB.Column(DB.String(80))
    password = DB.Column(DB.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_user_name(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username=?'
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user
    
    @classmethod
    def find_by_user_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE id=?'
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

