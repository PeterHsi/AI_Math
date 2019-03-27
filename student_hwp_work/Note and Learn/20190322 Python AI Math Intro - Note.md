# 20190322 Python AI Math

[TOC]

今天上課檔案：[Git與GitHub的介紹](https://github.com/yenlung/AI_Math/blob/master/slides/Git%E8%88%87GitHub%E7%9A%84%E4%BB%8B%E7%B4%B9.pdf)、[05. Pandas.ipynb](https://nbviewer.jupyter.org/github/yenlung/AI_Math/blob/master/05.%20Pandas.ipynb)

## 插播: 在 `matplotlib` 圖中顯示中文

```python
import matplotlib as mpl
mpl.rc('font', family='Noto Sans CJK TC')

# 查詢字體列表
[f.name for f in mpl.font_manager.fontManager.ttflist]

# 另一個同學的作法
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

myf = FontProperties(fname = r'font_path')
plt.title('title', fontproperties = myf);
plt.xlabel('xlabel', fontproperties = myf);
plt.ylabel('ylabel', fontproperties = myf);
```

> ref: [解決Python 3 Matplotlib與Seaborn視覺化套件中文顯示問題](https://medium.com/marketingdatascience/%E8%A7%A3%E6%B1%BApython-3-matplotlib%E8%88%87seaborn%E8%A6%96%E8%A6%BA%E5%8C%96%E5%A5%97%E4%BB%B6%E4%B8%AD%E6%96%87%E9%A1%AF%E7%A4%BA%E5%95%8F%E9%A1%8C-f7b3773a889b)

## 找資料、清資料

### 一些 Open Data

- [政府資料開放平台](https://data.gov.tw)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

```python
import pandas as pd

# 讀入資料 (as dataframe)

## CSV
df = pd.read_csv('csv位置') # csv
## HTML
df = pd.read_html('網頁表格URL') # HTML
len(df) # 可能不只一張表，先看看有幾個

# 清資料 (Case by case)
df.head() # 讀表頭
colnames = df.loc[1].values # 先把第2行讀出來
df = df[2:] # 設定第三行開始才是資料
df.columns = colnames # 把列名稱灌進去

# 利用真假值篩選資料
undergraduate = df[(df['日間∕進修別'] == 'D 日') & (df['等級別']  == 'B 學士')]
```

老師上課用的例子

```python
'http://stats.moe.gov.tw/files/detail/107/107_student.csv'
'https://browser.geekbench.com/mac-benchmarks' # mac-benchmarks
'http://www.9800.com.tw/statistics.asp' # 大樂透
```

### View & Copy

![view 和 copy](20190322 Python AI Math Intro - Note.assets/pandas_view_copy.png)

```python
# 不加 Copy 的話可能會遇到 SettingWithCopyWarning!
df2 = undergraduate.loc[:, '學校名稱':'女生計'].copy()
```

### 修正數字格式

利用 atof

```python
import locale
locale.setlocale(locale.LC_NUMERIC, '')
df2['男生計'] = df2['男生計'].apply(locale.atof)
```

