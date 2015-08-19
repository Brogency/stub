# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filestorage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relativefilestorage',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(default='ru', blank=True, max_length=50, null=True, choices=[('ru', 'Russian'), ('en', 'English')], verbose_name='Show for this lang'),
        ),
    ]
