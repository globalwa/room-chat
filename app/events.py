from collections import defaultdict
from flask import session, request, redirect, url_for
from flask_socketio import Namespace, join_room, leave_room, emit
from flask_socketio import Namespace, emit
from app import socketio

users = defaultdict(list)

class Chat(Namespace):
    def on_joined(self, data):
        room = session.get('room')
        name = session.get('name')

        users[room].append(name)

        join_room(room)

        emit('user', {'users': users[room]}, to=room)

    def on_left(self, data):
        room = session.get('room')
        name = session.get('name')

        leave_room(room)
        emit('user', {'users': users[room]}, to=room)


    def on_message(self, data):
        room = session.get('room')
        name = session.get('name')

        message = data['message']

        emit('message', {'message': f'{name} says: {message}'}, to=room)

    
    def on_disconnect(self):
        room = session.get('room')
        name = session.get('name')

        users[room].remove(name)
        emit('user', {'users': users[room]}, to=room)


socketio.on_namespace(Chat('/chat'))