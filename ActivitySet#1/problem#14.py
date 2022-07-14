# Using Web Services
# https://www.py4e.com/lessons/servces
#1 st program
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
    sum = tree.findall('contents')
    sum+=sum
print(sum)

#Json
import json
import urllib.request, urllib.parse, urllib.error
sum = 0
fhand = urllib.request.uropen('http://py4e-data.dr-chuck.net/comments_42.json')
info = json.loads(fhand)
print('User count:', len(info))
for item in info:
    sum = info.
    sum+=sum
print(sum)

import urllib.request, json

address = input('Enter location: ')
print('Retrieving', address)
with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

print('Retrieved', len(str(raw)), 'characters')
data = raw.get("comments")
#print(data)
num = total = 0
for i in range(len(data)):
    tmp = data[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)

import urllib.request, json

address = input('Enter location: ')
print('Retrieving', address)
with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

print('Retrieved', len(str(raw)), 'characters')
data = raw.get("comments")
num = total = 0
for i in range(len(data)):
    tmp = data[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)


import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Ages(
             name VARCHAR(128),
             age INTEGER
             )"""
         )
def add_people(sName, iAge):
    with conn:
        c.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':sName, 'age':iAge})
    