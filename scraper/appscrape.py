from selenium import webdriver
import sqlite3
connection = sqlite3.connect('data.db')
#cursor = connection.cursor()
#create_table = "CREATE TABLE urls (id INTEGER, data text, url text, desc text)"
#cursor.execute(create_table)
d = webdriver.Chrome()

base_url = d.get('https://www.google.pl/search?q=mleko modyfikowane&num=100')
urls = d.find_elements_by_css_selector('h3.r a')
description = d.find_elements_by_css_selector('span.st')
links =[]

f = open('links.txt','w')
for index,i in enumerate(urls):
    url = str(i.get_attribute('href'))
  #  user = (index+1, '12-01-2018', url, 'desc' )
   # insert_query = "INSERT INTO urls VALUES (?,?,?,?)"
   # cursor.execute(insert_query, user)
    f.write(url+'\n')

'''    
for index, i in enumerate(description):
        desc = str(i.get_attribute('innerText'))
        user = (index + 1, '12-01-2018', url, 'desc')
        insert_query = "UPDATE  VALUES (?,?,?,?)"
        cursor.execute(insert_query, user)
'''

connection.commit()
connection.close()