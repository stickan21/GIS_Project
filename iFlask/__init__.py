#-*- coding: utf-8 -*-
import os
from flask import Flask, request, abort
import logging
from logging.handlers import RotatingFileHandler

from .helpers import RegexConverter, setJinJa2_template_path
from .register_blueprint import register_blueprint

app = Flask(__name__,
        template_folder='templates',
        static_folder='static')

app.url_map.converters['regex'] = RegexConverter

# load config by py file
app.config.from_pyfile('config.py')

# load logger
if not os.path.exists('log'):
    os.mkdir('log')
handler = RotatingFileHandler('log/iflasker.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

register_blueprint(app)

@app.before_request
def setTemplateFolder():
    refer = request.referrer

    if app.config['DEBUG']:
        # refer = 1
        # according to the referer, choice template
        if refer and refer.find('neutronmobile.com') != -1:
            app.jinja_loader = setJinJa2_template_path(app.jinja_loader, 'neutron_mobile_templates')
        else:
            app.jinja_loader = setJinJa2_template_path(app.jinja_loader, 'templates')
    else:
        if refer and (refer.find('dataapplab.com') or refer.find('neutronmobile.com')):
            # refer = 1
            # according to the referer, choice template
            if refer.find('neutronmobile.com') != -1:
                app.jinja_loader = setJinJa2_template_path(app.jinja_loader, 'neutron_mobile_templates')
            else:
                app.jinja_loader = setJinJa2_template_path(app.jinja_loader, 'templates')
        else:
            abort(404)


