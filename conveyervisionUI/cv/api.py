from rest_framework import generics
from cv.models import CVSpots, CVConfig, FoodItem
from .serializers import CVSpotsSerializer, CVConfigSerializer, FoodItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.http import HttpResponseRedirect
import datetime
import logging

class CvSpotsList(generics.ListCreateAPIView):
    queryset = CVSpots.objects.all()
    serializer_class = CVSpotsSerializer

logger = logging.getLogger(__name__)

# Example curl command to test POST endpoints (fill in the appropriate IP address for your environment):
# curl -H "Content-Type: application/json" -d "{\"action\": \"activate\"}" http://ip_address:8000/api/cvspots/15/
@api_view(['GET', 'POST'])
def CvSpotsDetail(request, pk):
    this_cvspot = CVSpots.objects.get(pk=pk)
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        action = json_data['action']
        if action == "activate": # Expected JSON payload: {"action": "activate"}
            this_cvspot.active = True
            this_cvspot.added = datetime.datetime.now()
            this_cvspot.save()
            logger.info('['+str(datetime.datetime.now())+' UTC] Conveyer spot '+str(this_cvspot.id)+' activated.')
            return Response({"message": "API request received - activate cvspots "+str(this_cvspot.id)+"."})
        elif action == "deactivate": # Expected JSON payload: {"action": "deactivate"}
            this_cvspot.active = False
            this_cvspot.save()
            logger.info('['+str(datetime.datetime.now())+' UTC] Conveyer spot '+str(this_cvspot.id)+' deactivated.')
            return Response({"message": "API request received - deactivate cvspots "+str(this_cvspot.id)+"."})
        elif action == "update":
            if json_data['type'] == 'food':
                this_cvspot.food = json_data['value'] # Expected JSON payload: {"action": "update", "type": "food", "value":"Salmon Sushi Secial"}
                this_cvspot.save()
                logger.info('['+str(datetime.datetime.now())+' UTC] Conveyer spot '+str(this_cvspot.id)+' food value updated to be \''+json_data['value']+'\'.')
                return Response({"message": "API request received - update cvspots "+str(this_cvspot.id)+" food value \""+json_data['value']+"\"."})
            elif json_data['type'] == 'location':
                this_cvspot.location = json_data['value'] # Expected JSON payload: {"action": "update", "type": "location", "value":"8"}
                this_cvspot.location_update = datetime.datetime.now()
                this_cvspot.save()
                logger.info('['+str(datetime.datetime.now())+' UTC] Conveyer spot '+str(this_cvspot.id)+' location value updated to be \''+json_data['value']+'\'.')
                return Response({"message": "API request received - update cvspots "+str(this_cvspot.id)+" location value \""+str(json_data['value'])+"\"."})
            else:
                logger.info('['+str(datetime.datetime.now())+' UTC] API error - Unexpected POST data.')
                return Response({"message": "API error - Unexpected POST data."})
        else:
            logger.info('['+str(datetime.datetime.now())+' UTC] API error - Unexpected POST data.')
            return Response({"message": "API error - Unexpected POST data."})
    else:
        logger.info('['+str(datetime.datetime.now())+' UTC] Served API GET request for CVSpots.id '+str(this_cvspot.id)+'.')
        return Response({"id": this_cvspot.id,
            "active": this_cvspot.active,
            "food": this_cvspot.food,
            "location": this_cvspot.location,
            "added": this_cvspot.added,
            "location_update": this_cvspot.location_update})
