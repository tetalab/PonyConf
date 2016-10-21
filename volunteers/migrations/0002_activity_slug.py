# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 23:07
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
