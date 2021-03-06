# Generated by Django 2.2.5 on 2020-11-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('completed', 'completed')], max_length=200, null=True)),
                ('coach', models.ManyToManyField(blank=True, to='main.Coach')),
                ('player', models.ManyToManyField(blank=True, to='main.Player')),
            ],
        ),
    ]
