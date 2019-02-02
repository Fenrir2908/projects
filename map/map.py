import folium as maplib
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(elev <= elev < 3000):
        return('orange')
    else:
        return('red')

map = maplib.Map(location=[0,0], zoom_start=2, tiles='OpenStreetMap')

marker_cluster = MarkerCluster().add_to(map)

for lat, lon, elevation in zip(lat, lon, elevation):
    maplib.CircleMarker(location=[lat, lon], radius=9, popup=str(elevation)+" m",
                  fill_color=color_change(elevation),
                  color='gray', fill_opacity=0.9).add_to(marker_cluster)

map.save("map1.html")
