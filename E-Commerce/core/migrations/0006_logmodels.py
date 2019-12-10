# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
import enumfields.fields
import E-Commerce.utils.analog


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('E-Commerce', '0005_shopproduct_visibilty'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Attribute', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarrierLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Carrier', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyContactLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.CompanyContact', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactGroupLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.ContactGroup', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerTaxGroupLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.CustomerTaxGroup', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ManufacturerLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Manufacturer', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderLineLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.OrderLine', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderLineTaxLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.OrderLineTax', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Payment', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethodLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.PaymentMethod', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentProcessorLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.PaymentProcessor', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonContactLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.PersonContact', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMediaLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.ProductMedia', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SavedAddressLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.SavedAddress', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShipmentLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Shipment', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShipmentProductLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.ShipmentProduct', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShippingMethodLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.ShippingMethod', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShopLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Shop', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShopProductLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.ShopProduct', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuppliedProductLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.SuppliedProduct', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupplierLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Supplier', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaxClassLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.TaxClass', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaxLogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, verbose_name='log entry kind', enum=E-Commerce.utils.analog.LogEntryKind)),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(verbose_name='target', to='E-Commerce.Tax', related_name='log_entries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
