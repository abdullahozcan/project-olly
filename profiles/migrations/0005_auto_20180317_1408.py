# Generated by Django 2.0.3 on 2018-03-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180329_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='twitter_profile',
            field=models.CharField(blank=True, default='No Twitter Linked', max_length=15),
        ),
    ]