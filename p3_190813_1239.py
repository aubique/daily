#!/usr/bin/env python3
# p3_190813_1239.py
# Parse search results on eBay and extract data to CSV

import requests
from bs4 import BeautifulSoup
import csv

SEARCH_REQUEST = "Office 2008"
CSV_FILE = "files/p3_190813_1239.csv"
URL1 = "https://www.ebay.com/sch/i.html?_nkw="
URL2 = "&_sop=12"

class eBayParse:
    def __init__(self, request: str):
        self.url: str = URL1 + self.format_search(request) + URL2
        self.len_results: int = 0
        self.html: str = ''
        self.results: list = []
        self.is_finished: bool = False

    def request_html_page(self):
        """Get a html page for object.html"""
        req = requests.get(self.url)
        #print(req.status_code)
        if req.ok: #200
            self.html = req.text

    def set_len_results(self):
        """Look for results number in HTML"""
        soup = BeautifulSoup(self.html, 'lxml')
        # Find the number
        count: str = soup.find('div', class_='clearfix').find('h1').text
        # Split by whitespace then split by ,
        nums = count.split()[0].split(',')
        # Merge list of numbers
        self.len_results = ''.join(nums)

    def parse_results_from_html(self):
        """Parse and collect data from HTML"""
        soup = BeautifulSoup(self.html, 'lxml')
        # Find a bulleted list and list items
        lis = soup.find(
            'ul', class_='srp-results srp-list clearfix'
        ).find_all('li', class_='s-item')
        for li in lis:
            url = li.find('a', class_='s-item__link').get('href')
            name = li.find('h3').text
            # Get description information
            info = li.find('div', class_='s-item__subtitle')
            # Doesn't want to save "New Brand" info
            if info.find('span'):
                desc = 'No info'
            # If first infoription isn't a nested span
            else:
                desc = info.text
            data = {'name': name,
                    'desc': desc,
                    'url': url}
            self.results.append(data)

    def set_url(self):
        """Set a new URL to keep parsing"""
        s = BeautifulSoup(self.html, 'lxml')
        p = s.find('div', class_='s-pagination')
        pagination = p.find(
            'a', {
                'class': 'x-pagination__control',
                'rel': 'next'
            }
        )
        if pagination.get('aria-disabled'):
            self.is_finished = True
        self.url = pagination.get('href')

    def write_results_to_csv(self):
        """Write list of dictionaries to CSV"""
        with open(CSV_FILE, 'w') as f:
            writer = csv.writer(f)
            for data in self.results:
                writer.writerow(tuple([data[item] for item in data]))

    @staticmethod
    def format_search(request):
        """Format a string to URL query`"""
        return '+'.join(request.split())


def main():
    par = eBayParse(SEARCH_REQUEST)
    while not par.is_finished:
        par.request_html_page()
        par.set_len_results()
        par.parse_results_from_html()
        par.set_url()
        print(par.url)
    par.write_results_to_csv()


if __name__ == '__main__':
    main()
