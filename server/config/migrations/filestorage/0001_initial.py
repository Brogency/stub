# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.TextField(verbose_name='имя')),
                ('hidden', models.BooleanField(default=False, verbose_name='hidden')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='FileStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('document', models.FileField(upload_to='filestorage/', verbose_name='Document')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden')),
                ('extension', models.CharField(max_length=10, null=True, blank=True, verbose_name='Extension')),
                ('description', models.CharField(max_length=150, null=True, blank=True, verbose_name='Description')),
                ('description_ru', models.CharField(max_length=150, null=True, blank=True, verbose_name='Description')),
                ('description_en', models.CharField(max_length=150, null=True, blank=True, verbose_name='Description')),
                ('category', models.ForeignKey(to='filestorage.Category', null=True, blank=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'FileStorage',
                'verbose_name_plural': 'FileStorages',
            },
        ),
        migrations.CreateModel(
            name='RelativeFileStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('languages', multiselectfield.db.fields.MultiSelectField(max_length=50, null=True, blank=True, choices=[('ru', 'Russian'), ('en', 'English')], verbose_name='Show for this lang')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Order')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('document', models.ForeignKey(to='filestorage.FileStorage', verbose_name='File')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'RelativeFileStorage',
                'verbose_name_plural': 'RelativeFileStorages',
            },
        ),
    ]
