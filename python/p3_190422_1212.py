#!/usr/bin/env python3
#p3_190422_1212.py
# Parsing an example of Apache log

import re
import csv
from collections import Counter

LOG_FILE = 'files/p3_190422_1212.log'
CSV_FILE = 'files/p3_190422_1212.csv'
PATTERN = r'(?:\d{1,3}\.){3}\d{1,3}'

def reader(filename):
    # Open and return list of IPs
    with open(filename) as f:
        log = f.read()
        ip_list = re.findall(PATTERN, log)
        return ip_list

def get_count(ip_list):
    # Return dictionary of repeated IPs in the list
    return Counter(ip_list)

def write_csv(count: dict):
    with open(CSV_FILE, 'w') as csvfile:
        writer = csv.writer(csvfile)
        # 1st row in the table
        header = ['IP', 'Frequency']
        writer.writerow(header)
        for item in count:
            # IP        | Frequency
            # dict-key  | dict-value
            writer.writerow( (item, count[item]) )

if __name__ == '__main__':
    write_csv(get_count(reader(LOG_FILE)))
