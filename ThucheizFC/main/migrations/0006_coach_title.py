# Generated by Django 2.2.5 on 2020-07-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_playercontract'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='title',
            field=models.CharField(blank=True, choices=[('Manager', 'Manager'), ('Ass Manager', 'Ass Manager'), ('Gk Coach', 'GK Coach')], max_length=100, null=True),
        ),
    ]