# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filestorage', '0004_auto_20150819_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.TextField(null=True, verbose_name='\u0438\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.TextField(null=True, verbose_name='\u0438\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='relativefilestorage',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=10, null=True, verbose_name='Show for this lang', choices=[('ru', 'Russian'), ('en', 'English')]),
        ),
    ]
