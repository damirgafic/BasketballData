from requests import get
from bs4 import BeautifulSoup, Comment
import re


def cleanHtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def get_player_salary (name):
    suffix = get_player_suffix('Lebron james')
    print(suffix.replace('/', '%2F'))
    r = get('https://www.basketball-reference.com/players/j/jamesle01.html')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        table_div = soup.find('div', {'id': 'all_contract'})
        comment = table_div.find(string=lambda text: isinstance(text, Comment))
        soup2 = BeautifulSoup(comment, 'html.parser')
        salaries = (soup2.findAll('td'))
      # test  print(cleanHtml(str(salaries[1])))

