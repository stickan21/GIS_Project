# coding: utf-8

"""
    forms.py
    ~~~~~~~~
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import FloatField, StringField, SubmitField, IntegerField
from wtforms.validators import Required, EqualTo

class FeatureForm(FlaskForm):
    """ Feature Form"""
    ListPrice = FloatField()
    DOM = IntegerField()
    CDOM = IntegerField()
    Bedrooms = IntegerField()
    YearBuilt = IntegerField()
    LotSqFt = FloatField()
    StructureSqFt = FloatField()
    BathsFull = IntegerField()
    BathsHalf = FloatField()
    GarageSpaces = IntegerField()
    ParkingSpaces = IntegerField()
    NumberUnits = IntegerField()
    StoriesTotal = IntegerField()
    HOAFee = FloatField()
    Points = StringField()
    clickPointLat = StringField()
    clickPointLng = StringField()

    go = SubmitField('Submit')
