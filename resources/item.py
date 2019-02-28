from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required
import sqlite3

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type= float, 
        required= True, 
        help="This field can not be left blank")

    parser.add_argument('store_id', 
        type= int, 
        required= True, 
        help="Every item needs store id.")
    
   

    @jwt_required()
    def get(this, name):
        item = ItemModel.find_by_name(name)
        if item:
           return item.json()
        else:
            return {'message': 'Item is not found'}, 404


  #  @jwt_required()
    def post(this, name):
        val  = ItemModel.find_by_name(name)
        print('val0', val)
        if val:
            return {'message': "An item with name '{}' already exist".format(name)}, 400
            
        data = Item.parser.parse_args()

       # item = ItemModel(name, data["price"], data['store_id'])
        item = ItemModel(name, **data)
        print('DDD',item)
        try:
           # item.insert()
           item.insert()
        except:
            return { 'message': 'An error occured inserting the item'}, 500
        return item.json(), 201

    @jwt_required()
    def delete(this, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = 'DELETE FROM items WHERE name=?'
        # cursor.execute(query, (name,))
        # connection.commit()
        # connection.close()

        return {'message': 'Item has deleted successfully!'}

    @jwt_required()
    def put(this, name):
       # data = request.get_json()
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
       # updated_item = ItemModel(name, data['price'], data['store_id'])
        if item is None:
           # item = ItemModel(name, data['price'], data['store_id'])
           item = ItemModel(name, **data)
        else:
           item.price = data['price']

        item.save_to_db()
        return item.json()

    

class ItemList(Resource):
    def get(this):
        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = 'SELECT * FROM items'
        # result = cursor.execute(query)
        result = ItemModel.query.all()
        items = []
        # for row in result:
        #    items.append({'name': row.name, 'price':row.price})
        #return {'items': items}, 201
        #return {'items': [item.json() for item in result]}, 201
        
        return {'items': list(map(lambda x: x.json(), result))}, 201

