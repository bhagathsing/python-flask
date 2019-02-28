import sqlite3
from db import DB

class ItemModel(DB.Model):
    __tablename__ = 'items'


    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(80))
    price = DB.Column(DB.Float(precision=2))
    store_id = DB.Column(DB.Integer, DB.ForeignKey('stores.id'))

    store = DB.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = 'SELECT * FROM items WHERE name=?'
        # result = cursor.execute(query,(name,))

        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(*row)
        # else:
        #     return None
    
    
    def insert(self):
       print(self)
       DB.session.add(self)
       DB.session.commit()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = 'INSERT INTO items VALUES (?, ?)'
        # cursor.execute(query, (self.name, self.price))
        # connection.commit()
        # connection.close()

    # def update(self):

    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = 'UPDATE items SET price=? WHERE name=?'
    #     cursor.execute(query, (self.price, self.name))
    #     connection.commit()
    #     connection.close()
    def delete_from_db(self):
        DB.session.delete(self)
        DB.session.commit()
