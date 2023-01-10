from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.GGI

users = db.users
grants = db.grants

#todo: add,remove,update users method 



#todo: add,remove,update grants method 