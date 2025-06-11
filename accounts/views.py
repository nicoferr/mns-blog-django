from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .ban import validate_address

# Create your views here.
def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        address_validation = validate_address(form.data.get('address'))

        if not address_validation['valid']:
            messages.error(request, 'Adresse invalide. Vérifier votre adresse')
            return redirect('register')

        if form.is_valid():
            user = form.save()
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.address = address_validation['label']
            user.profile.latitude = address_validation['latitude']
            user.profile.longitude = address_validation['longitude']
            user.profile.save()
            messages.success(request, 'Inscription réussie')
            return redirect('articles_list')
        else:
            messages.error(request, 'Erreur lors de l\'inscription, Vérifiez vos informations')
            return redirect('register')

    return render(request, 'register.html', {'form': form})

@login_required
def manage_profile(request):
    return render(request, 'manage_profile.html')