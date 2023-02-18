import streamlit as st
from streamlit_folium import st_folium
import folium
import requests
import json
import geopandas as gpd
import matplotlib.pyplot as plt
from areasToAvoid import getAreasToAvoid
class coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return "".join(["[", str(self.lat), ",", str(self.lon), "]"])

#example addresses
#10 Rockefeller Plaza, New York, NY 10020
#20 W 34th St., New York, NY 10001

openRouteServiceAPIKey = "5b3ce3597851110001cf6248a39d88d90cfd44289c2256b4181024f1"
openStreetMapAPIURL= "https://api.openstreetmap.org/"
nominatimAPIURL = "https://nominatim.openstreetmap.org/search?q="

def getAddressJSON(address):
    search_friendly_address = address.replace(" ", "+")
    search_friendly_address = search_friendly_address.replace(',', '')
    nominatim_url_request = ''.join([nominatimAPIURL, search_friendly_address, "&format=json&polygon=1&addressdetails=1"])
    #print(nominatim_url_request)
    response = requests.get(nominatim_url_request)
    return response.json()

def getReadableInstructions(steps):
    readableInstructions = []
    for step in steps:
        readableInstructions.append(step["instruction"])
    return readableInstructions

def parseWaypointsInRoute(waypoints):
    coordinatesList = []
    for waypoint in waypoints:
        cuCoordinate = coordinate(0, 0)
        #openrouteservice has their coordinates lon,lat while openstreetmap has their coordinates lat,lon
        cuCoordinate.lat, cuCoordinate.lon = waypoint[1], waypoint[0]
        coordinatesList.append(cuCoordinate)
    return coordinatesList

def getDirectionsJSON(urlRequest):
    response = requests.get(urlRequest)
    jsonRes = response.json()
    steps = jsonRes["features"][0]["properties"]["segments"][0]["steps"]
    readableInstructions = getReadableInstructions(steps)
    rawWaypoints = jsonRes["features"][0]["geometry"]["coordinates"]
    coordinatesInRoute = parseWaypointsInRoute(rawWaypoints)

    for instruction in readableInstructions:
        st.write(instruction)

startingLocation = st.text_input('Starting Location', '')
endLocation = st.text_input('Destination', '')

if st.button('Calculate Route'):

    startAddressJSON = getAddressJSON(startingLocation)
    
    start_lat = startAddressJSON[0]["lat"]
    start_lon = startAddressJSON[0]["lon"]
    
    endAddressJSON = getAddressJSON(endLocation)

    end_lat = endAddressJSON[0]["lat"]
    end_lon = endAddressJSON[0]["lon"]

    direction_request_url = ''.join(["https://api.openrouteservice.org/v2/directions/driving-car?api_key=", openRouteServiceAPIKey, "&start=", start_lon, ",", start_lat, "&end=", end_lon, ",", end_lat]);
    getDirectionsJSON(direction_request_url)
else:
    st.write('Click the button')


mapView = folium.Map(location=[40.7831, -73.9712], zoom_start=12.6, tiles='cartodbpositron')
polygons = getAreasToAvoid()
for polygon in polygons:
    folium.GeoJson(polygon).add_to(mapView)
folium.LatLngPopup().add_to(mapView)
st_data = st_folium(mapView, width=725)