
from flask import session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
#可以用来制定session的位置

from info import create_app,db

import logging



app = create_app('testing')

manager = Manager(app)
#将app与db链接起来
Migrate(app,db)
manager.add_command('db',MigrateCommand)



@app.route('/')
def index():
    session["name"] = "itheima"
    logging.debug('测试bug')
    logging.info('info数据')
    logging.error('错误数据')
    return 'inde333333x'


if __name__ == '__main__':
    manager.run()