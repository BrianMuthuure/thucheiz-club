# Generated by Django 2.2.5 on 2020-10-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_auto_20201002_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='opponent_logos'),
        ),
    ]