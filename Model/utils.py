import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup, Comment
import re
import time

from Model.basketballStats import get_player_suffix

teamArray = ["ATL", "BRK", "BOS", "CHO", "CHI", "CLE", "DAL",
             "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
             "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR",
             "SAC", "SAS", "TOR", "UTA", "WAS"]


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

    # print(player_names)


def scrape_data():  # function to scrape team rosters, player salaries, and player stats
    # and to place this data into a file
    # steps to scrape all this information
    # 1) scrape team roster (I have function for this already)
    # 2) scrape player salaries (have function already)
    # 3) scrape each players PER stat (have function for this already)
    # 3 arrays [players, salaries, playerPer] element numbers should match up with players
    # read the arrays into file EX: Giannis Antetokounmpo 25,842,697 31.9
    teams = []

    playersPer = []
    salaries = []
    f = open("PlayerNames2020.txt", "r")
    players = f.read().splitlines()
    print(players)
    for i in range(len(players)):
        try:
            playersPer.append(get_player_per(players[i]))
            salaries.append(get_player_salary(players[i]))
            print(i)
            print(playersPer[i])
            print(salaries[i])
            time.sleep(3)
        except requests.exceptions.ConnectionError:
            playersPer.append('Name Error')
            salaries.append('Name Error')
            print(playersPer[i] + '\n' + salaries[i])

    f = open("BasketballData2020.txt", "x")
    for i in range(len(players)):
        f.write(players[i] + ' ' + salaries[i] + ' ' + playersPer[i] + '\n')
    f.close()
    print(players)

scrape_data()







#print(get_player_per('Wendell Carter'))


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
