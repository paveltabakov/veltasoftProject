# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 12:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 22, 24, 992433, tzinfo=utc))),
            ],
        ),
    ]
