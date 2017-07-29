# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_auto_20170728_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='alumni',
            name='user_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='username_roll',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]