import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

#TODO: Explain what this does
#requests makes a request for the webpage's Html and turns it into text
html_text = requests.get('https://store.steampowered.com/search/?supportedlang=norwegian%2Cenglish&specials=1&hidef2p=1&ndl=1').text

#Has BeautifulSoup store the webpage's Html into the lxml's library
soup = BeautifulSoup(html_text, 'lxml')

#TODO:Write a good description on what this does idk
#from the html that BeautifulSoup shoved into the lxml's library
games = soup.find_all('a', class_ = 'search_result_row ds_collapse_flag')


#TODO: find out if you can figure out how to find the titles from the games from games.

#prints the html that was found from games
print(games)


