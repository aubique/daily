#!/usr/bin/env python3
# p3_190603_2042.py
# Progress-bar downloading and base64 CLI encode-decode functions
# Base64 CLI: -e encode / -d decode

from clint.textui import progress
from pathlib import Path
from os.path import expanduser
from base64 import b64encode, b64decode
from sys import argv
import requests

FILENAME = 'p3_190602_2042'
URL = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
SIZE = 1024

def download_clink():
    r = requests.get(URL, stream=True)
    #fname = str(Path.home()) + '/Downloads/' + FILENAME + '.mp3'
    fname = expanduser('~') + '/Downloads/' + FILENAME + '.mp3.'
    with open(fname, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=SIZE),
                                  expected_size=(total_length/SIZE) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

def convert_to_bin(string):
    return string.encode('utf-8', 'ignore')

def encode_b64(string):
    enc64data = b64encode(convert_to_bin(string))
    return enc64data

def decode_b64(encoded_string):
    dec64data = b64decode(convert_to_bin(encoded_string))
    return dec64data.decode('utf-8', 'ignore')

def show(argument, callback_func):
    print(argument)
    print(callback_func(argument))

def main():
    if argv[1] == '-e':
        [show(arg, encode_b64) for arg in argv[2:]]
    elif argv[1] == '-d':
        [show(arg, decode_b64) for arg in argv[2:]]

if __name__ == '__main__':
    main()
