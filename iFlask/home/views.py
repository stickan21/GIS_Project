# encoding: utf-8
# Created by woolf

import os
import logging
from flask import send_from_directory

from . import home

from flask import (
    render_template,
    request)
from flask.views import View

@home.route('/')
def index():
    # app.logger.debug('Debug test')
    return render_template('home/welcome.html')

# @home.route('/hello')
@home.route('/hello/<name>')
def hello_world(name = None):
    return render_template('home/hello.html', name=name)
    #return 'Hello, World!'

# yet another router
class MyView(View):
    methods = ['GET']

    def dispatch_request(self, name):
        return 'Hello %s!' % name

home.add_url_rule('/hello/<name>', view_func=MyView.as_view('myview'))

@home.route('/about')
def about():
    return 'The about page'

@home.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


# below method just for test
@home.route('/user/<name>')
def show_user_profile(name):
    return 'User %s name' % name

@home.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id