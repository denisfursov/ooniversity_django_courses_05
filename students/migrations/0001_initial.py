# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='Student name')),
                ('surname', models.CharField(max_length=90, verbose_name='Student surname')),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(blank=True, max_length=40, null=True)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
        ),
    ]
