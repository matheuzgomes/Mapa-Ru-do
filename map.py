import folium
import requests
import urllib.parse
import pandas as pd


df = pd.DataFrame(columns=['Rua', 'Bairro', 'Estado'])

for _ in range(2):
    ra = input('Qual a rua: ')
    ba = input('Agora o Bairro: ')
    es = input('E o estado: ')
    df1 = pd.DataFrame(data=[[ra,ba,es]], columns=['Rua', 'Bairro', 'Estado'])
    df = pd.concat([df,df1], axis=0)

my_map = folium.Map()

for label, row in df.iterrows():
    rua = row['Rua']
    bairro = row['Bairro']
    teste = [rua,bairro]
    print(teste)
    teste_str = str(teste)
    print(teste_str)
    # address = input("Endereço: ")
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(teste_str) +'?format=json'

    response = requests.get(url).json()
    lat = response[0]['lat']
    lon = response[0]['lon']

    folium.Marker([lat, lon]).add_to(my_map)

my_map.location = [lat, lon]
my_map.options['zoom'] = 12

    # folium.CircleMarker(
    #     radius = 50,
    #     location=[lat, lon],
    #     popup= 'Barulho pra caralho',
    #     color = "#3186cc",
    #     fill = True,
    #     fill_color = 'red'
    # ).add_to(my_map1)

# value = input("Qual o tipo de barulho se encontra nesta área: ")



my_map.save('my_map1.html')