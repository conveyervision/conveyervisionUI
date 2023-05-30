from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import FoodItem
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'cv/home.html')

def login(request):
    return render(request, 'cv/login.html')

@login_required(login_url="/login/")
def dashboard(request):
    item = FoodItem.objects.first()  # gets the first FoodItem
    context = {
        'fooditem': item,
    }
    return render(request, 'cv/dashboard.html', context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'cv/home.html')

def auth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
                auth_login(request, user)
        # Redirect to a success page.
                return redirect(dashboard)
    else:
                # Return an 'invalid login' error message.
                return redirect(login)
