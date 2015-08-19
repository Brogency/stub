# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filestorage', '0002_auto_20150819_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestorage',
            name='created',
            field=models.DateTimeField(verbose_name='Created', default=datetime.datetime(2015, 8, 19, 21, 49, 17, 889488)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relativefilestorage',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Show for this lang', choices=[('ru', 'Russian'), ('en', 'English')], max_length=50, blank=True, null=True),
        ),
    ]
