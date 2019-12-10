# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-07 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0020_md_to_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryLimitBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='E-Commerce.ServiceBehaviorComponent')),
                ('available_in_countries', jsonfield.fields.JSONField(blank=True, null=True)),
                ('available_in_european_countries', models.BooleanField(default=False)),
                ('unavailable_in_countries', jsonfield.fields.JSONField(blank=True, null=True)),
                ('unavailable_in_european_countries', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('E-Commerce.servicebehaviorcomponent',),
        ),
    ]
