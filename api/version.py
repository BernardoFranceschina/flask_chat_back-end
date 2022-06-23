from flask_restful import Resource, Api

class Version(Resource):
    def get(self):
        return {'API': '0.2'}
