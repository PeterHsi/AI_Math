#%%
import os
import datetime
import pathlib
import pandas as pd
import requests
from bs4 import BeautifulSoup
#%%
# 取得巴哈動畫瘋官網 HTML
req_anigamer = requests.get('https://ani.gamer.com.tw/')
soup = BeautifulSoup(req_anigamer.text, 'html.parser')
thisSeasonAnime = soup.find_all(attrs={"data-look": "本季新番"})

## 擷取資訊項目
numAni = [x for x in range(len(thisSeasonAnime))]
title = [str(thisSeasonAnime[i].find('p').string) for i in numAni]
vol = [thisSeasonAnime[i].find(
    class_="newanime-vol").string.replace("第 ", "").replace(" 集", "") for i in numAni]
update = [thisSeasonAnime[i].find(
    class_="newanime-date").string.replace(" 更新", "") for i in numAni]
untrt_number = [thisSeasonAnime[i].find(
    class_="newanime-count") for i in numAni]
number = []
for str_temp in untrt_number:
    posi_end = str(str_temp).find("</span>")
    posi_stat = str(str_temp).rfind(">", 0, posi_end)
    num_temp = int(str(str_temp)[posi_stat+1:posi_end].replace(",", ""))
    number.append(num_temp)

## 將擷取資料彙整於表格
AnimeInfo = pd.DataFrame(
    {'title': title,
     'vol': vol,
     'update': update,
     'number': number
     })
### 加入彙整時間戳記
AnimeInfo['date'] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

#%%
# 存檔
tsp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
if not os.path.exists(pathlib.PurePath('DailyData/')):
    os.makedirs(pathlib.PurePath('DailyData/'))
AnimeInfo.to_csv(pathlib.PurePath('DailyData/AniGamerInfo '+tsp+'.csv'))