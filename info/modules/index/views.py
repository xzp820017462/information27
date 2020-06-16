from flask import render_template

from . import index_blu
from info import redis_store
@index_blu.route('/')
def index():
    #redis_store.set("name","itheima")
    #redis_store.set("name","itcast")
    return render_template('news/index.html')
