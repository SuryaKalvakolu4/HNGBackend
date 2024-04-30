# Generated by Django 5.0 on 2024-01-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_survey_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='video_on_app',
        ),
        migrations.AddField(
            model_name='survey',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
