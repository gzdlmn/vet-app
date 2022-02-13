from django import forms
from .models import Pet

#only registered users can add their pet. The user can see this form after registering.
class PetForm(forms.ModelForm):
    name = forms.CharField(label="Your pet's name:")
    type = forms.CharField(label="Type: dog,cat,bird..etc")
    genius = forms.CharField(label="Genius: terrier,poddle,chihuahua...etc:")
    image = forms.FileField(label="Please your pet's image must be square")
    class Meta:
        model = Pet
        fields = ["image", "name", "type", "genius", "age", "explanation"]


#This form is there for searching. method = get. Model is not unnecessary. 
class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))


