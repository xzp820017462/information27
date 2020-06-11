from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
#可以用来制定session的位置
from flask_session import Session
import pymysql
from config import Config


                   #mysql+pymysql://root:dzd123@localhost/你的数据库名





app = Flask(__name__)
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