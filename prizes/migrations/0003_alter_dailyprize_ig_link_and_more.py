# Generated by Django 5.0 on 2024-02-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0002_badge_medal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyprize',
            name='ig_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailyprize',
            name='tiktok_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailyprize',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
