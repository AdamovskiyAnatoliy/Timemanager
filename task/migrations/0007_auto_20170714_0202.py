# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20170713_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dream',
            old_name='detail_deram',
            new_name='detail_dream',
        ),
        migrations.RenameField(
            model_name='dream',
            old_name='my_deream',
            new_name='my_dream',
        ),
    ]
