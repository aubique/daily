#!/usr/bin/env python3
#p3_190427_2103.py
# Parsing Avito. Part 2
# Exploiting Selenium-webdriver as alternative of PhantomJS

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from PIL import Image
from PIL.PngImagePlugin import PngImageFile
from pytesseract import image_to_string
from base64 import decodebytes

URL1 = 'https://www.avito.ru/rossiya/telefony?p=1&q=htc'
URL = 'https://www.avito.ru/kaluga/telefony/prodam_htc10_m10h_gray_1105880585'
BCLASS = 'button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card'
ICLASS = 'item-phone-big-number js-item-phone-big-number'
SCREEN = 'files/p3_190427_2103'
PNG = '.png'
GIF = '.gif'

class Bot:
    def __init__(self):
        options = Options()
        options.add_argument('--no-sandbox') # Bypass OS security model
        self.driver = webdriver.Chrome(chrome_options=options)
        self.navigate()
    def navigate(self):
        self.driver.get(URL)
        button = self.driver.find_element_by_xpath('//a[@class="{}"]'.format(BCLASS))
        button.click()
        self.take_screenshot()
        self.decode_img()
        #self.get_grop()
        self.recon()
    def take_screenshot(self):
        sleep(1)
        self.driver.save_screenshot(SCREEN+PNG)
    def screenshot_crop(self, image:PngImageFile, x, y, width, height):
        print('x:\t{}\ny:\t{}\nw:\t{}\nh:\t{}'.format(x, y, width, height))
        sleep(1)
        image.crop((x, y, x+width, y+height)).save(SCREEN+GIF)
    def get_grop(self):
        i = self.driver.find_element_by_xpath('//div[@class="{}"]//*'.format(ICLASS))
        l = i.location      # dict {'x': 2332, 'y': 3232}
        s = i.size          # dict {'width': 488, 'height': 844}
        self.set_grop(l, s)
    def set_grop(self, location, size):
        image: PngImageFile = Image.open(SCREEN+PNG)
        x = location['x']
        y = location['y']
        w = size['width']
        h = size['height']
        self.screenshot_crop(image, x, y, w, h)
    def recon(self):
        image = Image.open(SCREEN+GIF)
        print(image_to_string(image))
    def decode_img(self):
        image = self.driver.find_element_by_xpath('//div[@class="{}"]/img'.format(ICLASS))
        image_src = image.get_attribute('src').split(',')[1]
        img = decodebytes(bytearray(image_src, 'utf-8'))
        with open(SCREEN+GIF, 'wb') as f:
            f.write(img)

def main():
    b1 = Bot()

if __name__ == '__main__':
    main()
