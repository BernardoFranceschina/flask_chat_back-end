from flask_restful import Resource, Api, reqparse
from database.database import Database
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument('user', required=True)

class Rooms(Resource):
    def post(self):
        data = parser.parse_args()
        info = Database().get_user_rooms(data['user'])
        return jsonify(info)
