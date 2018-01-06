# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-05 05:07
from __future__ import unicode_literals

import authorsanonymous.models
from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authorsanonymous', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fancypage',
            name='header_body',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fancypage',
            name='header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=authorsanonymous.models.StreamField([]),
        ),
        migrations.AlterField(
            model_name='fancypage',
            name='body',
            field=authorsanonymous.models.StreamField([]),
        ),
    ]