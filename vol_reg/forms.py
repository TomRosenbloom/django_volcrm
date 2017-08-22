from django import forms
from backend.models import Profile, Activity

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from localflavor.gb.forms import GBPostcodeField

class ProfileForm(forms.ModelForm):
    postcode = GBPostcodeField()
    activitys = forms.ModelMultipleChoiceField(queryset=Activity.objects.all(),label='Activities')

    class Meta:
        model = Profile
        fields = ('postcode','range','skills','activitys')
        labels = { 'range': 'Travel range'}


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', )
