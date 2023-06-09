# Generated by Django 4.1.7 on 2023-03-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_settings_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
