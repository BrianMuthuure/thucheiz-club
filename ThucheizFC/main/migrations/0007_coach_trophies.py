# Generated by Django 2.2.5 on 2020-07-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_coach_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='trophies',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
