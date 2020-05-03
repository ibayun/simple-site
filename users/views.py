from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from users.forms import RegistrationForm
from users.models import User


def login_view(request):
    last_page = request.GET.get('u')
    if request.method == 'GET':
        return render(request, "login.html", context={
            "error": False,
            "u": last_page,
        })

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        last_page = request.POST.get('u')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('%s' %last_page if last_page != "None" else "/")
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                pass
            return render(request, "login.html", context={
                "error": True
            })


def logout_view(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "register.html", context={
        "forms": form
    })