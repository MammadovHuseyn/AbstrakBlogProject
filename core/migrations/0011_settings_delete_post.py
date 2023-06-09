# Generated by Django 4.1.7 on 2023-03-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250, null=True)),
                ('phone1', models.CharField(max_length=50, null=True)),
                ('phone2', models.CharField(max_length=50, null=True)),
                ('facebook_url', models.URLField(verbose_name='')),
                ('instagram_url', models.URLField(verbose_name='')),
                ('twitter_url', models.URLField(verbose_name='')),
                ('linkedin_url', models.URLField(verbose_name='')),
                ('youtube_url', models.URLField(verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
