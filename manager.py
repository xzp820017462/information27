from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
#可以用来制定session的位置
from flask_session import Session
import pymysql


app = Flask(__name__)                    #mysql+pymysql://root:dzd123@localhost/你的数据库名
class Config(object):
    app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:@127.0.0.1:3306/information27"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    SECRET_KEY = "w/YHy55xaBzqquY/7IccwsDkKFedltkasyDhSVqbRWeDdzAD1Jzm+clB3iGK+Czh"
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    DEBUG = True
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    #设置是否过期
    SESSION_PERMANENT = False
    #设置session过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    #制定SESSION保存到REDIS
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)





app.config.from_object(Config)
db = SQLAlchemy(app)
redis_sotre = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
Migrate(app,db)
Session(app)

CSRFProtect(app)
manager = Manager(app)
#将app与db链接起来
Migrate(app,db)
manager.add_command('db',MigrateCommand)



@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index'

if __name__ == '__main__':
    manager.run()