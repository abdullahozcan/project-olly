# Generated by Django 2.2.15 on 2020-12-31 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_auto_20201215_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='config_generated',
            field=models.BooleanField(default=False),
        ),
    ]