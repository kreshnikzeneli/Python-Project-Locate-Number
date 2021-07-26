
import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

Key = 'a628486d57a14307ab26f6b646ca454c'

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print("Phone number is: " + number)
print("Country is: " + yourLocation)


## get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print("Service Provider is: " + carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

## save map in html file

myMap.save("myLocation.html")

