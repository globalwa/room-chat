from flask import session, request
from flask_socketio import Namespace, join_room, leave_room, emit
from app import socketio

from flask_socketio import Namespace, emit

class Chat(Namespace):
    def on_joined(self, data):
        room = session.get('room')
        name = session.get('name')

        join_room(room)

        emit('status', {'message': f'Server: {name} has entered the room!'}, to=room)


    def on_left(self, data):
        room = session.get('room')
        name = session.get('name')

        leave_room(room)

        emit('status', {'message': f'Server: {name} has left the room.'}, to=room)


    def on_message(self, data):
        room = session.get('room')
        name = session.get('name')

        message = data['message']

        emit('message', {'message': f'{name} says: {message}'}, to=room)


socketio.on_namespace(Chat('/chat'))