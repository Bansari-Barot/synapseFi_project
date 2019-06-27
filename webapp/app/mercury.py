from flask import jsonify, request
from synapsepy import Client, User
import pymongo
import json
from config import Config
from app import api
from flask_restful import Resource, Api

from app import app
from app.models import User

client = Client(
    client_id='client_id_2bb1e412edd311e6bd04e285d6015267',
    client_secret='client_secret_6zZVr8biuqGkyo9IxMO5jY2QlSp0nmD4EBAgKcJW',
    fingerprint='123456',
    ip_address='127.0.0.1',
    devmode=True
    )
users=[]

class User(Resource):
    def post(self):

        body=request.get_json()
        new_user= client.create_user(body,"127.0.0.1:5000")
        result=new_user.__dict__
        #user=User(user_id=result['id'], user_refresh_token=result['body']['refresh_token'], user_emails=["test@synapsefi.com"], phone_numbers=["test@synapsefi.com", "901.111.1111"],legal_names=["Test User"]).save()
        users.append(result)
        return str(result),201

    # def get(self,user_id):
    #     user=client.get_user(user_id, full_dehydrate=True)
    #     result=user.__dict__
    #     return str(result),200

# api.add_resource(User, '/user')
api.add_resource(User, '/user')
