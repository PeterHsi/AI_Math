#%% 
import pandas as pd
import requests
req_anigamer = requests.get('https://ani.gamer.com.tw/')

#%%
from bs4 import BeautifulSoup
soup = BeautifulSoup(req_anigamer.text, 'html.parser')
thisSeasonAnime = soup.find_all(attrs={"data-look": "本季新番"})
numAni = [x for x in range(len(thisSeasonAnime))]
title = [thisSeasonAnime[i].find('p').string for i in numAni]
vol = [thisSeasonAnime[i].find(
    class_="newanime-vol").string for i in numAni]
update = [thisSeasonAnime[i].find(
    class_="newanime-date").string for i in numAni]
number = [thisSeasonAnime[i].find(class_="newanime-count").findChild('span') for i in numAni]

AnimeInfo = pd.DataFrame(
    {'title': title,
     'vol': vol,
     'update': update,
     'number': number
     })

AnimeInfo.head()
