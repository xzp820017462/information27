from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

import pymysql
app = Flask(__name__)                    #mysql+pymysql://root:dzd123@localhost/你的数据库名
class Config(object):
    app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:@127.0.0.1:3306/information27"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    DEBUG = True


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_sotre = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
Migrate(app,db)


CSRFProtect(app)
manager = Manager(app)
#将app与db链接起来
Migrate(app,db)
manager.add_command('db',MigrateCommand)



app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()