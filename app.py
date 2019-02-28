from flask import Flask, request
from flask_jwt import JWT,jwt_required
from flask_restful import Api

from security import authenticate, identity
from resources.user import UserRegisterUser
from resources.item import Item, ItemList
from resources.store import Store, Storelist
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'super-secret'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.secret_key = 'bhagath'

jwt = JWT(app, authenticate, identity) #auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegisterUser, '/register')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Storelist, '/stores')



if __name__ == '__main__':
    from db import DB
    DB.init_app(app)
    app.run(port = 7000, debug=True)
   