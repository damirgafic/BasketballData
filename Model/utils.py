from basketball_reference_scraper.utils import get_player_suffix
import pandas as pd
from requests import get
from bs4 import BeautifulSoup, Comment
import re
from pandastable import Table, TableModel
def cleanHtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def get_player_per(name):
    suffix =get_player_suffix(name)
    r = get(f'https://www.basketball-reference.com{suffix}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        table_div = soup.find('div', {'id': 'all_advanced'})
        comment = table_div.find(string=lambda text: isinstance(text, Comment))
        soup2 = BeautifulSoup(comment, 'html.parser')
        per = soup2.findAll('td', {'data-stat': 'per'})
        currentPer = (len(per)-2)
        return cleanHtml(str(per[currentPer]))

def get_player_salary (name): # retrieve player salary from 2019-2020 season
    suffix = get_player_suffix(name)
   # print(suffix.replace('/', '%2F'))
    r = get(f'https://www.basketball-reference.com{suffix}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        table_div = soup.find('div', {'id': 'all_contract'})
        comment = table_div.find(string=lambda text: isinstance(text, Comment))
        soup2 = BeautifulSoup(comment, 'html.parser')
        salaries = (soup2.findAll('td'))
        return cleanHtml(str(salaries[1]))
      # test  print(cleanHtml(str(salaries[1])))

def get_team_roster(team): # team variable uses team acronyms ex: GSW, LAL, etc.
    r = get(f'https://www.basketball-reference.com/teams/{team}/2020.html')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        #print(soup)
        table_div = soup.find('div', {'id': 'all_advanced'})
        #print(table_div)
        player_names = table_div.findAll('tbody')

        player_names = (cleanHtml(str(player_names)))
        player_names = re.sub(r'[\[\]0-9.-]+', '', player_names)
        names = player_names.splitlines()
        names.pop(0) # removes first element which is a blank element
        return names

       # print(player_names)


#print(get_player_salary('Lebron James').replace(',','').replace('$',''))
#print(get_player_per('Stephen Curry'))
#print(get_team_roster('LAL'))
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
