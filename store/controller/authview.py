from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from store.forms import CustomUserForm
from django.contrib import messages


def register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created succesfuly")
            return redirect("login")
    context = {"form": form}
    return render(request, "store/auth/register.html", context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("/")
    else:
        if request.method == "POST":
            name = request.POST.get("username")
            contraseña = request.POST.get("password")
            user = authenticate(request, username=name, password=contraseña)
            if user is not None:
                login(request, user)
                messages.success(request, "user already login")
                return redirect("home")
            else:
                messages.error(request, "username it's dosent exist")
                return redirect("login")
        return render(request, "store/auth/loginpage.html")


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Sesion it's expired")
    return redirect("home")
