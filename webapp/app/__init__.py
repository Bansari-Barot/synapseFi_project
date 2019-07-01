from flask import Flask
from pymodm import connect
from config import Config
from flask_restful import Resource, Api

app=Flask(__name__)
app.config.from_object(Config)
api=Api(app)
from app import mercury
