# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20171025_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='Mentor_Gender',
            field=models.CharField(default='X', help_text='Enter F or M', max_length=49),
        ),
    ]
