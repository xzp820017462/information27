
from flask import session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
#可以用来制定session的位置

from info import app,db

                   #mysql+pymysql://root:dzd123@localhost/你的数据库名






manager = Manager(app)
#将app与db链接起来
Migrate(app,db)
manager.add_command('db',MigrateCommand)



@app.route('/')
def index():
    session["name"] = "itheima"
    return 'inde333333x'

if __name__ == '__main__':
    manager.run()