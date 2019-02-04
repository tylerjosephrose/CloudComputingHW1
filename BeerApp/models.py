from django.db import models

from datetime import datetime

class Beer(models.Model):
    name = models.CharField(max_length=255)
    brewery = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    style = models.CharField(max_length=255)
    abv = models.CharField(max_length=10)
    ibu = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published', default=datetime.now)

