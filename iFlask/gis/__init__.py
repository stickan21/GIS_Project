#-*- coding: utf-8 -*-
from flask import Blueprint


gis_caller = Blueprint('gis', __name__, template_folder='templates')

from . import views

