from flask_restful import Resource, Api, reqparse
from database.database import Database
from flask import jsonify


class Users(Resource):
    def get(self):
        users = Database().get_users()
        for user in users:
            user.pop('password', None)
        return jsonify(users)
