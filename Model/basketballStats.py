from requests import get
from bs4 import BeautifulSoup
import unicodedata

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
                    print(unicodedata.normalize('NFD', anchor.text).encode('ascii', 'ignore').decode("utf-8").lower())
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


