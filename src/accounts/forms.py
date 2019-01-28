# coding=utf-8

"""
    Ecommerce - A Python Dating Website
    Copyright (C) 2018-2019 jlasne/ynacache
    <nbeny@student.42.fr>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class GuestForm(forms.Form):
    email   = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class RegisterForm(forms.Form):
    username    = forms.CharField()
    email       = forms.EmailField()
    password    = forms.CharField(widget=forms.PasswordInput)
    password2   = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('username')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email is token')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is token')
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match.')
        return data
