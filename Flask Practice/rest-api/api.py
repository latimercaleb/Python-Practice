# Rest works with JSON
from flask_restful import Resource, Api
from jwt_check import authenticate, userid_tbl
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, create_access_token
from user import User
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'no_secrets_today'
app.config['JWT_SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWTManager(app) # Needs to setup login resource


# Simple example
class Greetings(Resource):
    def get(self):
        return jsonify({'message': 'Hello, World!'})

    def post(self):
        data = request.get_json()
        name = data.get('name', 'World')
        return jsonify({'message': f'Hello, {name}!'})

api.add_resource(Greetings, '/') # Registering the resource with the API, '/' is the endpoint for this resource

# CRUD example
writers = [] # In memory storage for writers, practicing concept
class Writer(Resource):
    def get(self, name): # Take thing, find thing in store, return that thing if thing not found return error message
        for writer in writers:
            if writer['name'] == name:
                return writer
        return {'name': None}, 404 # Implicitly returns a tuple
        #return jsonify({'error': 'Writer not found'}), 404

    def post(self, name): # Take thing, write thing to store, then return that thing
        writer = {'name': name}
        writers.append(writer)
        return name
    
    def delete(self, name):# Take thing, find thing in store, delete that thing if thing not found return error message
        for idx, writer in enumerate(writers):
            if writer['name'] == name:
                del writers[idx]
                return {'message': f'Writer {name} deleted'}
        return {'message': 'Writer not found'}

    def put(self, name):
        pass

class AllWriters(Resource):
    # @app.route("/protected") # Might need this
    @jwt_required() # This decorator ensures that this endpoint can only be accessed by authenticated users with a valid JWT
    def get(self):
        current_user = get_jwt_identity() # This function retrieves the identity of the current user from the JWT, which is typically the user's id or username
        print (current_user)
        user = userid_tbl.get(int(current_user)) # This is how you would retrieve the user object from the database using the identity from the JWT
        print (user)
        return {'logged_in_user': user.username, 'writers': writers}

api.add_resource(Writer, '/writer/<string:name>') # Registering the resource with the API, '/writer/<string:name>' is the endpoint for this resource
api.add_resource(AllWriters, '/writers') # Registering the resource with the API, '/writers' is the endpoint for this resource

# Resource for logging in and getting a JWT
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username, password) # This will return a user object if authentication is successful, or None if it fails

        # For now, we'll do a simple check. 
        # Later, you'll use: user = User.query.filter_by(username=username).first()
        if user:
            # This is the magic function that creates the token
            access_token = create_access_token(identity=str(user.id))
            return {'access_token': access_token}, 200
        
        return {"message": "Invalid credentials"}, 401

api.add_resource(Login, '/auth')


if __name__ == '__main__':
    app.run(debug=True)