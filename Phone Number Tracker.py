import phonenumbers
#import folium
from phonenumbers import geocoder
from phonenumbers import carrier 
#import webbrowser

num = "+919461762700"
tag_num = phonenumbers.parse(num)
#89615 59528
#88751 12227
#94617 62700

#key = '6c88f3edf15448a582a99183d722c39c'
#chromedir ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
yourLocation = geocoder.description_for_number(tag_num, 'en')

#Nationality of the number
ch_nmber = phonenumbers.parse(num, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

#Service provider of the number
service_nmber = phonenumbers.parse(num, "RO")
print(carrier.name_for_number(service_nmber, "en"))

#from opencage.geocoder import OpenCageGeocode

#geocoder = OpenCageGeocode(key)
#query = str(yourLocation)
#geocode_result = geocoder.geocode(query)
#print(geocode_result)

#geom = geocode_result[0]
#loc = geom['location']
#lat = geom['lat']
#lng = geom['lng']

#print(lat,lng)

#myMap = folium.Map(Location=[lat,lng], zoom_start = 9)
#folium.Marker([lat ,lng], popup= yourLocation).add_to((myMap))

#webbrowser.get(chromedir).open("https://www.google.nl/maps/place/" + yourLocation)
