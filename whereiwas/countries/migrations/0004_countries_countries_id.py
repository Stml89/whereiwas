# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_auto_20170107_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='countries_id',
            field=models.IntegerField(default=0),
        ),
    ]