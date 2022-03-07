from pymongo import MongoClient
import random
import string

client = MongoClient('mongodb://localhost:27017/') 
db = client.users 

def login(username, password):  
        user = { 

                'username' : username,
                'password' : password
        }

        if (db.users.find_one({'username': { '$eq': username },'password': password})):
                return True 
        else: 
                return False 

def migrate(): 
        db.users.insert_one( 
                { 
                        'username' : 'ZeU!ski', 
                        'password' : "METACTF{Br3ak_Th3_m0NgO_w!tH_ReGeX}"
                })