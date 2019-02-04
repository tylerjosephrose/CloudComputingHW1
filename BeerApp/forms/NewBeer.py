from django.forms import ModelForm
from BeerApp.models import Beer

import datetime

class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'brewery', 'style', 'description', 'abv', 'ibu']

