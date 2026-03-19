# Rest works with JSON
from flask_restful import Resource, Api
from flask import Flask, jsonify, request

app = Flask(__name__)
api = Api(app)

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
    def get(self):
        return {'writers': writers}

api.add_resource(Writer, '/writer/<string:name>') # Registering the resource with the API, '/writer/<string:name>' is the endpoint for this resource
api.add_resource(AllWriters, '/writers') # Registering the resource with the API, '/writers' is the endpoint for this resource

if __name__ == '__main__':
    app.run(debug=True)