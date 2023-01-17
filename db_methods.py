from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.GGI

users = db.users
grants = db.grants

#todo: add,remove,update users method 

def register_user(username = None, password = None):
    data = {
        "Name": str(username)
        "Password": str(password)
    }
    users.insert_one(data).inserted_id


def patch_user(username = None, password = None):
    resp = ""
    resp = users.find_one({"Name": username})
    if resp == "":
        register_user(username,password)
    else:
        filter = { 'Name': username }
        newvalues = { "$set": { 'Name': username,'Password': password} }
        users.update_one(filter, newvalues)

def remove_user(username = None, password = None):
    data = {
        "Name": str(username)
        "Password": str(password)
    }
    users.delete_one(myquery)


#todo: add,remove,update grants method 

def add_grant(name = None, ammount = None):
    data = {
        "Name": str(name)
        "Ammount": str(ammount)
    }
    grants.insert_one(data).inserted_id
    

def patch_(name = None, ammount = None):
    resp = ""
    resp = grants.find_one({"Name": name})
    if resp == "":
        add_grant(name,ammount)
    else:
        filter = { 'Name': name }
        newvalues = { "$set": { 'Name': name,'Ammount': ammount} }
        grants.update_one(filter, newvalues)

def remove_(name = None, ammount = None):
    data = {
        "Name": str(name)
        "Ammount": str(ammount)
    }
    grants.delete_one(myquery)