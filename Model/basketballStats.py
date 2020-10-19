import requests
from bs4 import BeautifulSoup



URL = 'https://www.basketball-reference.com/players/c/curryst01.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='advanced.2020')

print(results)

