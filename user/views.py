from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Petowner
from . forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from pet.models import Pet,Petowner
# Create your views here.
#kayıt ol
def register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        tel = form.cleaned_data.get("tel")
        address = form.cleaned_data.get("address")
        user.set_password(password)
        user.save()
        Petowner.objects.create(user=user, tel=tel, address=address)
        login(request, user)
        messages.info(request, "Your account has been created successfully")
        return redirect("homepage")
    return render(request, "register.html", {"form":form})

#giriş yap
def loginUser(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=(authenticate(username=username, password=password))
        if user is None:
            messages.info(request, "Not found...")
            return render(request, "login.html", {"form":form})
        login(request,user)
        messages.info(request, "You logged successfully")
        return redirect("homepage")
    return render(request, "login.html", {"form":form})

#çıkış yap
def logoutUser(request):
    logout(request)
    return redirect("homepage")

def petowner(request, username):
    user = get_object_or_404(User, username=username)
    pets = Pet.objects.filter(petowner=request.user)
    return render(request, "petowner.html", {"user":user, "pets":pets})
