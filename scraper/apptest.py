from selenium import webdriver
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE urls (id INTEGER, data text, url text, status text)"
cursor.execute(create_table)
d = webdriver.Firefox()
base_url = d.get('https://www.google.pl/search?q=performance-media&num=100')
urls = d.find_elements_by_css_selector('h3.r a')
description = d.find_elements_by_css_selector('span.st')
links =[]
for index,i in enumerate(urls):
    print(str(i.get_attribute('innerText')))

