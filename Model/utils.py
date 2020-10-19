from basketball_reference_scraper.utils import get_player_suffix
import pandas as pd
from requests import get
from bs4 import BeautifulSoup, Comment
import re
from pandastable import Table, TableModel
def get_player_per():
    suffix =get_player_suffix('Lebron james')
    suffix.replace('/', '%2F')
    print(suffix)
    selector = 'advanced'  # advanced # all_salaries
    print(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url={suffix}&div=div_{selector}')
    r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url={suffix}&div=div_{selector}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]
       # print(df.columns)
        df.rename(columns={'Season': 'SEASON', 'PER': 'PER',
                           'Tm': 'TEAM', 'Lg': 'LEAGUE', 'Pos': 'POS', 'MP': 'MP'}, inplace=True)
        if 'FG.1' in df.columns:
            df.rename(columns={'FG.1': 'FG%'}, inplace=True)
        if 'eFG' in df.columns:
            df.rename(columns={'eFG': 'eFG%'}, inplace=True)
       # if 'FT.1' in df.columns:
          #  df.rename(columns={'FT.1': 'FT%'}, inplace=True)
        if 'PER' in df.columns:
            df.rename(columns={'per': 'PER'}, inplace=True)
        for name in soup.find_all('td class="right"'):
            salary = name.parent.find_all('td class="right"')[-1]  # last cell in the row
           # print(name.get_text())
           # print(salary.get_text())
        df1 = df.iloc[:, 7:8]  # Remember that Python does not slice inclusive of the ending index.


        career_index = df[df['SEASON'] == 'Career'].index[0]

        df = df.reset_index().drop('index', axis=1)
       # df1['PER'][0])   \\ to access the elments individually
        season_number = len(df1['PER']) - 1 # this variable will give us the number for the last season
        print(df1['PER'][season_number])
    #print(df.iloc[7])
   # print(df1)


def cleanHtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

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

print(get_player_salary('Lebron James'))
print(get_player_per())
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
