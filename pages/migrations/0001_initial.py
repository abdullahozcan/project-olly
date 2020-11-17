# Generated by Django 2.2.15 on 2020-11-17 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('singletournaments', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontPageSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('subhead', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='carousel_images')),
            ],
            options={
                'verbose_name_plural': 'Front Page Slides',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('website', models.URLField(blank=True, null=True)),
                ('twitter', models.CharField(blank=True, default='#', max_length=100)),
                ('bio', models.TextField()),
                ('logo', models.ImageField(blank=True, upload_to='partner_images')),
            ],
        ),
        migrations.CreateModel(
            name='SocialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitchchannel', models.URLField(blank=True, null=True, verbose_name='twitch_channel')),
                ('youtubechannel', models.URLField(blank=True, null=True, verbose_name='youtube_channel')),
                ('twitterprofile', models.URLField(blank=True, null=True, verbose_name='twitter_profile')),
                ('facebookpage', models.URLField(blank=True, null=True, verbose_name='facebook_page')),
                ('instagrampage', models.URLField(blank=True, null=True, verbose_name='instagram_page')),
                ('stream', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': 'Social info',
            },
        ),
        migrations.CreateModel(
            name='StaticInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField(default='about us')),
                ('terms', models.TextField(default='terms of service')),
                ('block1text', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('block1link', models.URLField(blank=True, null=True)),
                ('block1_img', models.ImageField(blank=True, upload_to='carousel_images')),
                ('block2text', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('block2link', models.URLField(blank=True, null=True)),
                ('block2_img', models.ImageField(blank=True, upload_to='carousel_images')),
                ('block3text', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('block3link', models.URLField(blank=True, null=True)),
                ('block3_img', models.ImageField(blank=True, upload_to='carousel_images')),
                ('featured_tournament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_tournament', to='singletournaments.SingleEliminationTournament')),
            ],
            options={
                'verbose_name_plural': 'Static info',
            },
        ),
    ]
