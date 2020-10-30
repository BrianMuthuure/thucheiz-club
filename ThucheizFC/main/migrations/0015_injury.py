# Generated by Django 2.2.5 on 2020-10-25 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201025_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injury_type', models.CharField(blank=True, max_length=200, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Player')),
            ],
            options={
                'verbose_name_plural': 'injuries',
            },
        ),
    ]