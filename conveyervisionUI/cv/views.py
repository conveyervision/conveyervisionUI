from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cv.models import CVSpots, CVConfig, FoodItem
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from cv.forms import Config
from django.http import HttpResponseRedirect
import datetime
import logging
#from rest_framework import viewsets
from rest_framework import generics
from .serializers import CVSpotsSerializer, CVConfigSerializer, FoodItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from cv.api import CvSpotsList, CvSpotsDetail

#logger = logging.getLogger(__name__)

def home(request):
    completed_check = CVConfig.objects.first() # gets the first config
    home_display_msg = 'This system has not yet been configured. It needs to be configured for use.'
    if completed_check.completed == True:
        spot_count = CVSpots.objects.count()
        home_display_msg = 'This system has been configured with ' + str(spot_count) + ' conveyer spots.'
    context = { 'home_display_msg': home_display_msg, }
    return render(request, 'cv/home.html', context)

def login(request):
    return render(request, 'cv/login.html')

@login_required(login_url="/login/")
def dashboard(request):
    completed = CVConfig.objects.first() # gets the first config
    config_msg = ''
    if not completed.completed == True:
        config_msg = '<a href="/config/" class="button special big">YOU NEED TO CONFIGURE YOUR SYSTEM! PLEASE CLICK HERE!</a>'
    item = CVSpots.objects.exclude(added__isnull=True).order_by('-added')  # Grabbing most recently added CVSpots objects
    if not item: # Handles if system is not yet configured
        added_delta = 0
    elif item[1].active == True:
        added_delta = item[0].added - item[1].added
    else:
        added_delta = 0
    context = {
#        'CVSpots': item,
        'added_delta': added_delta,
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
            CVSpots.objects.all().delete()
            i = 0
            this_CVSpots = []
            while i < num_spots:
                this_CVSpots.append(CVSpots(location=i))
                i += 1
            for x in this_CVSpots:
                x.active = False # Default cvspots.active to False for new (or reset) configurations
                x.save()
            logger.info('['+str(datetime.datetime.now())+' UTC] Application configuration updated successfully.')
            return HttpResponseRedirect("/dashboard/")
    else:
        existing_config = CVConfig.objects.latest('id') # gets the latest config
        return render(request, 'cv/config.html', {'form': Config(),'num_spots': existing_config.num_spots})

#class CVSpotsViewSet(viewsets.ModelViewSet):
#    queryset = CVSpots.objects.all()
#    serializer_class = CVSpotsSerializer
#
#class CVConfigViewSet(viewsets.ModelViewSet):
#    queryset = CVConfig.objects.all()
#    serializer_class = CVConfigSerializer
#
#class FoodItemViewSet(viewsets.ModelViewSet):
#    queryset = FoodItem.objects.all()
#    serializer_class = FoodItemSerializer

#class CvSpotsList(generics.ListCreateAPIView):
#    queryset = CVSpots.objects.all()
#    serializer_class = CVSpotsSerializer

