import folium
import requests
import urllib.parse

address = input("Endereço: ")
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = requests.get(url).json()
lat = response[0]['lat']
lon = response[0]['lon']

my_map1 = folium.Map(location= [lat, lon], zoom_start=12)

value = input("Qual o tipo de barulho se encontra nesta área: ")

folium.Marker([lat, lon], popup=value).add_to(my_map1)

folium.CircleMarker(
    radius = 50,
    location=[lat, lon],
    popup= 'Barulho pra caralho',
    color = "#3186cc",
    fill = True,
    fill_color = 'red'
).add_to(my_map1)

my_map1.save('my_map1.html')