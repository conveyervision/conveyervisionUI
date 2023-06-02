from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cv.models import CVSpots, CVConfig
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from cv.forms import Config
from django.http import HttpResponseRedirect
import datetime
import logging
#from pytz import timezone
#tz = timezone('EST')
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'cv/home.html')

def login(request):
    return render(request, 'cv/login.html')

@login_required(login_url="/login/")
def dashboard(request):
    completed = CVConfig.objects.first() # gets the first config
    config_msg = ''
    if not completed.completed == True:
        config_msg = '<a href="/config/" class="button special big">YOU NEED TO CONFIGURE YOUR SYSTEM! PLEASE CLICK HERE!</a>'
    item = CVSpots.objects.first()  # gets the item in the first spot
    context = {
        'CVSpots': item,
        'config_msg': config_msg,
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
        logger.info('['+str(datetime.datetime.now())+' UTC] User "'+username+'" logged in successfully.')
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
            this_config.completed = True
            this_config.save()
            logger.info('['+str(datetime.datetime.now())+' UTC] Application configuration updated successfully.')
            return HttpResponseRedirect("/dashboard/")
    else:
        existing_config = CVConfig.objects.first() # gets the first config
        return render(request, 'cv/config.html', {'form': Config(),'num_spots': existing_config.num_spots})
