# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import enumfields.fields
import E-Commerce.core.fields
import E-Commerce.campaigns.models.basket_conditions


class Migration(migrations.Migration):

    dependencies = [
        ('E-Commerce', '0002_rounding'),
        ('campaigns', '0002_productsinbasketcondition_operator'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProductsBasketCondition',
            fields=[
                ('basketcondition_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='campaigns.BasketCondition', parent_link=True)),
                ('operator', enumfields.fields.EnumIntegerField(verbose_name='operator', enum=E-Commerce.campaigns.models.basket_conditions.ComparisonOperator, default=1)),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity', default=1)),
                ('category', models.ForeignKey(blank=True, null=True, to='E-Commerce.Category', verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.basketcondition',),
        ),
        migrations.CreateModel(
            name='DiscountFromCategoryProducts',
            fields=[
                ('basketlineeffect_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='campaigns.BasketLineEffect', parent_link=True)),
                ('discount_amount', E-Commerce.core.fields.MoneyValueField(null=True, decimal_places=9, blank=True, help_text='Flat amount of discount.', default=None, max_digits=36, verbose_name='discount amount')),
                ('discount_percentage', models.DecimalField(null=True, decimal_places=5, blank=True, help_text='The discount percentage for this campaign.', max_digits=6, verbose_name='discount percentage')),
                ('category', models.ForeignKey(verbose_name='category', to='E-Commerce.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.basketlineeffect',),
        ),
    ]
