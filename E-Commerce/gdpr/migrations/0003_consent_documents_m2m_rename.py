# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-19 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0001_squashed_0004_auto_20160611_1202'),
        ('E-Commerce_simple_cms', '0007_gdpr'),
        ('E-Commerce_gdpr', '0002_consent_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gdpruserconsent',
            old_name='consents',
            new_name='documents'
        )
    ]
