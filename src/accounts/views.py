# coding=utf-8

"""
    eCommerce - A Python Dating Website
    Copyright (C) 2018-2019 nbeny
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

from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail


def guest_register_page(request):
    login_form = GuestForm(request.POST or None)
    context = {
        'form': login_form,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/cart/checkout/')
    return redirect('/cart/checkout/')


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'form': login_form,
    }
    # print('User logged in')
    # print(request.user.is_authenticated())
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if login_form.is_valid():
        # print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            # print(request.user.is_authenticated())
            # A backend authenticated the credentials
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            # context['form'] = login_form()
            else:
                return redirect('/')
        else:
            # No backend authenticated the credentials
            print('Error')

    return render(request, 'accounts/login.html', context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        'form': register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'accounts/register.html', context)


# def logout_page(request):
#     logout(request)
#     # Redirect to a success page.
#     return redirect('/')
