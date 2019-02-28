import sqlite3
from flask_restful import Resource, reqparse
from flask import Flask, request
from models.user import UserModel

class UserRegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type= str, 
        required= True, 
        help="This field can not be blank")
    parser.add_argument('password', 
        type= str, 
        required= True, 
        help="This field can not be blank")
    
    def post(self):
        
        data = UserRegisterUser.parser.parse_args()

        if(UserModel.find_by_user_name(data['username'])):
            return {'message': data['username'] + ' is already exist'}, 400
        

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL, ?, ? )'

        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {'message': 'User register successfull!'}, 201
