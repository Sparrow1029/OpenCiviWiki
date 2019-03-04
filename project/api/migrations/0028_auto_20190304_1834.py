# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-04 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20190226_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bill',
            name='source',
            field=models.CharField(choices=[(b'sunlight', b'sunlight'), (b'propublica', b'propublica')], default=b'propublica', max_length=50),
        ),
    ]
