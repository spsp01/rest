import requests
import sqlite3
import datetime
import sys
import fire
import validators


now = datetime.datetime.now().strftime("%Y-%m-%d")

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

def statuscode(url):
    try:
        r = requests.get(url)
        return r.status_code
    except:
        return '0'


def add_url(url):
    select_url = "SELECT * from list_urls WHERE url = ?"
    url_add =(url,)
    cursor.execute(select_url, url_add)
    #statuscode(url))
    a = cursor.fetchone()
    if a == None:
        insert = "INSERT INTO list_urls(url,added) VALUES (?,?)"
        insert_q = (url,now)
        cursor.execute(insert,insert_q)
        connection.commit()
        print(url +' - dodano adres url')
    else:
        print('Adres znajduje się w bazie')

def add_url_status(url):
    url_status= statuscode(url)
    url_data =(now,url,url_status)
    insert_query = "INSERT INTO urls_status(data_add,url,response) VALUES (?,?,?)"
    cursor.execute(insert_query, url_data)
    connection.commit()
    print(url+' url status added')

def read_list_url():
    select_q = "SELECT * FROM list_urls"
    c = cursor.execute(select_q)
    fetch_all = cursor.fetchall()
    return fetch_all


class Program(object):

    def list(self):
        print(read_list_url())
    def add(self, url):
        if not validators.url(url):
            print("Error: Nieprawidłowy adres URL!")
        else:
            if statuscode(url) != '0':
                add_url(url)
            else:
                print("Adres URL nie odpowiada - nie dodano")
    def status_r(self):
        listed = read_list_url()
        for i in listed:
            add_url_status(i[1])
        print('Sprawdzono statusy')

    def importlinks(self, filename):
        f = open(filename, 'r')
        for line in f:
            add_url(line)
        f.close()


if __name__ == '__main__':
    fire.Fire(Program)

connection.close()

