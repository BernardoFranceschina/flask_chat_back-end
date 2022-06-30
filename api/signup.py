from flask_restful import Resource, Api, reqparse
from database.database import Database
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help='Nome de usuário é obrigatório')
parser.add_argument('password', required=True, help='Senha é obrigatória')


class Signup(Resource):
    def post(self):
        data = parser.parse_args()
        if data['username'] and data['password']:
            Database().add_user(data['username'], data['password'])
            return jsonify({'message': 'success'})
        return jsonify({'message': 'failed'})
