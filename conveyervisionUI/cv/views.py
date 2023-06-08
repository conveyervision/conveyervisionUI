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
            CVSpots.objects.all().delete()
            i = 0
            this_CVSpots = []
            while i < num_spots:
                this_CVSpots.append(CVSpots(location=i))
                i += 1
            for x in this_CVSpots:
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

class CvSpotsList(generics.ListCreateAPIView):
    queryset = CVSpots.objects.all()
    serializer_class = CVSpotsSerializer

# Example curl command to test POST endpoints (fill in the appropriate IP address for your environment):
# curl -H "Content-Type: application/json" -d "{\"action\": \"deactivate\"}" http://ip_address:8000/api/cvspots/15/
@api_view(['GET', 'POST'])
def CvSpotsDetail(request, pk):
    this_cvspot = CVSpots.objects.get(pk=pk)
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        action = json_data['action']
        if action == "activate":
            this_cvspot.active = True
            this_cvspot.save()
            logger.info('['+str(datetime.datetime.now())+' UTC] Conveyer spot '+str(this_cvspot.id)+' activated successfully.')
            return Response({"message": "API request received - activate cvspots "+str(this_cvspot.id)+"."})
        elif action == "deactivate":
            this_cvspot.active = False
            this_cvspot.save()
            logger.info('['+str(datetime.datetime.now())+' UTC] Conveyer spot '+str(this_cvspot.id)+' deactivated successfully.')
            return Response({"message": "API request received - deactivate cvspots "+str(this_cvspot.id)+"."})
        else:
            logger.info('['+str(datetime.datetime.now())+' UTC] API error - Unexpected POST data.')
            return Response({"message": "API error - Unexpected POST data."})
    else:
        return Response({"message": "Did you forget POSTage?"})
