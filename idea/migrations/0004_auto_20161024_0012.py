# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0003_auto_20161023_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='tags',
            field=models.CommaSeparatedIntegerField(max_length=100),
        ),
    ]