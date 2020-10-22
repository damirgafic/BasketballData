import time
import unicodedata
from Model.utils import get_player_salary, get_player_per, requests

def scrape_data():  # function to scrape team rosters, player salaries, and player stats
    # and to place this data into a file
    # steps to scrape all this information
    # 1) scrape team roster (I have function for this already)
    # 2) scrape player salaries (have function already)
    # 3) scrape each players PER stat (have function for this already)
    # 3 arrays [players, salaries, playerPer] element numbers should match up with players
    # read the arrays into file EX: Giannis Antetokounmpo 25,842,697 31.9
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

#scrape_data()

'''
f = open("PlayerNames2020.txt", "r+")
players = f.read().splitlines()
players = list(dict.fromkeys(players))
f.seek(0)
f.truncate()
for i in range(len(players)):
    f.write(players[i] + '\n')
f.close()
'''