#coding=utf-8
from flask import Flask
def my_app():
    app = Flask(__name__,static_url_path='')
    return app
app = my_app()