# Generated by Django 2.0.1 on 2018-03-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='social_verified',
            field=models.BooleanField(default=False),
        ),
    ]