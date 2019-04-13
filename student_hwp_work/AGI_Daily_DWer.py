import os
import datetime
import pathlib
import pandas as pd
import requests
from bs4 import BeautifulSoup

reqAniGamer = requests.get('https://ani.gamer.com.tw/')
soup = BeautifulSoup(reqAniGamer.text, 'html.parser')
thisSeasonAnime = soup.find_all(attrs={"data-look": "本季新番"})

numAni = [x for x in range(len(thisSeasonAnime))]
title = [str(thisSeasonAnime[i].find('p').string) for i in numAni]
vol = [thisSeasonAnime[i].find(
    class_="newanime-vol").string.replace("第 ", "").replace(" 集", "") for i in numAni]
update = [thisSeasonAnime[i].find(
    class_="newanime-date").string.replace(" 更新", "") for i in numAni]
unNumber = [thisSeasonAnime[i].find(
    class_="newanime-count") for i in numAni]
number = []
for str_temp in unNumber:
    posEnd = str(str_temp).find("</span>")
    posSta = str(str_temp).rfind(">", 0, posEnd)
    num_temp = str(str_temp)[posSta+1:posEnd].replace(",", "")
    number.append(num_temp)

AnimeInfo = pd.DataFrame(
    {'title': title,
     'vol': vol,
     'update': update,
     'number': number
     })
AnimeInfo['date'] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
AnimeInfo.drop_duplicates(inplace = True)

tsp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
if not os.path.exists(pathlib.PurePath('DailyData/')):
    os.makedirs(pathlib.PurePath('DailyData/'))
AnimeInfo.to_csv(pathlib.PurePath('DailyData/AGI_Daily_'+tsp+'.csv'))