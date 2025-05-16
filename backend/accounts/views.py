from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                phone=request.POST['phone'],
                address=request.POST['address']
            )
            # Redirect to the index page
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, 'index.html')
