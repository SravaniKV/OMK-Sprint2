# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-24 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171021_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Emp_email',
            new_name='Emp_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Men_email',
            new_name='Men_name',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='Mentor_Sex',
        ),
        migrations.AddField(
            model_name='mentor',
            name='Mentor_Gender',
            field=models.CharField(default='X', max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Employee_Address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Employee_Id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Employee_phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='Mentor_Address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='Mentor_Id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='Mentor_phone',
            field=models.CharField(max_length=10),
        ),
    ]