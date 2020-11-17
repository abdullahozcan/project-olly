# Generated by Django 2.2.15 on 2020-11-17 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaptainMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('about_us', models.CharField(blank=True, default='Forever a mystery', max_length=250)),
                ('total_earning', models.PositiveSmallIntegerField(default=0)),
                ('website', models.CharField(blank=True, default='No Website', max_length=100)),
                ('twitter', models.CharField(blank=True, default='None Linked', max_length=15)),
                ('twitch', models.CharField(blank=True, default='None Linked', max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('num_matchloss', models.SmallIntegerField(default=0)),
                ('num_matchwin', models.SmallIntegerField(default=0)),
                ('num_wagerwin', models.SmallIntegerField(default=0)),
                ('num_wagerloss', models.SmallIntegerField(default=0)),
                ('num_tournywin', models.SmallIntegerField(default=0)),
                ('numtournyloss', models.SmallIntegerField(default=0)),
                ('totalxp', models.PositiveSmallIntegerField(default=0)),
                ('rank', models.PositiveSmallIntegerField(default=100)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('image', models.ImageField(blank=True, upload_to='team_images')),
                ('captain', models.ManyToManyField(related_name='teamcaptain', through='teams.CaptainMembership', to=settings.AUTH_USER_MODEL)),
                ('founder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='founder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
                'ordering': ['updated'],
            },
        ),
        migrations.CreateModel(
            name='TeamInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire', models.DateTimeField()),
                ('captain', models.CharField(choices=[('captain', 'Captain'), ('player', 'Player')], default='player', max_length=20)),
                ('accepted', models.BooleanField(default=False)),
                ('declined', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('hasPerms', models.BooleanField(default=False)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frominvite', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitedto', to='teams.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toinvite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(through='teams.TeamInvite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='captainmembership',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='captainmembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captainperson', to=settings.AUTH_USER_MODEL),
        ),
    ]
