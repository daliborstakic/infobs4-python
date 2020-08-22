from bs4 import BeautifulSoup
from collections import Counter
import requests
import csv

# Page source 
source = requests.get('http://www.informer.rs/vesti').text

# Soup parser
soup = BeautifulSoup(source, 'lxml')

# Getting the text from h2 and h5 tags
header_text = soup.find_all(['h5'])

# Empty data
data = []

# Appending every text
for header in header_text:
    try:
        text = header.a.string.lower().split(' ')
        data += text
    except:
        pass

# Using Counter object to represent the data
counted_data = Counter(data)

# CSV File
with open('infodata.csv', 'w', encoding='utf-8', newline='\n') as csv_file:
    writer = csv.writer(csv_file)

    # Writing rows
    for item in counted_data.most_common(30):
        writer.writerow([item[0], item[1]])
