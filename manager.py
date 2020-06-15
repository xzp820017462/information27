
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




if __name__ == '__main__':
    manager.run()