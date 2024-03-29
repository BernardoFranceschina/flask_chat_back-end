from flask import Flask, make_response, session
from api.version import *
from api.login import *
from api.logout import *
from api.signup import *
from api.users import *
from api.createRoom import *
from api.rooms import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Version, '/')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Signup, '/signup')
api.add_resource(Users, '/users')
api.add_resource(CreateRoom, '/create-room')
api.add_resource(Rooms, '/room')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

