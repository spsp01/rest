import requests

r = requests.get('http://www.dns.pl/deleted_domains.txt')

print(r.text)
