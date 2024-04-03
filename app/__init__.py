from flask import Flask
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('db/db.json')

from app import views
