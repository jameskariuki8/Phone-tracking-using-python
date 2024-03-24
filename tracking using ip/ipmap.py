import geocoder 
import folium
g = geocoder.ip('me')
myaddress = g.latlng
print(myaddress)
#print(myaddress)
myMap_1 = folium.Map(location=myaddress, zoom_start= 12)
folium.CircleMarker(location=myaddress, radius=50, popup="yorkshire").add_to(myMap_1)
folium.Marker(myaddress, popup='yorkshire').add_to(myMap_1)

myMap_1.save('mymap1.html')