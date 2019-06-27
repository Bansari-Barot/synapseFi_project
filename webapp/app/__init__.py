from flask import Flask

from config import Config
from flask_restful import Resource, Api
app=Flask(__name__)
api=Api(app)
from app import mercury
