from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# time and location per parameter
# geometry field for geodjango        

class tide(models.Model):
    parameterName = models.CharField(max_length=50)
    value = models.IntegerField()
    unit = models.CharField(max_length=50)
    time = models.DateTimeField(default=1)
    locationName = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField() 

class chlorosity(models.Model):
    categoryName = models.CharField(max_length=50)
    parameterName = models.CharField(max_length=50)
    value = models.IntegerField()
    unit = models.CharField(max_length=50)
    time = models.DateTimeField(default=1)
    locationName = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()    



