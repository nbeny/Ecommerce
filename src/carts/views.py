from django.shortcuts import render


def cart_home(request):
    print(request.session) # on the request
    print(dir(request.session))
    return render(request, 'carts/home.html', {})
