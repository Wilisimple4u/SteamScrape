import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


class TestError(BaseException):
    ...


#TODO: Explain what this does
#requests makes a request for the webpage's Html and turns it into text
html_text = requests.get('https://store.steampowered.com/search/?supportedlang=norwegian%2Cenglish&specials=1&hidef2p=1&ndl=1').text

#Alternative
#url = 'https://store.steampowered.com/search/?supportedlang=norwegian%2Cenglish&specials=1&hidef2p=1&ndl=1'
#page = requests.get(url)



#Has BeautifulSoup store the webpage's Html into the lxml's library
soup = BeautifulSoup(html_text, 'lxml')
#soup = BeautifulSoup(page.text, 'html')


#TODO:Write a good description on what this does idk
#from the html that BeautifulSoup shoved into the lxml's library

#
    #titleAll = soup.find_all('span', class_ = 'title')
    #dateAll = soup.find_all('div', class_ = 'col search_released responsive_secondrow')
    #priceAll = soup.find_all('div', class_ = 'discount_final_price')


    #gamesAll = titleAll, dateAll


title = soup.find('span', class_ = 'title')
date = soup.find(class_ = 'col search_released responsive_secondrow')
price = soup.find_all('div', class_ = 'col search_price_discount_combined responsive_secondrow')


topGame = title, date


#TODO: find out if you can figure out how to find the titles from the games from games.



#prints the html that was found from games
#print(soup)

#Print first
print(topGame)
#Print all
    #print(gamesAll)


