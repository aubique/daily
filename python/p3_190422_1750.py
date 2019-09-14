#!/usr/bin/env python3
#p3_190422_1750.py
# Parsing Avito. Part 1

import requests
from bs4 import BeautifulSoup
from bs4 import element
import csv

URL = 'https://www.avito.ru/rossiya/telefony?p=1&q=htc'
DOMAIN = 'https://www.avito.ru'
CSV_FILE = 'files/p3_190422_1750.csv'

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all(
        'a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)

def write_csv(data: dict):
    with open(CSV_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow( (data['title'],
                          data['price'],
                          data['location'],
                          data['url']
                         ) )

def write_csvs(data: list):
    for data_dict in data:
        write_csv(data_dict)

def get_pattern(html):
    soup = BeautifulSoup(html, 'lxml')
    pattern = soup.find('div', id='search_holder').find(
        'input', id='search').get('value')
    return pattern

def get_page_data(html, pattern=''):
    ad : element.Tag
    data_list = list()
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    # search: title, price, location, url
    for ad in ads:
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''
        # Filter irrelevant content
        if pattern in title.lower():
            try:
                url = DOMAIN + ad.find(
                    'div', class_='description').find('h3').find('a').get('href')
            except:
                url = ''
            try:
                price = ad.find('div', class_='about').find(
                    'span', class_='price').text.strip()
            except:
                price = ''
            try:
                location = ad.find('div', class_='data').find_all('p')[-1].text
            except:
                location = ''
            data = {'title': title,
                    'price': price,
                    'location': location,
                    'url': url}
            data_list.append(data)
        else:
            continue
    return data_list

def main():
    base_url = 'https://www.avito.ru/rossiya/telefony'
    page_part = '?p='
    query_part = '&q=htc'
    fp = get_html(URL)
    tp = get_total_pages(fp)
    pt = get_pattern(fp)
    #for i in range(1, tp+1):
    for i in range(1, 3):
        url_gen = base_url + page_part + str(i) + query_part
        html = get_html(url_gen)
        data = get_page_data(html, pt)
    write_csvs(data)

if __name__ == '__main__':
    main()
