from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Votre adresse e-mail")
    phone = forms.CharField(max_length=15, required=False, label='Téléphone')
    address = forms.CharField(max_length=255, required=False, label='Adresse', widget=forms.Textarea({
        'rows': '3',
        'placeholder': 'Adresse (Optionnel)'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'address')