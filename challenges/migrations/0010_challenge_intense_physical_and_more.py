# Generated by Django 5.0 on 2024-02-06 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0009_intensephysicalchallenge_moderatephysicalchallenge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='intense_physical',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenges.intensephysicalchallenge'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='moderate_physical',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenges.moderatephysicalchallenge'),
        ),
    ]
