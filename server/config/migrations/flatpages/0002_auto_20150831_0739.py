# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='type_editor',
            field=models.IntegerField(default=0, verbose_name='Editor_type', choices=[(0, b'RedactorEditor'), (1, b'CodeMirrorTextarea')]),
        ),
    ]
