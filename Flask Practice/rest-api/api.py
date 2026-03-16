# Rest works with JSON
from flask_restful import Resource, Api
from flask import Flask, jsonify, request

app = Flask(__name__)
api = Api(app)

class Greetings(Resource):
    def get(self):
        return jsonify({'message': 'Hello, World!'})

    def post(self):
        data = request.get_json()
        name = data.get('name', 'World')
        return jsonify({'message': f'Hello, {name}!'})

api.add_resource(Greetings, '/')

if __name__ == '__main__':
    app.run(debug=True)