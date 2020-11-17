# Generated by Django 2.2.15 on 2020-11-17 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='game_images')),
            ],
        ),
        migrations.CreateModel(
            name='MapChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_map', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('map_num', models.IntegerField(blank=True, default=0, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_for', to='matches.GameChoice')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('matchnum', models.SmallIntegerField(default=0)),
                ('reported', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('bestof', models.SmallIntegerField(choices=[(0, 'Best of 1'), (1, 'Best of 3'), (2, 'Best of 5'), (3, 'Best of 7'), (4, 'Best of 9')], default=0)),
                ('teamformat', models.SmallIntegerField(choices=[(0, '1v1'), (1, '2v2'), (2, '3v3'), (3, '4v4'), (4, '5v5'), (5, '6v6')], default=1)),
                ('team1reported', models.BooleanField(default=False)),
                ('team2reported', models.BooleanField(default=False)),
                ('info', models.TextField(default='Match Info: ')),
                ('disputed', models.BooleanField(default=False)),
                ('bye_1', models.BooleanField(default=False)),
                ('bye_2', models.BooleanField(default=False)),
                ('disable_userreport', models.BooleanField(default=True)),
                ('awayteam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='awayteam', to='teams.Team')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='GameChoice', to='matches.GameChoice')),
                ('hometeam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hometeam', to='teams.Team')),
                ('loser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loser', to='teams.Team')),
                ('map', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_map', to='matches.MapChoice')),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.CreateModel(
            name='MatchStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchid', models.PositiveIntegerField(default=0)),
                ('map', models.CharField(default='unknown', max_length=255)),
                ('team1', models.CharField(default='unknown', max_length=255)),
                ('team2', models.CharField(default='unknown', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='platform_images')),
            ],
        ),
        migrations.CreateModel(
            name='SportChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown sports', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatsPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=3, max_digits=6)),
                ('kills', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('killround', models.DecimalField(decimal_places=3, max_digits=6)),
                ('adr', models.IntegerField(default=0)),
                ('ud', models.IntegerField(default=0)),
                ('ef', models.IntegerField(default=0)),
                ('f_assists', models.IntegerField(default=0)),
                ('hs', models.IntegerField(default=0)),
                ('kast', models.IntegerField(default=0)),
                ('awp_k', models.IntegerField(default=0)),
                ('twok', models.IntegerField(default=0)),
                ('threek', models.IntegerField(default=0)),
                ('fourk', models.IntegerField(default=0)),
                ('fivek', models.IntegerField(default=0)),
                ('one_v_one', models.IntegerField(default=0)),
                ('one_v_two', models.IntegerField(default=0)),
                ('one_v_three', models.IntegerField(default=0)),
                ('one_v_four', models.IntegerField(default=0)),
                ('one_v_five', models.IntegerField(default=0)),
                ('f_kills', models.IntegerField(default=0)),
                ('f_deaths', models.IntegerField(default=0)),
                ('entries', models.IntegerField(default=0)),
                ('trades', models.IntegerField(default=0)),
                ('rounds', models.IntegerField(default=0)),
                ('rf', models.IntegerField(default=0)),
                ('ra', models.IntegerField(default=0)),
                ('damage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMatchStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds_won', models.PositiveSmallIntegerField(default=0)),
                ('rounds_lost', models.PositiveSmallIntegerField(default=0)),
                ('total_kills', models.PositiveSmallIntegerField(default=0)),
                ('total_deaths', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MatchReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('proof', models.CharField(default='no text inserted', max_length=300)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchreporting', to='matches.Match')),
                ('reported_winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winnerreporting', to='teams.Team')),
                ('reporting_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamreporting', to='teams.Team')),
                ('reporting_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userreporting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MatchDispute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('teamproof_1', models.URLField()),
                ('teamproof_2', models.URLField(blank=True)),
                ('teamproof_3', models.URLField(blank=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disputedMatch', to='matches.Match')),
                ('team1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1', to='teams.Team')),
                ('team1origreporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1OriginalReporter', to=settings.AUTH_USER_MODEL)),
                ('team2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2', to='teams.Team')),
                ('team2origreporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2OriginalReporter', to=settings.AUTH_USER_MODEL)),
                ('teamreporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1Disputer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MatchCheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_checkin', to='matches.Match')),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checkin_user', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checking_in_team', to='teams.Team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='PlatformChoice', to='matches.PlatformChoice'),
        ),
        migrations.AddField(
            model_name='match',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SportChoice', to='matches.SportChoice'),
        ),
        migrations.AddField(
            model_name='match',
            name='team1reportedwinner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1reportedwinner', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2reportedwinner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2reportedwinner', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='champions', to='teams.Team'),
        ),
        migrations.CreateModel(
            name='MapPoolChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default map pool', max_length=255)),
                ('description', models.CharField(default='No map pool description', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_pool_for', to='matches.GameChoice')),
                ('maps', models.ManyToManyField(blank=True, to='matches.MapChoice')),
            ],
        ),
    ]
