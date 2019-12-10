# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-07 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import parler.models
import E-Commerce.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0051_supplier_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', E-Commerce.core.fields.InternalIdentifierField(blank=True, editable=False, max_length=128, null=True, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified on')),
            ],
            options={
                'verbose_name': 'label',
                'verbose_name_plural': 'labels',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LabelTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='E-Commerce.Label')),
            ],
            options={
                'verbose_name': 'label Translation',
                'db_table': 'E-Commerce_label_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='shoptranslation',
            name='description',
            field=models.TextField(blank=True, help_text='To make your shop stand out, give it an awesome description. This is what will help your shoppers learn about your shop. It will also help shoppers find your store from the web.', verbose_name='description'),
        ),
        migrations.AddField(
            model_name='shoptranslation',
            name='short_description',
            field=models.CharField(blank=True, help_text='Enter a short description for your shop. The short description will be used to get the attention of your customer with a small but precise description of your shop.', max_length=150, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='labels',
            field=models.ManyToManyField(blank=True, to='E-Commerce.Label', verbose_name='labels'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='labels',
            field=models.ManyToManyField(blank=True, to='E-Commerce.Label', verbose_name='labels'),
        ),
        migrations.AddField(
            model_name='shop',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='shops', to='E-Commerce.Label', verbose_name='labels'),
        ),
        migrations.AlterUniqueTogether(
            name='labeltranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
