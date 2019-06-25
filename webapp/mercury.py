
from flask import Flask, jsonify, request
from synapsepy import Client, User
import pymongo
import json


app = Flask(__name__)



@app.route('/addUser', methods=['POST'])
def create_user():
    client = Client(
	client_id='client_id_2bb1e412edd311e6bd04e285d6015267',
	client_secret='client_secret_6zZVr8biuqGkyo9IxMO5jY2QlSp0nmD4EBAgKcJW',
	fingerprint='123456',
	ip_address='127.0.0.1',
	devmode=True
	)


    body = {
          "logins": [
            {
              "email": "test@synapsefi.com"
            }
          ],
          "phone_numbers": [
            "901.111.1111",
            "test@synapsefi.com"
          ],
          "legal_names": [
            "Test User"
          ]
        }

    new_user= client.create_user(body,"127.0.0.1:5000")

    result = new_user.__dict__


    return str(type(new_user.body))

if __name__ == '__main__':
    app.run(debug=True)
