#!/usr/bin/env python3
# p3_190528_2334.py
# Script of logging and parsing JWS download link
# Modules: Selenium + Requests
# You have to export environment variables prior to the script launch

from requests import Session, cookies
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from os import environ
from json import loads as deserialize

XSRF = "XSRF-TOKEN"
SESSION = "sessionstream"
URL_ADSF = "https://www.stream.jw.org/adfs/login/username/"
URL_VIDEOS = "https://fle.stream.jw.org/event/languageVideos"
PAYLOAD_EN = '{"language":{"id_language":153,"symbol":"en","locale":"en","code_tv":null,"name":"English","vernacular":"English","spellings":null,"direction":"ltr","is_sign":"0","has_content":"1","id_branch_channel":"2596","has_translation":"1","date_format":"Y-m-d","country_description":"United States","version":"1","translatedName":"English","translatedNameWithCountry":"English (United States)","translatedNameWithSymbol":"English(United States)(en)","translatedNameWithLocale":"English (United States) (en)"}}'
HEADERS_LANG = {
    "Host": "fle.stream.jw.org",
    "Connection": "keep-alive",
    "Content-Length": "502",
    "Pragma": "no-cache",
    "Cache-control": "no-cache",
    "Origin": "https://fle.stream.jw.org",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Referer": "https://fle.stream.jw.org/federation/ok",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,fr;q=0.6",
}
HEADERS_DOWN = {
    "Host": "fle.stream.jw.org",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,fr;q=0.6",
}

def selenium_login():
    """Authorize with Chromium and return cookies"""
    url = URL_ADSF + environ["JW_USER"]
    passwd = environ["JW_PASS"]
    options = Options()
    options.add_argument("no-sanbox")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    password_input = driver.find_element_by_id("passwordInput")
    password_input.send_keys(passwd)
    submit_button = driver.find_element_by_id("submitButton")
    submit_button.click()
    xsrf_val = get_cookie(driver, XSRF)
    session_val = get_cookie(driver, SESSION)
    return xsrf_val, session_val

def get_cookie(driver, search_pattern):
    """Get a value from the given cookie"""
    return next(
        (
            cookie
            for cookie in driver.get_cookies()
            if cookie["name"] == (search_pattern)
        )
    )["value"]

def set_session(xsrf_value, session_value):
    """Return a session with the pre-installed cookies"""
    xsrf_cookie = cookies.create_cookie(
        name="XSRF-TOKEN", value=xsrf_value
    )
    session_cookie = cookies.create_cookie(
        name="sessionstream", value=session_value
    )
    s = Session()
    s.cookies.set_cookie(xsrf_cookie)
    s.cookies.set_cookie(session_cookie)
    return s

def request_events(xsrf_value, session_value):
    """Return application/json data with the list of events"""
    s = set_session(xsrf_value, session_value)
    headers = {"X-XSRF-TOKEN": s.cookies.get("XSRF-TOKEN")}
    headers.update(HEADERS_LANG)
    page_events = s.post(URL_VIDEOS, data=PAYLOAD_EN, headers=headers)
    return page_events.content

def request_link(url_event, xsrf_value, session_value):
    """Get a link from the redirected event"""
    s = set_session(xsrf_value, session_value)
    pd = s.get(url_event, headers=HEADERS_DOWN)
    print(s.cookies)
    return pd.url

def create_dict(event_list):
    """Return a dict with the information all about event"""
    event_dict = {
        "event_id": event_list[1]["data"]["id_event"],
        "description": event_list[1]["description"],
        "date": event_list[1]["date"],
        "url_event": event_list[1]["vod_firstfile_url"],
    }
    return event_dict

def check_environment():
    """Check whether you typed the correct password"""
    print(environ["JW_USER"])
    print(environ["JW_PASS"])

def main():
    cookies = selenium_login()
    # Extract cookies-tuple for the request
    # Deserealize app/json data to the event list
    el = deserialize(request_events(*cookies))
    # Compile an event dictionary for ensuing usage
    ed = create_dict(el)
    # Send an url-link with and extracted tuple of cookies
    url = request_link(ed["url_event"], *cookies)
    # Add new pair to the event dictionary
    ed.update(url_download=url)
    print(ed)
    # check_environment()

if __name__ == "__main__":
    main()
