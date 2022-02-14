from django import forms
from django.contrib.auth.models import User
from .models import Petowner, Meeting
# for calender
from django.forms.widgets import NumberInput

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    email = forms.CharField(label="E-mail", required=False)
    tel = forms.CharField(label="Phone", required=True)
    address = forms.CharField(label="Address", required=False)
    class Meta:
        model = User
        fields=["username", "password", "first_name", "last_name", "email", "tel", "address"]
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("This username is registered in the system. Please choose another username.")
        return username

# User can update your information. Especially tel,address
class RegisterupdateForm(forms.ModelForm):
    tel = forms.CharField(label="Phone", required=True)
    address = forms.CharField(label="Address", required=False)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "tel", "address"]

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=["username","password"]
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

# make an appointment
class MeetingForm(forms.ModelForm):
    meeting_hour = forms.ChoiceField(choices=Meeting.CHOICES, label="Appointment Hour", widget=forms.RadioSelect)
    meeting_date = forms.DateField(label="Appointment Day", widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Meeting
        fields = ["meeting_hour", "meeting_date", "pet"]

