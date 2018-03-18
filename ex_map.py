import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data["LON"])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<= elevation<3000:
        return 'orange'
    elif elevation>3000:
        return 'red'

map = folium.Map(location=[36.081673, 115.872456], tiles="Mapbox Bright")
#NOw add objects to the map
fgv = folium.FeatureGroup(name = 'Volcanoes')             #new feature group added with will include a set of features
fgp = folium.FeatureGroup(name='Population')
for la,lo,el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[la,lo], popup=str(el)+" m" ,icon=folium.Icon(color=color_producer(el)))) #one of the which is Marker
    map.add_child(fgv)
fgp.add_child(folium.GeoJson(data = open('world.json', encoding = 'utf-8-sig').read(),                  #polygons are added i.e. country boundaries formed yellow colored polygons
style_function = lambda x: {'fillColor' : 'green' if
                            x[ 'properties' ]['POP2005']  < 10000000 else
                            'orange' if
                            10000000<= x['properties']['POP2005'] < 20000000 else
                             'red'}))                                                            #lambda function to give yelloe color to the polygons

map.add_child(fgp)    #now this feature group is added to the map
map.add_child(folium.LayerControl())   #This is a layer control
map.save("Map2.html")
