from snippets.models import chlorosity
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

def jsonGetTide(request):
     #  Haal de JSON data op
     j = urllib2.urlopen('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=waterstanden')
     j_obj = json.load(j)
     print(j_obj)
     log.debug("Entering debug mode")
     log.info("Hey there it works!!")
     return HttpResponse(j_obj)

def jsonGetChlorosity(object):
    # download and de-serialize json
     url_object = json.load(urllib2.urlopen('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=chlorositeit'))
     values = url_object['features']
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



