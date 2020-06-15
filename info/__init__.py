import logging
from logging.handlers import RotatingFileHandler

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
    #配置日志，并且传入配置名字，以便能获取到指定的配置所对应的日志等级
    setup_log(config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    redis_sotre = StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)
    CSRFProtect(app)
    Session(app)
    return app

def setup_log(config_name):
    logging.basicConfig(level=config[config_name].LOG_LEVEL) #调试debu级
    #创建日至记录其。知名日志保存的路径，每个文件的大小，保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log",maxBytes=1024*1024*100,backupCount=10)
    #创建日志记录格式,日志等级.输入日志信息文件名,行数,日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    #为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    #为全局的日志工具对象,(flask app 使用的)添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


