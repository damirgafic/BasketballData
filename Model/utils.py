import unicodedata

import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup, Comment
import re
import time

#from Model.basketball_stat_function_collector import get_player_suffix


teamArray = ["ATL", "BRK", "BOS", "CHO", "CHI", "CLE", "DAL",
             "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
             "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR",
             "SAC", "SAS", "TOR", "UTA", "WAS"]


def get_player_suffix(name):
    normalized_name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode("utf-8")
    names = normalized_name.split(' ')[1:]
    for last_name in names:
        initial = last_name[0].lower()
        r = get(f'https://www.basketball-reference.com/players/{initial}')
        if r.status_code==200:
            soup = BeautifulSoup(r.content, 'html.parser')
            for table in soup.find_all('table', attrs={'id': 'players'}):
                suffixes = []
                for anchor in table.find_all('a'):
                    if unicodedata.normalize('NFD', anchor.text).encode('ascii', 'ignore').decode("utf-8").lower() in normalized_name.lower():
                        suffix = anchor.attrs['href']
                        player_r = get(f'https://www.basketball-reference.com{suffix}')
                        if player_r.status_code==200:
                            player_soup = BeautifulSoup(player_r.content, 'html.parser')
                            h1 = player_soup.find('h1', attrs={'itemprop': 'name'})
                            if h1:
                                page_name = h1.find('span').text
                                if page_name.lower()==name.lower():
                                    return suffix

def cleanHtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def get_player_per(name):
    suffix = get_player_suffix(name)
    r = get(f'https://www.basketball-reference.com{suffix}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        table_div = soup.find('div', {'id': 'all_advanced'})
        comment = table_div.find(string=lambda text: isinstance(text, Comment))
        soup2 = BeautifulSoup(comment, 'html.parser')
        per = soup2.findAll('td', {'data-stat': 'per'})
        currentPer = (len(per) - 2)
        return cleanHtml(str(per[currentPer]))


def get_player_salary(name):  # retrieve player salary from 2019-2020 season
    suffix = get_player_suffix(name)
    # print(suffix.replace('/', '%2F'))
    r = get(f'https://www.basketball-reference.com{suffix}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        try: #some players do not have .find
            table_div = soup.find('div', {'id': 'all_contract'})
            comment = table_div.find(string=lambda text: isinstance(text, Comment))
        except AttributeError:
            return 'N/A'
        soup2 = BeautifulSoup(comment, 'html.parser')
        salaries = (soup2.findAll('td'))
        try:
            return cleanHtml(str(salaries[1]))
        except IndexError:
            return 'No Contract'
    # test  print(cleanHtml(str(salaries[1])))


def get_team_roster(team):  # team variable uses team acronyms ex: GSW, LAL, etc.
    r = get(f'https://www.basketball-reference.com/teams/{team}/2020.html')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup)
        table_div = soup.find('div', {'id': 'all_advanced'})
        # print(table_div)
        player_names = table_div.findAll('tbody')

        player_names = (cleanHtml(str(player_names)))
        player_names = re.sub(r'[\[\]0-9.-]+', '', player_names)
        names = player_names.splitlines()
        names.pop(0)  # removes first element which is a blank element
        return names









# print(get_player_salary('Lebron James').replace(',','').replace('$',''))
# print(get_player_per('Stephen Curry'))
# print(get_team_roster('LAL'))
'''
class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Table app')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        #df = TableModel.getSampleData()
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()
        return

app = TestApp()
#launch the app
app.mainloop()
'''
