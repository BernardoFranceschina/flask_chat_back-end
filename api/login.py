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
        session['user_session'] = uuid.uuid4()
        if Database().get_user(data['username'], data['password']):
            return True
        return False

    def get(self):
        session['user_session'] = uuid.uuid4()
