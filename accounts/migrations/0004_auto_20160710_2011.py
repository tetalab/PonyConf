# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160709_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='participation',
            name='connector',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='transport',
        ),
        migrations.AddField(
            model_name='participation',
            name='connector',
            field=models.ManyToManyField(blank=True, to='accounts.Connector', verbose_name='I can output'),
        ),
        migrations.AddField(
            model_name='participation',
            name='transport',
            field=models.ManyToManyField(blank=True, to='accounts.Transport', verbose_name="I'm ok to travel by"),
        ),
    ]