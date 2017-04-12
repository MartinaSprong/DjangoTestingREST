from snippets.models import chlorosity
from snippets.models import tide
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import urllib2
from django.http import HttpResponse
import os
import sys
import numpy
import datetime
import time

import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def jsonGetTide(object):
     # download and de-serialize json
     tideUrl = json.load(urllib2.urlopen('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=waterstanden'))
     tideValues = tideUrl['features']
     for tideValue in tideValues:
         tideTime = tideValue['meettijd']
         correctTime = (datetime.datetime.fromtimestamp(int(tideTime)).strftime('%Y-%m-%d %H:%M:%S'))
         t1 = tide.objects.update_or_create(parameterName=tideValue['parameternaam'], 
                                                  value=tideValue['waarde'], 
                                                  unit=tideValue['eenheid'],
                                                  time=correctTime, 
                                                  locationName=tideValue['locatienaam'], 
                                                  lat=tideValue['location']['lat'], 
                                                  lon=tideValue['location']['lon'])
     log.debug("Entering debug mode")
     log.info("Hey there it works!!")
     return HttpResponse(t1)

def jsonGetChlorosity(object):
    # download and de-serialize json
     urlObject = json.load(urllib2.urlopen('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=chlorositeit'))
     values = urlObject['features']
     for value in values:
         time = value['meettijd']
         correctTime = (datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S'))
        #  print value['location']['lon']
         c1 = chlorosity.objects.update_or_create(categoryName=value['categoryDescription'], 
                                                  parameterName=value['parameternaam'], 
                                                  value=value['waarde'], 
                                                  unit=value['eenheid'],
                                                  time=correctTime, 
                                                  locationName=value['locatienaam'], 
                                                  lat=value['location']['lat'], 
                                                  lon=value['location']['lon'])
        #  print(c1)

     log.debug("Entering debug mode")
     log.info("Hey there it works!!")
     return HttpResponse(c1)



