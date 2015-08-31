# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='news.Category', null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_en',
            field=redactor.fields.RedactorField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_ru',
            field=redactor.fields.RedactorField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_description',
            field=models.TextField(verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
