# Generated by Django 2.2.5 on 2020-10-09 12:39

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201009_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]