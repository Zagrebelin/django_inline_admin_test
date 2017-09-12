# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20170912_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Something',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tltle', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='departament',
            name='something',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='first.Something'),
            preserve_default=False,
        ),
    ]
