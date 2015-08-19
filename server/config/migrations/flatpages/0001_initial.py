# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.CharField(verbose_name='URL', db_index=True, max_length=100)),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('title_ru', models.CharField(verbose_name='title', null=True, max_length=200)),
                ('title_en', models.CharField(verbose_name='title', null=True, max_length=200)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('content_ru', models.TextField(verbose_name='content', null=True, blank=True)),
                ('content_en', models.TextField(verbose_name='content', null=True, blank=True)),
                ('enable_comments', models.BooleanField(verbose_name='enable comments', default=False)),
                ('template_name', models.CharField(verbose_name='template name', help_text="Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'.", blank=True, max_length=70)),
                ('registration_required', models.BooleanField(verbose_name='registration required', default=False, help_text='If this is checked, only logged-in users will be able to view the page.')),
                ('type_editor', models.IntegerField(verbose_name='Editor_type', choices=[(0, 'RedactorEditor'), (1, 'CodeMirrorTextarea')])),
                ('header_text', models.TextField(verbose_name='Header text', null=True, blank=True)),
                ('header_text_ru', models.TextField(verbose_name='Header text', null=True, blank=True)),
                ('header_text_en', models.TextField(verbose_name='Header text', null=True, blank=True)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'verbose_name': 'flat page',
                'verbose_name_plural': 'flat pages',
                'db_table': 'django_flatpage',
                'ordering': ('url',),
            },
        ),
    ]
