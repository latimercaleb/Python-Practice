# Rest works with JSON
from flask_restful import Resource
# from jwt_check import authenticate, userid_tbl
# from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, create_access_token
# from user import User
from model import Writer
from config import app, api, db

# TODO: Review table setup, and data, maybe add a few fields and integrate jwt into this side project for practice, clean up comments
class Writing(Resource):
    def get(self, name):
        writer = Writer.query.filter_by(username=name).first()
        if writer:
            return writer.json()
        else: 
            return {'name': None}, 404 

    def post(self, name): 
        writer = Writer(name)
        db.session.add(writer)
        db.session.commit()     
        return writer.json()
    
    def delete(self, name):
        writer = Writer.query.filter_by(username=name).first()
        db.session.delete(writer)
        db.session.commit()  
        return {'message': f'Writer {name} deleted'}, 200
    
    def put(self, name):
        pass

class AllWriters(Resource):
    # @jwt_required() # Commenting for now, just to use database functionality without needing to worry about JWTs, will add back in later, TODO
    def get(self):
        writers = Writer.query.all()
        return {'writers': [writer.json() for writer in writers]}
        # current_user = get_jwt_identity() # This function retrieves the identity of the current user from the JWT, which is typically the user's id or username
        # print (current_user)
        # user = userid_tbl.get(int(current_user)) # This is how you would retrieve the user object from the database using the identity from the JWT
        # print (user)
        # return {'logged_in_user': user.username, 'writers': writers}

api.add_resource(Writing, '/writer/<string:name>') # Registering the resource with the API, '/writer/<string:name>' is the endpoint for this resource
api.add_resource(AllWriters, '/writers') # Registering the resource with the API, '/writers' is the endpoint for this resource

# Resource for logging in and getting a JWT
# class Login(Resource):
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')

#         user = authenticate(username, password) # This will return a user object if authentication is successful, or None if it fails

#         # For now, we'll do a simple check. 
#         # Later, you'll use: user = User.query.filter_by(username=username).first()
#         if user:
#             # This is the magic function that creates the token
#             access_token = create_access_token(identity=str(user.id)) # TODO: Rework this to just use the username, its alot more readable and a good point of return-refactorting for active recall
#             return {'access_token': access_token}, 200
        
#         return {"message": "Invalid credentials"}, 401

# api.add_resource(Login, '/auth')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)