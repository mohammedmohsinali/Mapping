import folium
import pandas,io
data = pandas.read_csv("Volcanoes.txt");
data_json = io.open('world.json', 'r', encoding='utf-8-sig').read()
map = folium.Map(location=[38.2, -99.1], zoom_start=6, titles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'        
for i, j, k in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[i, j], radius=6, popup=k, fill_color=color_producer(k), color = 'grey', fill_opacity=0.7))

#fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'), style_function=lambda x: {'fillColor':'yellow'}))
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=data_json,style_function=lambda x: {'fillColor':'blue' if x['properties']
['POP2005'] < 10000000
else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else
'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map_1.html")

 