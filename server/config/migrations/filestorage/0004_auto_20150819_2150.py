# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filestorage', '0003_auto_20150819_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestorage',
            name='created',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Created'),
        ),
    ]
