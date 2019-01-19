from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginFrom, RegisterForm


def home_page(request):
    context = {
        "title":"Hello World!",
        "content":"Welcome to the home page.",
        "premium_content":"YEAHHHH, your authenticated :D"
    }
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


def login_page(request):
    login_form = LoginFrom(request.POST or None)
    context = {
        'form': login_form,
    }
    print('User logged in')
    # print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # print(request.user.is_authenticated())
            # A backend authenticated the credentials
            login(request, user)
            # context['form'] = login_form()
            return redirect('/')
        else:
            # No backend authenticated the credentials
            print('Error')

    return render(request, 'auth/login.html', context)


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
    return render(request, 'auth/register.html', context)


def logout_page(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')
