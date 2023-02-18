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

# example addresses
# 10 Rockefeller Plaza, New York, NY 10020
# 20 W 34th St., New York, NY 10001

# example of rerouting to avoid bad areas
# 312 W 34th St., New York, NY 10001
# 112 W 34th St., New York, NY 10120


openRouteServiceAPIKey = "5b3ce3597851110001cf6248a39d88d90cfd44289c2256b4181024f1"
openStreetMapAPIURL = "https://api.openstreetmap.org/"
nominatimAPIURL = "https://nominatim.openstreetmap.org/search?q="


def getAddressJSON(address):
    search_friendly_address = address.replace(" ", "+")
    search_friendly_address = search_friendly_address.replace(',', '')
    nominatim_url_request = ''.join(
        [nominatimAPIURL, search_friendly_address, "&format=json&polygon=1&addressdetails=1"])
    # print(nominatim_url_request)
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
        # openrouteservice has their coordinates lon,lat while openstreetmap has their coordinates lat,lon
        cuCoordinate.lat, cuCoordinate.lon = waypoint[1], waypoint[0]
        coordinatesList.append(cuCoordinate)
    return coordinatesList


def getDirectionsJSON(urlRequest, start_lat, start_lon, end_lat, end_lon):
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': openRouteServiceAPIKey,
        'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        "coordinates": [
            [start_lon, start_lat],
            [end_lon, end_lat],
        ],
        "options": {
            "avoid_polygons": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [-73.99323914300739, 40.75230617940999],
                            [-73.9907378546972, 40.75119382478945],
                            [-73.99088089928028, 40.75099943254187],
                            [-73.99340244093696, 40.75205809080204],
                            [-73.99323914300739, 40.75230617940999]
                        ],
                        [
                            [-73.87093974982044, 40.82273628803473],
                            [-73.87010229895341, 40.822811582521744],
                            [-73.87003596621149, 40.82261707158884],
                            [-73.87086512548576, 40.822504129495044],
                            [-73.87093974982044, 40.82273628803473]
                        ],
                        [
                            [-73.91989243077671, 40.83874526858156],
                            [-73.91935571709065, 40.838323892160844],
                            [-73.91947723717053, 40.838178325138465],
                            [-73.92000382418324, 40.838599702484494],
                            [-73.91989243077671, 40.83874526858156]
                        ],
                        [
                            [-73.99569892445557, 40.754102364435894],
                            [-73.99304001015363, 40.752979699450854],
                            [-73.99311265808538, 40.752825606698856],
                            [-73.9958296907327, 40.753959280736964],
                            [-73.99569892445557, 40.754102364435894]
                        ],
                        [
                            [-73.98710389540031, 40.750518513614594],
                            [-73.98422193493894, 40.74931378806984],
                            [-73.9843421512827, 40.74910562172596],
                            [-73.98715864847888, 40.75029389583511],
                            [-73.98710389540031, 40.750518513614594]
                        ],
                        [
                            [-73.84722713332482, 40.887700851471244],
                            [-73.84695659826608, 40.88760498130328],
                            [-73.84721867910423, 40.88707449719653],
                            [-73.84767520701587, 40.887010583161654],
                            [-73.84722713332482, 40.887700851471244]
                        ],
                        [
                            [-73.90038858261332, 40.85424856293518],
                            [-73.90024486086335, 40.85424856293518],
                            [-73.90079438520144, 40.85295045254363],
                            [-73.90102264915726, 40.85298242601149],
                            [-73.90038858261332, 40.85424856293518]
                        ],
                        [
                            [-73.95402190296713, 40.648808089778825],
                            [-73.9529561481669, 40.64887770482077],
                            [-73.95290563679325, 40.64871171217062],
                            [-73.95405719286119, 40.64864743940491],
                            [-73.95402190296713, 40.648808089778825]
                        ]
                    ]
                ]
            }
        }
    }
    response = requests.post(
        "https://api.openrouteservice.org/v2/directions/driving-car/geojson", headers=headers, json=data)
    jsonRes = response.json()
    #print(jsonRes)
    steps = jsonRes["features"][0]["properties"]["segments"][0]["steps"]
    readableInstructions = getReadableInstructions(steps)
    rawWaypoints = jsonRes["features"][0]["geometry"]["coordinates"]
    coordinatesInRoute = parseWaypointsInRoute(rawWaypoints)

    print('-------------------------')
    for instruction in readableInstructions:
        print(instruction)
        st.write(instruction)
    print('-------------------------')


startingLocation = st.text_input('Starting Location', '')
endLocation = st.text_input('Destination', '')

if st.button('Calculate Route'):

    startAddressJSON = getAddressJSON(startingLocation)

    start_lat = startAddressJSON[0]["lat"]
    start_lon = startAddressJSON[0]["lon"]

    endAddressJSON = getAddressJSON(endLocation)

    end_lat = endAddressJSON[0]["lat"]
    end_lon = endAddressJSON[0]["lon"]

    direction_request_url = ''.join(["https://api.openrouteservice.org/v2/directions/driving-car?api_key=",
                                    openRouteServiceAPIKey, "&start=", start_lon, ",", start_lat, "&end=", end_lon, ",", end_lat])
    getDirectionsJSON(direction_request_url, start_lat,
                      start_lon, end_lat, end_lon)


mapView = folium.Map(location=[40.7831, -73.9712],
                     zoom_start=12.6, tiles='cartodbpositron')
polygons = getAreasToAvoid()
for polygon in polygons:
    folium.GeoJson(polygon).add_to(mapView)
folium.LatLngPopup().add_to(mapView)
st_data = st_folium(mapView, width=725)
