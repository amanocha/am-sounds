from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://amanocha:sounds@ds163377.mlab.com:63377/heroku_lkgwp7wm')
    db = client.heroku_rfsb5xrr
    return db