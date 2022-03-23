from flask import * 
import jwt
import db
from jwt_utils import load_key, token_required
from datetime import datetime, timedelta


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
                 'db': 'users',
                 'host': 'localhost',
                 'port': 27017
				 }

app.config['KEYS_DIR'] = 'jwt_keys'
app.config['PRIMARY_KID'] = '4540608b-d3fd-42fd-8f8d-d4a83c743501'


@app.route('/') 
def index():
	return render_template("index.html") 


@app.route('/login', methods = ['GET']) 
def login(): 
	return render_template("login.html") 


@app.route('/login', methods = ['POST']) 
def authenticate():  
	user = request.get_json()
	try: 	   
		if db.login(user['username'], user['password']):
			payload = {
				'iat': datetime.utcnow(),                          # Current time
				'exp': datetime.utcnow() + timedelta(minutes=10),  # Expiration time
				'sub': user['username']
			}
			secret_key = load_key(app.config['PRIMARY_KID'])
			access_token = jwt.encode(payload, secret_key, algorithm='HS256', headers={'kid': app.config['PRIMARY_KID']})
						
			return jsonify({ "token": access_token })

			#TO-DO: Implement JWT handling in front-end 
					
		else: 
			return jsonify(message= "Incorrect Username or Password!")
	except:
		return jsonify(error = "Some unexpected error occured")


@app.route('/garage', methods = ['GET'])
@token_required()  
def garage():
	return "<h1> You're In </h1>"


if __name__ == '__main__':
	
	db.migrate()
	app.run(host="127.0.0.1", port=8080) 
