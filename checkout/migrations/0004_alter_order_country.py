# Generated by Django 3.2.4 on 2021-07-18 15:17

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_lineitem_total_orderlineproduct_lineproduct_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]