import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts =  tree.findall('.//count')
print ("Count: " ,len(counts))

sum = 0

for count in counts:
    sum += int(count.text)

print ("Sum:" ,sum)
