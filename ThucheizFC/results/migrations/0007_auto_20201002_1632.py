# Generated by Django 2.2.5 on 2020-10-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_auto_20201002_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='club_goal',
            field=models.ManyToManyField(blank=True, null=True, to='results.ClubGoal'),
        ),
        migrations.AlterField(
            model_name='result',
            name='opponent_goal',
            field=models.ManyToManyField(blank=True, null=True, to='results.OpponentGoal'),
        ),
    ]
