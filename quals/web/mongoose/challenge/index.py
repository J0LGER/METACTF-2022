#!/usr/bin/env python3 
from flask import * 
import db

app = Flask(__name__) 

app.config['MONGODB_SETTINGS'] = { 
	
	'db': 'users',  
	'host': 'localhost', 
	'port': '27017' 
				}

@app.route('/')
def index(): 
	return render_template('index.html') 

@app.route('/login', methods= ['POST'])
def authenticate():  
	try:
		if 'application/json' in request.content_type : 
			user = request.get_json()
			if db.login(user['username'],user['password']): 
				return jsonify({'url': '/success'}), 302 
			else:  
				return jsonify({'message': 'Invalid Username or Password!'}), 401

	except: 
 		return f""" 
		<!DOCTYPE html>
    	<html>
    	<h1>Unexpected Error.. </h1>
 		</html>
 		""", 400 		

@app.route('/success', methods=['GET'])
def success(): 
	return jsonify({'message': 'Successfull login!'})

if __name__ == '__main__':
	db.migrate()
	app.run(host="0.0.0.0", port=8080, debug=False) 


