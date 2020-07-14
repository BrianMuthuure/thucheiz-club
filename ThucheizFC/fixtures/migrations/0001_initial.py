# Generated by Django 2.2.5 on 2020-07-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(default='Stars United', editable=False, max_length=200)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('opponent', models.CharField(max_length=200)),
                ('stadium', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
