# Generated by Django 2.2.12 on 2020-05-16 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matches', '0022_auto_20200410_1506'),
        ('teams', '0008_team_image'),
        ('singletournaments', '0021_auto_20200420_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='League Ruleset', max_length=50)),
                ('ot_losses', models.BooleanField(default=True)),
                ('pts_ot_loss', models.PositiveSmallIntegerField(default=1)),
                ('ot_wins', models.BooleanField(default=False)),
                ('pts_ot_win', models.PositiveSmallIntegerField(default=3)),
                ('pts_win', models.PositiveSmallIntegerField(default=3)),
                ('pts_loss', models.PositiveSmallIntegerField(default=0)),
                ('allow_tie', models.BooleanField(default=False)),
                ('num_games', models.PositiveIntegerField(default=10)),
                ('auto_schedule', models.BooleanField(default=False)),
                ('record_format', models.CharField(choices=[(1, 'W-L-OTL'), (2, 'W-L-T'), (3, 'W-L-OTW-OTL'), (4, 'W-L-OTW-OTL-OTT'), (5, 'W-L')], default='W-L-OTL', max_length=20)),
                ('num_divisons', models.PositiveSmallIntegerField(default=2)),
                ('max_division_size', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('losses', models.PositiveSmallIntegerField(default=0)),
                ('ot_losses', models.PositiveSmallIntegerField(default=0)),
                ('ot_wins', models.PositiveSmallIntegerField(default=0)),
                ('ties', models.PositiveSmallIntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='league_team', to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='LeagueDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('games', models.ManyToManyField(blank=True, to='matches.Match')),
                ('teams', models.ManyToManyField(blank=True, to='leagues.LeagueTeam')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='League Name', max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('info', models.TextField(default='No information provided')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='league_images')),
                ('teamformat', models.SmallIntegerField(choices=[(0, '1v1'), (1, '2v2'), (2, '3v3'), (3, '4v4'), (4, '5v5'), (5, '6v6')], default=1)),
                ('bestof', models.SmallIntegerField(choices=[(0, 'Best of 1'), (1, 'Best of 3'), (2, 'Best of 5'), (3, 'Best of 7'), (4, 'Best of 9')], default=0)),
                ('allow_register', models.BooleanField(default=False)),
                ('open_register', models.DateTimeField()),
                ('close_register', models.DateTimeField()),
                ('start', models.DateTimeField()),
                ('divisions', models.ManyToManyField(blank=True, to='leagues.LeagueDivision')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='league_game', to='matches.GameChoice')),
                ('platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='league_platform', to='matches.PlatformChoice')),
                ('ruleset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='league_ruleset', to='singletournaments.SingleTournamentRuleset')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='league_settings', to='leagues.LeagueSettings')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='league_sport', to='matches.SportChoice')),
            ],
        ),
    ]