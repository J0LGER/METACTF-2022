from flask import * 
import db 
from flask_jwt_extended import *


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
                 'db': 'users',
                 'host': 'localhost',
                 'port': 27017  }

app.config['JWT_SECRET_KEY'] = 'SchwiftyWifty'                  
jwt = JWTManager(app)

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
			access_token = create_access_token(identity = user['username'])
			 
			return jsonify({ "token": access_token }) 
			#TO-DO: Implement JWT handling in front-end 
 				 
		else: 
   			return jsonify(message= "Incorrect Username or Password!")  
	except:
		return jsonify(error = "Some unexpected error occured")


@app.route('/garage', methods = ['GET'])
@jwt_required()  
def garage(): 
	return "<h1> You're In </h1>"


if __name__ == '__main__':
	
	db.migrate()
	app.run(host="127.0.0.1", port=8080, debug=True) 
