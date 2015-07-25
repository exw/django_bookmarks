# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='tag',
            name='bookmarks',
            field=models.ManyToManyField(to='bookmarks.Bookmark'),
        ),
    ]
