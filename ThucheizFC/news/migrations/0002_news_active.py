# Generated by Django 2.2.5 on 2020-07-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]