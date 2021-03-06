# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-18 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20170714_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopDream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
        migrations.AlterModelOptions(
            name='dream',
            options={'ordering': ['-priority_dream']},
        ),
        migrations.AddField(
            model_name='topdream',
            name='dreams',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.Dream'),
        ),
    ]
