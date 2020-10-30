# Generated by Django 2.2.5 on 2020-10-30 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_adminpictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminpictures',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
