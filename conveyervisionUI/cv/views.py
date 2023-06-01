from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cv.models import CVSpots, CVConfig
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from cv.forms import Config
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'cv/home.html')

def login(request):
    return render(request, 'cv/login.html')

@login_required(login_url="/login/")
def dashboard(request):
    item = CVSpots.objects.first()  # gets the item in the first spot
    context = {
        'CVSpots': item,
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

@login_required(login_url="/login/")
def config(request):
    if request.method == "POST":
        form = Config(request.POST)
        if form.is_valid():
            # PROCESS FORM DATA HERE
            num_spots = form.cleaned_data['num_spots']
            this_config = CVConfig.objects.all()[0]
            this_config.num_spots = num_spots
            this_config.save()
            return HttpResponseRedirect("/dashboard/")
    return render(request, 'cv/config.html', {'form': Config()})
