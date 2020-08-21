from bs4 import BeautifulSoup
import requests

# Page source 
source = requests.get('http://www.informer.rs')

# Soup parser
soup = BeautifulSoup(source, 'lxml')
