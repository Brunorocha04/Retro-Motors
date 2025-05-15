
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomLoginForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}! O seu registo foi realizado com sucesso.")
            return redirect('index')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo de volta, {username}!")
                # Redireciona para a página solicitada ou para a página inicial
                next_page = request.GET.get('next', 'index')
                return redirect(next_page)
        else:
            messages.error(request, "Nome de utilizador ou password inválidos.")
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Saiu do sistema.")
    return redirect('login')

def index(request):
    return render(request, 'accounts/index.html')
