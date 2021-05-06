from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class CreateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    tos = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'profile_picture',
            'about_me',
            'alternate_name',
            'xbl',
            'psn',
            'steam',
            'steamid64',
            'discord',
            'epic',
            'lol',
            'battlenet',
            'activisionid',
            'twitter_profile',
            'twitch_channel',
            'favorite_game',
            'favorite_console',
            'country',
            'email_enabled',
            'feat_team'
        )

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['feat_team'].queryset = self.instance.founder_teams.all() | self.instance.captain_teams.all() | self.instance.player_teams.all()


class SortForm(forms.Form):  # to be improved
    sort_xp_asc = forms.BooleanField(required=False)
    sort_xp_desc = forms.BooleanField(required=False)
    sort_trophies_asc = forms.BooleanField(required=False)
    sort_trophies_desc = forms.BooleanField(required=False)
    sort_rank_asc = forms.BooleanField(required=False)
    sort_rank_desc = forms.BooleanField(required=False)
