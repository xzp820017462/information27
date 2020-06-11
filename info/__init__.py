from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from flask import Flask,session
from flask_migrate import Manager,Migrate
from flask_wtf import CSRFProtect
from config import config


app = Flask(__name__)
app.config.from_object(config['Testing'])
db = SQLAlchemy(app)
redis_sotre = StrictRedis(host=config['Testing'].REDIS_HOST,port=config['Testing'].REDIS_PORT)
CSRFProtect(app)
Session(app)


