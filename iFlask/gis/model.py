# coding: utf-8
from __future__ import division
import os
import numpy as np
import pandas as pd
from math import sin, cos, sqrt, atan2, radians

from .container.base import Base

# set a global variable for keep the big data
df = None

class GIS(Base): #Base class to regulate machine learning model traits.
    def __init__(self):
        global df

        super(GIS, self).__init__()
        self.picker = np.array([u'ListPrice',
                                u'DOM',
                                u'CDOM',
                                u'Bedrooms',
                                u'YearBuilt',
                                u'LotSqFt',
                                u'StructureSqFt',
                                u'BathsFull',
                                u'BathsHalf',
                                u'GarageSpaces',
                                u'ParkingSpaces',
                                u'NumberUnits',
                                u'StoriesTotal',
                                u'HOAFee']
                               )
        appPath = os.path.join(os.getcwd(), 'iFlask/gis/data')

        self.dataPath = os.path.join(appPath, 'data.pkl')
        if df is None:
            df = self.load(self.dataPath)
            df = df[(df.lat != 0) & (df.lng != 0) & (df.lat.isnull() == False) & (df.lng.isnull() == False)]
            df = df[list(['DataId']) + list(self.picker) + list(['lat', 'lng', 'SalePrice'])]
            var_NA = df.isnull().sum() != 0
            var_NA = var_NA[var_NA == True].index
            for i in var_NA:
                df[i].fillna(round(df[i].mean()), inplace = True)
        self.df = df

    def loadDvalidFromDict(self, data):
        """exactly, need a method convert data to df object"""
        # it will raise ValueError: If using all scalar values, you must must pass an index
        # reference: http://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe
        index = ['ListPrice', 'DOM', 'CDOM', 'Bedrooms', 'YearBuilt', 'LotSqFt', 'StructureSqFt', 'BathsFull',
                 'BathsHalf', 'GarageSpaces', 'ParkingSpaces', 'NumberUnits', 'StoriesTotal', 'HOAFee']
        feature = pd.Series([data[key] for key in index], index=index)

        coord = (float(data['clickPointLat']), float(data['clickPointLng']))
        samples = self.find_samples(1000, coord) # Find near by samples: number of neighbors: n.
        trainX = samples[index]
        trainY = samples['SalePrice']
        weight = samples['Weight']

        return feature, trainX, trainY, weight

    def dist(self, coord1, coord2):
        #coord1 and coord2 must be tuples of (lat, lng)
        R = 6373.0 # approximate radius of earth in km

        lat1 = radians(coord1[0])
        lon1 = radians(coord1[1])
        lat2 = radians(coord2[0])
        lon2 = radians(coord2[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def find_samples(self, n, coord):
        distance = self.df.apply(lambda row: self.dist((row['lat'], row['lng']), coord), axis=1).sort_values()[0:n]
        distance.name = "Distance"
        # Using a Bisquare kernel.
        weight = (1 - (distance/max(distance))**2)**2
        weight.name = "Weight"

        samples = self.df.loc[distance.index].merge(pd.concat([distance, weight], axis=1),
                                                    left_index = True, right_index = True)

        return samples

