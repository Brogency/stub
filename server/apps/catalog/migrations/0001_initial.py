# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('available_languages', multiselectfield.db.fields.MultiSelectField(default='ru', max_length=50, verbose_name='Available languages', choices=[('ru', 'Russian'), ('en', 'English')])),
                ('title', models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(null=True, upload_to='catalog/%Y/%m/%d', blank=True)),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('short_description', models.TextField(verbose_name='Short description')),
                ('short_description_ru', models.TextField(null=True, verbose_name='Short description')),
                ('short_description_en', models.TextField(null=True, verbose_name='Short description')),
                ('description', redactor.fields.RedactorField(verbose_name='Description')),
                ('description_ru', redactor.fields.RedactorField(null=True, verbose_name='Description')),
                ('description_en', redactor.fields.RedactorField(null=True, verbose_name='Description')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden')),
                ('created', models.DateTimeField(null=True, verbose_name='Created', blank=True)),
            ],
            options={
                'verbose_name': 'Catalog (RENAME)',
                'verbose_name_plural': 'Catalog (RENAME)',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name='\u0438\u043c\u044f')),
                ('name_ru', models.TextField(null=True, verbose_name='\u0438\u043c\u044f')),
                ('name_en', models.TextField(null=True, verbose_name='\u0438\u043c\u044f')),
                ('hidden', models.BooleanField(default=False, verbose_name='hidden')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='catalog.Category', null=True),
        ),
    ]
