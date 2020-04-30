from django import forms
from django.contrib.auth.hashers import make_password

from users.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
        )
        widgets = {
            "username": forms.TextInput(attrs={
                'placeholder': 'nickname',
            }),
            "email": forms.TextInput(attrs={
                'placeholder': 'mail@mail.mail',
            }),
            "password": forms.PasswordInput(attrs={
                'placeholder': 'password',
            }),
            "first_name": forms.TextInput(attrs={
                'placeholder': 'Semenov',
            }),
            "last_name": forms.TextInput(attrs={
                'placeholder': 'Anton',
            }),
        }

    def save(self, commit=True):
        password = (
            make_password(
                self.cleaned_data['password']
            )
        )
        self.instance.password = password
        self.cleaned_data['password'] = password
        return super().save(commit)
