from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from flask import Flask,session
from flask_migrate import Manager,Migrate
from flask_wtf import CSRFProtect
from config import config
#在flask里面可以先初始化扩展的对象,然后再调用init_app
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config['Testing'])
    db.init_app(app)
    redis_sotre = StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)
    CSRFProtect(app)
    Session(app)
    return app

