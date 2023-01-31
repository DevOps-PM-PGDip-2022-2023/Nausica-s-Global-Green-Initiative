from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.GGI

users = db.users

def search(username = None, password = None):
    resp = ""
    # resp = users.find_one({"Name": username})
    resp = {"Name":username, "Password":password}
    if resp == "":
        return False
    
    else:
        try:
            if resp['Name'] == username and resp['Password'] == password:
                return True
            else:
                return False
        except:
            return False

