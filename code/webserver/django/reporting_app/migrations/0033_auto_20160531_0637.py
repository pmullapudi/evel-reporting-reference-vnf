# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting_app', '0032_auto_20160318_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fault',
            options={'ordering': ['fault_name']},
        ),
        migrations.AddField(
            model_name='fault',
            name='fault_name',
            field=models.CharField(default='name', max_length=64),
        ),
    ]