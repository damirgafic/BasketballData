# BasketballData
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) <br />
An application that gives the user the best/worst performing player in a certain salary range. I calculated this 
by taking a player's PER (Player Efficiency Rating) and dividing it by the player's contract for the 2019-2020 season.
The PER is a rating of a player’s per-minute  productivity. I wrote this to show what players outperformed their 
contract and which ones underperformed. 

I started building this application by first scraping data off www.basketball-reference.com. I created a web scraper 
that went through all 30 NBA team rosters. I then had a list of players from each team, but I discovered I had 
duplicates as well. Those duplicates were from players that played for more than one team during the 2019-2020 NBA 
season. To solve this issue, I created a function to delete duplicates. Then I created a function to scrape an individual 
player's statistics by visiting their webpage. During this process I noticed one of the players URL was showing they were 
under the /p/ index on the players table, but this player was actually under another letter by mistake. I found this bizarre and emailed the 
website team to address this issue. 

While the scraper traversed through the players, I did have some errors, such as players that did not have a contract during the season. 
To solve this, I wrote try and catch blocks to identify those players. And in the end I decided not to count those players in my analysis.
I created a function to store the player names and statistics in a file, so I wouldn’t need to scrape the website each time
the program was run. Once I had everything in a .txt file, I started working on transferring the data from the file to a 
class object in the program. I wrote a binary tree to sort the data for the players, but I decided eventually python's built 
in sort function was more convenient for my purposes. 

Finally, I started to work on the GUI. I linked my function that returns a best/worst player depending on the salary cap and
check boxes selected by the user.


## Getting Started

Clone the project and proceed to open the terminal. Go to the directory where the project lies in your system 
and then type 
''' 
python View.py
'''

## Built With

* [Tkinter](https://docs.python.org/3/library/tkinter.html) - The library used for GUI

## Authors

* **Damir Gafic** - [DamirGafic](https://github.com/DamirGafic)

## Acknowledgments
* Thanks to www.basketball-reference.com for the great exstensive library of NBA statistics
* And a big thank you to the team at www.basketball-reference.com for fixing the error I mentioned
