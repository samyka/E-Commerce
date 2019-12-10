# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import enumfields.fields
from django.db import migrations, models

import E-Commerce.core.fields
import E-Commerce.xtheme.models


class Migration(migrations.Migration):
    replaces = [
        ('E-Commerce_xtheme', '0001_initial'),
        ('E-Commerce_xtheme', '0002_md_to_html'),
        ('E-Commerce_xtheme', '0003_shop_theme'),
        ('E-Commerce_xtheme', '0004_convert_shop_themes'),
        ('E-Commerce_xtheme', '0005_alter_names'),
    ]

    dependencies = [
        ('E-Commerce', '0001_squashed_0039_alter_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedViewConfig',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('shop', models.ForeignKey(
                    to='E-Commerce.Shop',
                    null=True,
                    related_name='saved_views_config')),
                ('theme_identifier', models.CharField(
                    verbose_name='theme identifier',
                    db_index=True,
                    max_length=64)),
                ('view_name', models.CharField(
                    verbose_name='view name', db_index=True, max_length=64)),
                ('created_on', models.DateTimeField(
                    verbose_name='created on', auto_now_add=True)),
                ('status', enumfields.fields.EnumIntegerField(
                    enum=E-Commerce.xtheme.models.SavedViewConfigStatus,
                    verbose_name='status',
                    db_index=True)),
                ('_data', E-Commerce.core.fields.TaggedJSONField(
                    db_column='data',
                    verbose_name='internal data',
                    default=dict)),
            ], ),
        migrations.CreateModel(
            name='ThemeSettings',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('shop', models.ForeignKey(
                    to='E-Commerce.Shop', null=True,
                    related_name='themes_settings')),
                ('theme_identifier', models.CharField(
                    db_index=True,
                    verbose_name='theme identifier',
                    max_length=64)),
                ('active', models.BooleanField(
                    db_index=True, verbose_name='active', default=False)),
                ('data', E-Commerce.core.fields.TaggedJSONField(
                    db_column='data', verbose_name='data', default=dict)),
            ], ),
        migrations.AlterUniqueTogether(
            name='themesettings',
            unique_together=set([('theme_identifier', 'shop')]), ),
    ]
