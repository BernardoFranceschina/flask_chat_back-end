from flask_restful import Resource, Api, reqparse
from database.database import Database
from flask import jsonify

parser = reqparse.RequestParser()

class CreateRoom(Resource):
    def post(self):
        parser.add_argument('nome', required=True, help='Nome do grupo é obrigatório')
        parser.add_argument('users', required=True, help='Usuários é obrigatório', action='append')
        parser.add_argument('session', required=True)
        data = parser.parse_args()
        if len(data.users) > 1:
            room = Database().add_room(data.nome)
        else:
            room = Database().add_room(eval(data.users[0])["username"])
        for i in data.users:
            Database().add_participant(room, eval(i)['id'])
        Database().add_participant(room, data.session)
        return jsonify({'message': 'success'})
