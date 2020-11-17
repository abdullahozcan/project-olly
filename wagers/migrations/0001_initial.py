# Generated by Django 2.2.15 on 2020-11-17 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WagerChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(default='No additional info given')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('confirm', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_user', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_team', to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='WagerMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.PositiveIntegerField(default=5)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_obj', to='matches.Match')),
            ],
        ),
        migrations.CreateModel(
            name='WagerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('challenge_accepted', models.BooleanField(default=False)),
                ('expiration', models.DateTimeField(null=True)),
                ('expired', models.BooleanField(default=False)),
                ('credits', models.PositiveIntegerField(default=5)),
                ('bestof', models.SmallIntegerField(choices=[(0, 'Best of 1'), (1, 'Best of 3'), (2, 'Best of 5'), (3, 'Best of 7'), (4, 'Best of 9')], default=0)),
                ('teamformat', models.SmallIntegerField(choices=[(0, '1v1'), (1, '2v2'), (2, '3v3'), (3, '4v4'), (4, '5v5'), (5, '6v6')], default=1)),
                ('info', models.TextField(default='No additional info given')),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wager_challenge', to='wagers.WagerChallenge')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_user', to=settings.AUTH_USER_MODEL)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_choices', to='matches.GameChoice')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='platform_choices', to='matches.PlatformChoice')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_team', to='teams.Team')),
                ('wmatch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wmatch', to='wagers.WagerMatch')),
            ],
        ),
    ]
