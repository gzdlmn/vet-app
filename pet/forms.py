from django import forms
from .models import Pet

#formu modelden türetiyoruz.
#sadece siteye kayıt olmuş kullanıcı hayvanını ekleyebilir. Bu yüzden petowner göstermeye gerek yok. Kendine ait formu dolduracak.
class PetForm(forms.ModelForm):
    name = forms.CharField(label="Can Dostumuz Adı:")
    type = forms.CharField(label="Tür: köpek,kedi,kuş...")
    genius = forms.CharField(label="Cins: terrier,iran kedisi,sultan papağanı...varsa cinsi:")
    image = forms.FileField(label="Lütfen kare bir resim yükleyiniz")
    class Meta:
        model = Pet
        fields = ["image", "name", "type", "genius", "age", "explanation"]

#Bu bir modele ait değil get atan arama formu
class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))

