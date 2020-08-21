from bs4 import BeautifulSoup
import requests

# Page source 
source = requests.get('http://www.informer.rs/vesti').text

# Soup parser
soup = BeautifulSoup(source, 'lxml')

# Getting the text from h2 and h5 tags
header_text = soup.find_all(['h5'])

for header in header_text:
    try:
        print(header.a.string)
    except:
        pass

# print(header_text)

# print(link_text)

""" for header in header_text.get_all('a'):
    try:
        print(header.a['title'])
    except:
        pass """

# print(header_text)
