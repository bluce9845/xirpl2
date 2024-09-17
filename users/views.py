from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.

def login_user(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
        login(request, form.get_user())
        return redirect('index')
    else:
       form = AuthenticationForm()
       
    return render(request, 'login/login_view.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('login')
    else:
        form = UserCreationForm()
            
    return render(request, 'register/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')