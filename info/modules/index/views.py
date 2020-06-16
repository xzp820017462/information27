from flask import current_app
from flask import render_template

from . import index_blu
from info import redis_store
@index_blu.route('/')
def index():
    #redis_store.set("name","itheima")
    #redis_store.set("name","itcast")
    return render_template('news/index.html')

#在打开网页的时候.会默认请求根路径favicon.ico
@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')