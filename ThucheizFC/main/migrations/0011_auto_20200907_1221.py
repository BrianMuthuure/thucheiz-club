# Generated by Django 2.2.5 on 2020-09-07 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_playercontract_remaining_days'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerContract',
            new_name='Contract',
        ),
    ]