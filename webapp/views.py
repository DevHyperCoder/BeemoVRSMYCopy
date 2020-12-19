from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import AuthenticationForm


# Sign in route (LOGIN)
def sign_in(request):
    data = request.POST or None
    form = AuthenticationForm(data=data)

    next_location = ""
    if request.GET:
        next_location = request.GET.get('next')

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(user=user, request=request)
        if next_location != "":
            print(next_location)
            return redirect(next_location)

        return redirect('home')

    return render(request, "signin.html", {'form': form, 'next': next_location})


# Sign up route (REGISTER)
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('sign_in')

    return render(request, "register.html", {'form': form})


# Logout page
def logout(request):
    django_logout(request)
    return redirect('home')
