from django.shortcuts import render,redirect,get_object_or_404
from .models import Pet
from .forms import PetForm,SearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Q
from user.models import Petowner


# Create your views here.

#Tüm hayvanları ve hayvan sahiplerini göreceği sayfa
#Yetki sadece giriş yapmış superuser için. Onun dışındakiler page not found 404 hatası alır
#(Bu sayfa normal kullanıcılar için navbarda gösterilmez. Yine de arama çubuğuna yazıp gitmek isterse hata alır)
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

#Kullanıcı kayıt olduktan sonra hayvanını eklemek için buraya yönlenir
def add_pet(request):
    form = PetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.petowner = request.user
        pet.save()
        messages.success(request, "Can dostumuz kliniğimize kaydedildi")
        return redirect("homepage")
    return render(request, "addpet.html", {"form":form})

#id ye ihtiyacım var güncellemek ve silmek için. Çünkü hayvan sahibinin birden fazla hayvanı olabilir.
#filter orm yerine get_object_404 kullanıldı
def detail(request,id):
    pet = get_object_or_404(Pet, id=id)
    return render(request, "detail.html", {"pet":pet})

#Güncelleme
def update(request, id):
    pet = get_object_or_404(Pet, id=id)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save(commit=False)
        pet.save()
        return redirect("pet:pets")
    return render(request, "update.html", {"form":form})
#Silme
def delete(request, id):
    pet = get_object_or_404(Pet, id=id)
    pet.delete()
    return redirect("pet:pets")
