from flask import Flask, session, request, render_template
from api.version import *
from api.login import *
from api.logout import *
from api.signup import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Version, '/')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Signup, '/signup')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.before_request
def before_request():
    if 'user_session' not in session and request.endpoint != 'login':
        return render_template('no_access.html')
