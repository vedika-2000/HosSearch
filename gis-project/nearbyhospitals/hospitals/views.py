from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from geopy.geocoders import Nominatim
import time
from .models import Hospital

app = Nominatim(user_agent="gis=project")
def get_location_by_address(address):
    """This function returns a location as raw from an address
    will repeat until success"""
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)


address = "Andheri, Mumbai, Maharashtra, India"
location = get_location_by_address(address)
latitude = float(location["lat"])
longitude = float(location["lon"])



# latitude = 19.0760
# longitude = 72.8777
user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Hospital
    context_object_name = 'hospitals'
    queryset = Hospital.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:12]
    template_name = 'hospitals/index.html'

home = Home.as_view()
