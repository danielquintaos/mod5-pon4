from app import db
from tinydb import TinyDB
from datetime import datetime

def insert_log(command):
    db.insert({'command': command})

def get_all_logs():
    return db.all()

def insert_log(command):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.insert({'command': command, 'timestamp': timestamp})