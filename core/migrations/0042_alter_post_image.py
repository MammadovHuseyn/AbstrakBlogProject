# Generated by Django 4.1.7 on 2023-05-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts'),
        ),
    ]
