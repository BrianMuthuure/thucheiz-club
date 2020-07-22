# Generated by Django 2.2.5 on 2020-07-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='opponent_image',
            field=models.ImageField(default='logo.png', upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='club',
            field=models.CharField(default='Thucheiz United', editable=False, max_length=200),
        ),
    ]