# Generated by Django 2.0.1 on 2018-04-13 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0010_auto_20180407_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='disputed',
            field=models.BooleanField(default=False),
        ),
    ]