# Generated by Django 2.2.5 on 2020-11-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201116_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
