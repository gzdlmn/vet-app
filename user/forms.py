from django import forms
from django.contrib.auth.models import User
from .models import Petowner


class RegisterForm(forms.ModelForm):
    username=forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'myclass'}))
    first_name = forms.CharField(label="Ad", required=True)
    last_name = forms.CharField(label="Soyad", required=True)
    email = forms.CharField(label="E-mail", required=False)
    tel = forms.CharField(label="Telefon", required=True)
    address = forms.CharField(label="Adres", required=False)
    class Meta:
        model=User
        fields=["username","password", "first_name", "last_name", "email", "tel", "address"]
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Bu kullanıcı adı sistemde kayıtlı.Lütfen başka bir kullanıcı adı seçiniz.")
        return username

class LoginForm(forms.Form):
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'myclass'}))
    class Meta:
        model=User
        fields=["username","password"]
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
