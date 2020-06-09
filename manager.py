from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import pymysql
app = Flask(__name__)                    #mysql+pymysql://root:dzd123@localhost/你的数据库名
class Config(object):
    app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:@127.0.0.1:3306/information27"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(Config)
db = SQLAlchemy(app)


app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)