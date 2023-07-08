from flask import current_app
from pymongo import MongoClient

def get_database():
    client = MongoClient(current_app.config['CONNECTION_STRING'])
    return client['tac_me']

def get_memes_collection():
    return get_database()['memes']

def get_user_collection():
    return get_database()['users']