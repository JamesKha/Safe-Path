import streamlit as st
from streamlit_folium import st_folium
import folium
import requests
import json
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
    print(nominatim_url_request)
    response = requests.get(nominatim_url_request)

    return response.json()


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

    print(direction_request_url)

else:
    st.write('Click the button')

mapView = folium.Map(location=[40.7831, -73.9712], zoom_start=12.6)

st_data = st_folium(mapView, width=725)