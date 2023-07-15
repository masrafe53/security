from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, FavoriteNumberForm
from .models import CustomUser




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if not user.favorite_number:
                    return redirect('enter_favorite')
                else:
                    return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})





@login_required
def enter_favorite(request):
    user = request.user
    if request.method == 'POST':
        form = FavoriteNumberForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FavoriteNumberForm(instance=user)
    return render(request, 'enter_favorite.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')
