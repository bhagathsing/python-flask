import sqlite3
from db import DB

class StoreModel(DB.Model):
    __tablename__ = 'stores'


    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(80))

    items = DB.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [ item.json() for item in self.items.all() ]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
      
    def insert(self):
       print(self)
       DB.session.add(self)
       DB.session.commit()

    def delete_from_db(self):
        DB.session.delet(self)
        DB.session.commit()
