# Generated by Django 3.1.6 on 2021-03-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=255)),
                ('call', models.BigIntegerField()),
                ('fb_link', models.CharField(max_length=255)),
                ('twitter_link', models.CharField(max_length=255)),
                ('instagram_link', models.CharField(max_length=255)),
                ('youtube_link', models.CharField(max_length=255)),
            ],
        ),
    ]
