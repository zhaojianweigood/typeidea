# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-11 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sidebar',
            old_name='display',
            new_name='display_type',
        ),
    ]
