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
def send_message_room(message, room, user):
    send(message, to=room)
    Database().send_message(room, user, message)
    print('Message:', message, '\nRoom:', room)


@socketio.on('join')
def on_join(user, room):
    join_room(room)
    msgs = Database().get_user_messages(room)
    messages = []
    for i in msgs:
        user = Database().get_user_by_id(i["user_id"])
        messages.append({'msg': i["message"], 'user_id': i["user_id"], 'username': user["username"]})
    send(messages, to=room)


@socketio.on('leave')
def on_leave(user, room):
    leave_room(room)
    send(user + ' has left the room.', to=room)


if __name__ == '__main__':
    socketio.run(app, debug=True)
