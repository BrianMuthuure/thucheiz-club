# Generated by Django 2.2.5 on 2020-10-09 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('injury', '0005_auto_20201009_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='injury',
            name='players',
        ),
    ]
