from selenium import webdriver
import sqlite3

d = webdriver.Firefox()
base_url = d.get('https://www.google.pl/search?q=performance-media&num=100')
urls = d.find_elements_by_css_selector('h3.r a')
description = d.find_elements_by_css_selector('span.st')
links =[]
for index,i in enumerate(urls):
      print(str(i.get_attribute('innerText')))

