# Generated by Django 4.1.7 on 2023-05-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_postcomments_options_alter_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Subscription',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]