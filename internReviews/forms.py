from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_tamu_email_address(email):
    if not email.endswith('tamu.edu'):
        raise ValidationError(
            "Please use Texas A&M University email address for Signup")


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField(validators=[validate_tamu_email_address])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
