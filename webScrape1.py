import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count= int(input("Enter Count: "))
position = int(input("Enter position: "))
current_repeat_count = 0

def parse_html(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while count!=0:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            break
        else:
            continue
    count -= 1
print('Last Url: ', url)
