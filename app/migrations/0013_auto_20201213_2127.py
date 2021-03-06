# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-13 18:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201213_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='mage',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 13, 21, 27, 19, 362665), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 13, 21, 27, 19, 363165), verbose_name='Дата'),
        ),
    ]
