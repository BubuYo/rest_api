# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 08:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='highlighted',
        ),
    ]
