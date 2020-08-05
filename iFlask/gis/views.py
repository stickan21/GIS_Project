# -*- coding: utf-8 -*-
import os
import logging
import warnings
import json
from ast import literal_eval
from flask import (
    jsonify,
    render_template, 
    request)

from .forms import FeatureForm

from . import gis_caller
from .model import GIS

logger = logging.getLogger(__name__)


# handler for form
@gis_caller.route('/', methods=('GET', 'POST'))
def form():
    form = FeatureForm()
    data = {}

    if form.is_submitted(): # save frontend data to backend dict.

        data['ListPrice'] = form.ListPrice.data
        data['DOM'] = form.DOM.data  #tian
        data['CDOM'] = form.CDOM.data#tian
        data['Bedrooms'] = form.Bedrooms.data #1-7
        data['YearBuilt'] = form.YearBuilt.data #####
        data['LotSqFt'] = form.LotSqFt.data #tian
        data['StructureSqFt'] = form.StructureSqFt.data #####
        data['BathsFull'] = form.BathsFull.data #####
        data['BathsHalf'] = form.BathsHalf.data #####
        data['GarageSpaces'] = form.GarageSpaces.data #####
        data['ParkingSpaces'] = form.ParkingSpaces.data #tian
        data['NumberUnits'] = form.NumberUnits.data #tian 0
        data['StoriesTotal'] = form.StoriesTotal.data #tian 1
        data['HOAFee'] = form.HOAFee.data #tian
        # the Points format must like'(31.456, 156.3546),(-117.98583, 34.0737809)'
        data['POINTS'] = [int(item) for item in form.Points.data.split(',')]
        # Added Feature: Lat and Lng for click point.
        data['clickPointLat'] = form.clickPointLat.data
        data['clickPointLng'] = form.clickPointLng.data

        # test
        # data['ListPrice'] = 197000.0
        # data['DOM'] = 82.0
        # data['CDOM'] = 185.0
        # data['Bedrooms'] = 2.0
        # data['YearBuilt'] = 1978.0
        # data['LotSqFt'] = 0.0
        # data['StructureSqFt'] = 900.0
        # data['BathsFull'] = 2.0
        # data['BathsHalf'] = 0.0
        # data['GarageSpaces'] = 2.0
        # data['ParkingSpaces'] = 2.0
        # data['NumberUnits'] = 100.0
        # data['StoriesTotal'] = 0.0
        # data['HOAFee'] = 250.0
        # data['POINTS'] = list(literal_eval('(-117.8639059, 33.7477946),(-117.98583, 34.0737809),(-118.00609, 34.576074),(-117.817744, 34.033266),(-118.359678, 34.217548),(-118.30086, 33.731388)'))

        gis = GIS()
        results = gis.run(data)

        if results:
            result = {'status': 'success', 'data': round(results[0], 2)}
        else:
            result = {'status': 'failed', 'data':''}

        return jsonify(result)

    return render_template('gis/result.html', form=form)


