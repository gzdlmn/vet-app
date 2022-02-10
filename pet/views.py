from django.shortcuts import render,redirect,get_object_or_404
from .models import Pet
from .forms import PetForm,SearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Q
from user.models import Petowner


# Create your views here.

#Only logged in superuser will see this page. Normal users will see 404 not found. When project publish, this page will be a real error page.
@login_required(login_url="user:login")
@user_passes_test(lambda u: u.is_superuser)
def all_pets(request):
    form = SearchForm(request.GET or None)
    if form.is_valid():
        search = form.cleaned_data.get("search", None)
        if search:
            pets = Pet.objects.filter(Q(name__icontains=search)).distinct()
            return render(request, "pets.html", {"pets": pets, "form":form})
    pets = Pet.objects.all()
    return render(request, "pets.html", {"pets": pets, "form":form})

#User will come here after registration and then he/she will write his/her pet's attr.
def add_pet(request):
    form = PetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.petowner = request.user
        pet.save()
        messages.success(request, "Can dostumuz kliniğimize kaydedildi")
        return redirect("homepage")
    return render(request, "addpet.html", {"form":form})

#I need an id.  Because The user can have more than one animal. get_object_or_404 instead of filter
def detail(request,id):
    pet = get_object_or_404(Pet, id=id)
    return render(request, "detail.html", {"pet":pet})

#update. only superuser can see this page and edit
def update(request, id):
    pet = get_object_or_404(Pet, id=id)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save(commit=False)
        pet.save()
        return redirect("pet:pets")
    return render(request, "update.html", {"form":form})
#delete. only superuser
def delete(request, id):
    pet = get_object_or_404(Pet, id=id)
    pet.delete()
    return redirect("pet:pets")
