from flask import Flask
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app)
bootstrap = Bootstrap(app)

from app import routes, events