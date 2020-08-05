#-*- coding: utf-8 -*-
from flask import Blueprint


app_caller = Blueprint('app', __name__, template_folder='templates')

from . import views

