# Generated by Django 4.1.7 on 2023-05-07 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_subscription_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='reading_time',
            field=models.IntegerField(default=0),
        ),
    ]
