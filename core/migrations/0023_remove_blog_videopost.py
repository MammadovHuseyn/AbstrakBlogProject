# Generated by Django 4.1.7 on 2023-03-29 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_blog_videopost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='videopost',
        ),
    ]
