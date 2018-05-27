# Generated by Django 2.0.1 on 2018-03-29 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_social_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='social_verified',
            new_name='xbl_verified',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='psn_verified',
            field=models.BooleanField(default=False),
        ),
    ]