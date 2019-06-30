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
    fingerprint='327639869',
    ip_address='127.0.0.1',
    devmode=True
    )
users=[]

class User(Resource):
    def post(self,user_id=None):
        body=request.get_json()

        #if email id present in mongodb then don't create new user

        result=new_user.__dict__
        #user=User(user_id=result['id'], user_refresh_token=result['body']['refresh_token'], user_emails=["test@synapsefi.com"], phone_numbers=["test@synapsefi.com", "901.111.1111"],legal_names=["Test User"]).save()
        users.append(result)
        return str(result),201

    def get(self,user_id):
        user=client.get_user(user_id, full_dehydrate=True)
        #database query to get refresh_token for user with user_id
        body={
            "refresh_token":"refresh_ehG7YBS8ZiD0sLa6PQHMUxryovVkJzElC5gWROXq",
            "scope":[
                "NODES|POST",
                "NODES|GET",
                "NODE|GET",
                "TRANS|POST"
                ]
        }
        oauth_user=user.oauth(body)
        # result=oauth_user.__dict__
        return oauth_user,200

    def patch(self,user_id):
        user=client.get_user(user_id, full_dehydrate=True)
        body=request.get_json()
        result=user.update_info(body)
        return str(result)


class KYCDocument(Resource):
    def post(self,user_id):
        body=request.get_json()
        user=client.get_user(user_id, full_dehydrate=True)
        result=user.update_info(body)
        return str(result), 201

    def delete(self,user_id):
        body=request.get_json()
        user=client.get_user(user_id, full_dehydrate=True)
        result=user.user_update(body)
        return str(result), 202


class IssueRouting(Resource):
    def post(self,user_id,node_id,subnet_id=None):
        body=request.get_json()
        user=client.get_user(user_id, full_dehydrate=True)
        result=user.create_subnet(node_id,body)
        return str(result), 201

    def get(self,user_id,node_id,subnet_id):
        user=client.get_user(user_id, full_dehydrate=True)
        result=user.get_subnet(node_id, subnet_id)
        return str(result), 200

    def patch(self,user_id,node_id,subnet_id):
        user=client.get_user(user_id, full_dehydrate=True)
        body=request.get_json()
        result=user.update_subnet(node_id, subnet_id, body)
        return str(result)


class DepositAccount(Resource):
    def post(self, user_id):
        body=request.get_json()
        user=client.get_user(user_id, full_dehydrate=True)
        #open bank account
        open_account=user.create_node(body, idempotency_key='123456')
        #store node_id open_account['nodes'][0]['_id'] in db where user_id is user_id
        return str(open_aacount), 201
#         body= {
#    "type": "DEPOSIT-US",
#    "info": {
#       "nickname": "My Deposit Account",
#       "document_id": "2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8"
#    }
# }

    def get(self,user_id):
        #query to get node_id from the user_id
        node_id="5ba05ed620b3aa005882c52a"
        user=client.get_user(user_id, full_dehydrate=True)
        node = user.get_node(node_id, full_dehydrate=True, force_refresh=True)
        return str(node), 200

    def patch(self,user_id):
        #query to get node_id from the user_id
        node_id="5ba05ed620b3aa005882c52a"
        user=client.get_user(user_id, full_dehydrate=True)
        body=request.get_json()
        result=user.update_node(node_id, body)
        return str(result)


class FundWithdraw(Resource):
    def post(self,user_id,node_id):
        user=client.get_user(user_id, full_dehydrate=True)
        body=request.get_json()
        result=user.create_trans(node_id, body)
        return str(result), 201

class DebitCard(Resource):
    def post(self,user_id,node_id,subnet_id=None):
        body=request.get_json()
        user=client.get_user(user_id, full_dehydrate=True)
        result=user.create_subnet(node_id, body)

        return str(result)
    def patch(self,user_id,node_id,subnet_id):
        body=request.get_json()
        # body = {
        #     "status": "ACTIVE",
        #     "preferences": {
        #       "allow_foreign_transactions":True,
        #       "daily_atm_withdrawal_limit":10,
        #       "daily_transaction_limit":1000
        #     },
        #     "card_pin":"mlMKMv5+ekyw9M5AtqUBZxgdzj+GEjzddp93qSPw6uRXGpdNiNulVZxcbH1gGGiwEU9UeOwGmgiMaQsDkpbuh3SWY6IxSiPNHI9ryY8z/z+d8MXockQxsKnl1B+ekcLAXx9s2RZM7T6Nfoa+ABGwRV7aFGt91NYaolA0tfU1981J9juB/iljm9cz5JUKDPCxZbn+LW1f4O/5Pt3fDX9Nrre/HsuHtgc7OIu6XTvg1FCm+ds3AkFdHA0dw1aW4j5biXWVEkNpb01PIicANYXtO/AusqH8udBLh0GIU/xNSTzipk/M2hUqoTZdOo7Hu8UZgLbWUEpv7hAAY2tfu/ymsA=="
        #
        # }
        user=client.get_user(user_id, full_dehydrate=True)

        if body['status']=="ACTIVE":
            result=user.update_subnet(node_id, subnet_id, body)
        else:
            result=user.update_subnet(node_id, subnet_id, body)
        return str(result)

    def get(self,user_id,node_id,subnet_id):
        user=client.get_user(user_id, full_dehydrate=True)
        result=user.get_subnet(node_id, subnet_id)
        return str(result), 200

    def delete(self,user_id,node_id,subnet_id):
        body = {
                  "status":"TERMINATED"
                }
        user=client.get_user(user_id, full_dehydrate=True)
        result=user.update_subnet(node_id, subnet_id, body)
        return str(result)



api.add_resource(User, '/user/<string:user_id>')
api.add_resource(KYCDocument, '/kyc/<string:user_id>')

api.add_resource(DepositAccount, '/deposit_acc/<string:user_id>')
api.add_resource(IssueRouting, '/issue_routing/<string:user_id>/<string:node_id>/<string:subnet_id>')
api.add_resource(FundWithdraw, '/fund_withdraw/<string:user_id>/<string:node_id>')
api.add_resource(DebitCard, '/debitcard/<string:user_id>/<string:node_id>/<string:subnet_id>')
