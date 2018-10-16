import geopy
import math
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
from difflib import get_close_matches
import requests
import unittest
from unittest.mock import patch


def get_webpage(url):
    '''given a URL, returns webpage text in html parsed form'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def getCapitals():

    soup = get_webpage(
        "https://en.wikipedia.org/wiki/List_of_national_capitals")

    table = soup.find_all("table", {
        "class": "wikitable sortable"
    })[0].tbody.find_all('tr')

    capitals = []
    for item in table:
        try:
            capitals.append(item.find_all('td')[0].text.lower())
        except IndexError:
            pass
    return capitals

def choiceFromList(list, message="Enter Selection: ", caseSensitive=False):

    while True:

        choice = input(message)

        if caseSensitive:
            if choice not in list:
                print("Did you mean one of the following? :{}".format(
                    get_close_matches(choice, list, 5, 0.7)))
            else:
                break
        else:
            if choice.lower() not in list:
                print("Did you mean one of the following? :{}".format(
                    get_close_matches(choice, list, 5, 0.7)))
            else:
                break
    print("Selection: {}".format(choice))
    return choice

def getCoords(search):
    geolocator = Nominatim(user_agent="my-application")
    location_info = geolocator.geocode(search)
    location = {
        "lat": location_info.latitude,
        "lon": location_info.longitude
    }
    return location

def haversine(lon_a, lat_a, lon_b, lat_b):

    lat_a_rad = math.radians(lat_a)
    lat_b_rad = math.radians(lat_b)
    delta_lon = lon_b - lon_a
    delta_lat = lat_b - lat_a
    delta_lon_rad = math.radians(delta_lon)
    delta_lat_rad = math.radians(delta_lat)

    R = 6371  # km
    a = (math.sin(delta_lat_rad/2) * math.sin(delta_lat_rad/2)) + \
        (math.cos(lat_a_rad) * math.cos(lat_b_rad) *
        (math.sin(delta_lon_rad/2) * (math.sin(delta_lon_rad/2))))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

def main():

    capitals = getCapitals()
    city_a = getCoords(choiceFromList(capitals, "Choose city 1: "))
    city_b = getCoords(choiceFromList(capitals, "Choose city 2: "))

    lon_a = city_a['lon']
    lat_a = city_a['lat']
    lon_b = city_b['lon']
    lat_b = city_b['lat']

    distance = haversine(lon_a, lat_a, lon_b, lat_b)
    print("The distance between the cities is: {}km".format(round(distance)))


class MyTest(unittest.TestCase):

    def test_haversine(self):
        self.assertEqual(
            round(haversine(-0.127758, 51.507351, 2.352222, 48.856613)), 344)

    def test_getCoords_lat(self):

        expected = 51.5074
        self.assertAlmostEqual(
            getCoords('London')['lat'], expected, 3)

    def test_getCoords_lon(self):

        expected = -0.1278
        self.assertAlmostEqual(
            getCoords('London')['lon'], expected, 3)

if __name__ == "__main__":
    main()
    unittest.main()
    