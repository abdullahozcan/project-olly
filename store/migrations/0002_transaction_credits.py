# Generated by Django 2.0.1 on 2018-04-12 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='credits',
            field=models.PositiveSmallIntegerField(default=5),
            preserve_default=False,
        ),
    ]