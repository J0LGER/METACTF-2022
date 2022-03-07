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

	if (db.users.find_one(user)):
 		return True 
	else: 
 		return False 	

def migrate(): 
	db.users.insert_one( 
		{ 
			'username' : 'Morty', 
			'password' : "".join(random.choices(string.ascii_letters+string.digits,k=12))
 		})
