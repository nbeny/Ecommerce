# coding=utf-8

"""
    eCommerce - A Python Dating Website
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

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


def home_page(request):
    # print(request.session.get("first_name", "Unknown")) # getter
    # request.session['first_name']
    context = {
        "title":"Hello World!",
        "content":"Welcome to the home page.",
    }
    if request.user.is_authenticated:
       context['premium_content'] = 'YEAHHHH, your authenticated :D'
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title":"About Page",
        "content":"Welcome to the about page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact Page",
        "content":"Welcome to the contact page.",
        "form": contact_form,
        # "brand": "new Brand Name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/views.html", context)
