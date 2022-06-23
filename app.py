from flask_socketio import SocketIO, join_room, leave_room, send
from router import *

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def connect():
    print('Conexão feita com sucesso!')


@socketio.on('disconnect')
def disconnect():
    print('Cliente foi desconectado')


@socketio.on('send_message_room')
def send_message_room(message, room):
    send(message, to=room)
    print('Message:', message, '\nRoom:', room)


@socketio.on('join')
def on_join(user, room):
    join_room(room)
    send(user + ' has entered the room.', to=room)


@socketio.on('leave')
def on_leave(user, room):
    leave_room(room)
    send(user + ' has left the room.', to=room)


if __name__ == '__main__':
    socketio.run(app, debug=True)
