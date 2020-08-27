from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Register user
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login user
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
