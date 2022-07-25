import uuid
from flask_restful import Resource, Api, reqparse
from database.database import Database
from flask import session, jsonify

parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help='Nome de usuário é obrigatório')
parser.add_argument('password', required=True, help='Senha é obrigatória')


class Login(Resource):
    def post(self):
        data = parser.parse_args()
        user = Database().get_user(data['username'], data['password'])
        if user:
            return jsonify({'user': {'session': uuid.uuid4(), 'id': user['id'], 'name': user['username']}})
        return jsonify({'user': None})
