from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from django import forms

from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


password_validation = RegexValidator(r'^.{8,}$', 'Password have minimum 8 characters')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=128, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=128, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    password1 = forms.CharField(max_length=24, required=True, widget=forms.PasswordInput(),
                                validators=([password_validation]))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']