# Generated by Django 2.2.12 on 2020-12-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaguesettings',
            name='allow_fa',
            field=models.BooleanField(default=False),
        ),
    ]
