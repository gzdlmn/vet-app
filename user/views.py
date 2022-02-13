from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import Petowner,Meeting
from . forms import RegisterForm,LoginForm,MeetingForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from pet.models import Pet
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import date
# Create your views here.
#register
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

#login
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

#logout
def logoutUser(request):
    logout(request)
    return redirect("homepage")

#username page
#if the user is not logged in, when user writes this address to the browser, user see login page.(decorator's goal)
#if the user wants to go an another user page, you will see forbidden page
@login_required(login_url="user:login")
def petowner(request, username):
    list_hours = ["9","10","11","12","13","14","15","16","17","18","19","20"]
    form = MeetingForm(request.POST or None)
    if form.is_valid():
        meeting = form.save(commit=False)
        meeting.user = request.user
        meeting.save()
        messages.success(request, "Your appointment date has been created")
        return redirect("homepage")
    user = get_object_or_404(User, username=username)
    pets = Pet.objects.filter(petowner=request.user)
    pets_count = Pet.objects.filter(petowner=request.user).count()
    petowner = get_object_or_404(Petowner, user=user)
    if request.user.username == petowner.user.username:
        return render(request, "petowner.html", {"user":user, "pets":pets, "petowner":petowner, "form":form, "list_hours":list_hours, "pets_count":pets_count})
    elif request.user.username != petowner.user.username:
        return HttpResponseForbidden()

def meeting(request):
    today = date.today()
    meetings = Meeting.objects.all()
    return render(request, "appointments.html", {"meetings":meetings, "today":today})