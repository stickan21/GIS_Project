# -*- coding: utf-8 -*-
import os
import logging
from flask import ( 
    render_template, 
    request)

from . import app_caller

logger = logging.getLogger(__name__)


# handler for upload data file
@app_caller.route('/hello/', methods=('GET', 'POST'))
def hello():
    return render_template('app/result.html', result="Yeah")
