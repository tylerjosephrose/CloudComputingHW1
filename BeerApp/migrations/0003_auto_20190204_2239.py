# Generated by Django 2.1.5 on 2019-02-04 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerApp', '0002_beer_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
