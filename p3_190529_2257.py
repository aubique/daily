#!/usr/bin/env python3
#p3_190529_2257.py
# Molchanov courses. Lesson 2
# Parsing wordpress.org and export the output as CSV

import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://wordpress.org/plugins/'

def get_html(url):
    r = requests.get(url)
    return r.text

def refined(s): # 26,682 total ratings
    """Normalize numeric data to the unified-format without any commas"""
    ra = s.split(' ')[0] # 26,682
    return ra.replace(',', '') # 26682

def write_csv(*data):
    """Save the given dictionary as CSV-file"""
    with open('files/p3_190529_2257.csv', 'a') as f:
        writer = csv.writer(f)
        # No more than a sinle argument for writerow()
        for item in data:
            writer.writerow( (item['name'],
                              item['url'],
                              item['reviews']) )

def get_data(html):
    """Return a dictionary of popular plugins data"""
    ldata = list()
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')
    for plug_in in plugins:
        name = plug_in.find('h2').text
        url = plug_in.find('h2').find('a').get('href')
        ra = plug_in.find('span', class_='rating-count').find('a').text
        rating = refined(ra)
        data = {'name'   : name,
                'url'    : url,
                'reviews': rating}
        ldata.append(data)
    return tuple(ldata)

def main():
    # Extract tuple and sent it as multiple args to write_csv
    write_csv(*get_data(get_html(URL)))

if __name__ == '__main__':
    main()
