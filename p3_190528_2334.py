#!/usr/bin/env python3
#p3_190528_2334.py
# Selenium + Requests
# Script of logging and parsing JW video streams
# You have to export environment variables prior to the script launch

from requests import Session, cookies
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ

XSRF = 'XSRF-TOKEN'
SESSION = 'sessionstream'
URL_ADSF = 'https://www.stream.jw.org/adfs/login/username/'
URL_VIDEOS = 'https://fle.stream.jw.org/event/languageVideos'
PAYLOAD_EN = '{"language":{"id_language":153,"symbol":"en","locale":"en","code_tv":null,"name":"English","vernacular":"English","spellings":null,"direction":"ltr","is_sign":"0","has_content":"1","id_branch_channel":"2596","has_translation":"1","date_format":"Y-m-d","country_description":"United States","version":"1","translatedName":"English","translatedNameWithCountry":"English (United States)","translatedNameWithSymbol":"English(United States)(en)","translatedNameWithLocale":"English (United States) (en)"}}'
HEADERS_LANG = {
    'Host': 'fle.stream.jw.org',
    'Connection': 'keep-alive',
    'Content-Length': '502',
    'Pragma': 'no-cache',
    'Cache-control': 'no-cache',
    'Origin': 'https://fle.stream.jw.org',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Referer': 'https://fle.stream.jw.org/federation/ok',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,fr;q=0.6',
}

def selenium_login():
    url = URL_ADSF + environ['JW_USER']
    passwd = environ['JW_PASS']
    options = Options()
    options.add_argument('no-sanbox')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    password_input = driver.find_element_by_id('passwordInput')
    password_input.send_keys(passwd)
    submit_button = driver.find_element_by_id('submitButton')
    submit_button.click()
    xsrf_val = get_cookie(driver, XSRF)
    session_val = get_cookie(driver, SESSION)
    return xsrf_val, session_val

def get_cookie(driver, search_pattern):
    return next((cookie for cookie in driver.get_cookies()
                 if cookie['name'] == (search_pattern)))['value']

def request_videos(xsrf_value, session_value):
    xsrf = cookies.create_cookie(
        name='XSRF-TOKEN', value=xsrf_value)
    session = cookies.create_cookie(
        name='sessionstream', value=session_value)
    s = Session()
    s.cookies.set_cookie(xsrf)
    s.cookies.set_cookie(session)
    headers = {'X-XSRF-TOKEN': s.cookies.get('XSRF-TOKEN')}
    headers.update(HEADERS_LANG)
    page_events = s.post(URL_VIDEOS, data=PAYLOAD_EN, headers=headers)
    #print(s.cookies)
    return page_events.content

def check_environment():
    print(environ["JW_USER"])
    print(environ['JW_PASS'])

def main():
    cookies = selenium_login()
    print(request_videos(*cookies))
    check_environment()

if __name__ == '__main__':
    main()
