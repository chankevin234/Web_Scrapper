import requests
import pprint

URL = 'https://ca.indeed.com/jobs?q=software+developer&l=Toronto%2C+ON'
page = requests.get(URL)

print(page)