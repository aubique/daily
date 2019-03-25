#!/usr/bin/env python3
#p3_190325_2257.py
# WWTBAM game
# CLI-based app

import json

class WWTBAM:
    def __init__(self):
        pass
    def first_question(self):
        pass
    def create_file(self):
        with open('files/WWTBAM1.json', 'w') as f:
            pass
    def open_file(self):
        with open('files/WWTBAM1.json', 'r') as f:
            jsondata = json.load(f)
            print(jsondata[0]['A'][0])

def main():
    cli_app = WWTBAM()
    cli_app.open_file()

if __name__ == '__main__':
    main()
