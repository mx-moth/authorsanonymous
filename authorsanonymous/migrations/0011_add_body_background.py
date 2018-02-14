# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-14 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('authorsanonymous', '0010_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='body_background',
            field=models.ForeignKey(blank=True, help_text="Background image for this page. If not set, the background image in the <a href='/admin/settings/authorsanonymous/sitecopy/'>site copy</a> will be used instead.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='fancypage',
            name='body_background',
            field=models.ForeignKey(blank=True, help_text="Background image for this page. If not set, the background image in the <a href='/admin/settings/authorsanonymous/sitecopy/'>site copy</a> will be used instead.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='sitecopy',
            name='body_background',
            field=models.ForeignKey(blank=True, help_text='Default background image for all pages', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
