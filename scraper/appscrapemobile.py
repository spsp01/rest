from selenium import webdriver
import sqlite3

from selenium.webdriver.chrome.options import Options

mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

d = webdriver.Chrome(chrome_options = chrome_options)


base_url = d.get('https://www.google.pl/search?q=mleko modyfikowane&num=100')
urls = d.find_elements_by_css_selector('div._Z1m > div > a')
description = d.find_elements_by_css_selector('div._bCp > div._D3n')
links =[]
desc = []

f = open('link_mobile.txt','w')
for index,i in enumerate(description):
    descw = str(i.get_attribute('innerHTML'))
    f.write(descw+'\n')


