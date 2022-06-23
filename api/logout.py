from flask_restful import Resource, Api, reqparse
from flask import session


class Logout(Resource):
    def get(self):
        if session.pop('user_session', None):
            return {'message': 'Usuário desconectado'}
