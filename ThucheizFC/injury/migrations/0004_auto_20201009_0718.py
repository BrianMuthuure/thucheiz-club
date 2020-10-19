# Generated by Django 2.2.5 on 2020-10-09 04:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('injury', '0003_auto_20201009_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='injury',
            name='injury_date',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='injury',
            name='last_edited',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='injury',
            name='players',
            field=models.CharField(blank=True, editable=False, max_length=200),
        ),
    ]