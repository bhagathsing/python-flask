from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "'{}' store is already exists".format(name)}
        store = StoreModel(name)
        try:
            store.insert()
        except:
            return {'message': 'An error occured while creating store'}, 500
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}


class Storelist(Resource):
    def get(self):
        stores = StoreModel.query.all()
        return {'stores': [store.json() for store in stores]}

