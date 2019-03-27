# 20190308 Python AI Math

[TOC]

## Info

- 線上直播連結： [http://bit.ly/aimath_video](https://www.youtube.com/playlist?list=PLQZfZKhc0kiAn7xGZ-WKkwQyseO8SbVR0)

- GitHub：https://github.com/yenlung/AI_Math

  (可視化程式碼：https://bit.ly/yenlung)

- 今天上課示範程式碼：

  [02. Python 101.ipynb](https://github.com/yenlung/AI_Math/blob/master/02.%20Python%20101.ipynb)

  [03. Python 資料分析主流環境 Jupyter.ipynb](https://github.com/yenlung/AI_Math/blob/master/03.%20Python%20%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E4%B8%BB%E6%B5%81%E7%92%B0%E5%A2%83%20Jupyter.ipynb)

  [0308TAcode.ipynb](https://nbviewer.jupyter.org/github/yenlung/AI_Math/blob/master/0308TAcode.ipynb)


## Python Code Intro

### 輸入 Package、畫圖(上次上課)

Package

```python
import Package名稱 
from Package名稱 import 該Package函數(或物件)
```

Plot

```python
%matplotlib inline #在jupyter中加這個不用再特別show圖

import matplotlib.pyplot as plt #載入畫圖的套件並命名 plt
import numpy as np #很多數學函數
import pandas as pd #順便

plt.plot(X,Y) #折線圖
plt.scatter(X,Y) #散布圖
plt.xkcd() #使圖變成漫畫形式

np.random.rand(n) #輸出n個亂數(以array格式)
np.linspace(start, end, n) #給出兩點之間的n個點(以array格式)
np.sin(X) #sin函數
```

### 資料型態

字串單雙引號沒區別，但三個單/雙引號可以自動把換行轉換成\n

```python
x='''為什麼會變成這樣呢？
明明都是我先來的。
為什麼你會這麼熟練啊！'''

# 會被記錄成 '為什麼會變成這樣呢？\n明明都是我先來的。\n為什麼你會這麼熟練啊！'
# 順帶一提 '這是不能換行的，換行會出事'
# 字串可加/乘
```

#### List 串列

```python
x = [a, b, c, d, f] #基本的 list
x = list(str) #會把 string 每個單一符號拆成一個 list
```

但我們最常用的還是 array

#### 字典

```python
x = {"srt1":a, "str2":b,...}
```

#### Python 變數 Index 的方法

原則不分資料型態

![slicing](Slide/images/slicing.jpeg)

ex: 要調出 "E"，使用 `[4]` 或 `[-7]` 都可以

```python
x[a:-b] #從a讀到-b(不包含第-b個)，省a或-b就是從頭或到尾
x[:] #全叫
```

### 基礎函數

#### input 要求輸入

```{.python .input}
變數 = input("提示訊息") #進去會變成字串，要用其他函數把字串變成數字
```

#### def 自訂義函數

```{.python .input}
def 函數命名(函數變數):
    '''函數說明(shift+tab可以調出來說明)''' #或是用 `函數名?` 也能調出來
    #程式碼 #需要縮排(用space不要用tab)
    return(輸出變數)
```

#### print 的 f-string

Literal String Interpolation `f'...字串{變數}字串{變數}...'` 能直接全部拼成字串

```{.python .input  n=2}
stock = 'tsmc'
close = 217.5
f'{stock} price: {close}' #會回傳 stock+" price: "+str(close)
```

假如要在變數裡面呼出元素需要用到 `‘單引號’` ，f 的單引號可以改成 `“雙引號”` (也可以反過來)

### if 條件判斷

```{.python .input}
if 條件1:
    #條件1 為 T 執行的程式碼
elif 條件2:
    #"條件1=F"且"條件2=T" 執行的程式碼
...
else:
    #之前條件都F的程式碼  
```

### while/for

```python
while eggs != 'bye':
    eggs = input('>> ')
    if eggs == 'bye':
        print('再見!')
    elif '快樂' in eggs:
        print('太好了!')
    else:
        print('拍拍')
```

```python
lens = ['31mm', '43mm', '77mm']

for i in lens:
    print(i)
```

#### 其他常用

```python
range(start=0, n)
```

```python
A in B #若B中有A元素為T
```

```python
from IPython.display import clear_output #可以清空 cell 顯示的指令 (Jupyter 指令)
import time #時間套件 (Python 標準套件)

clear_output(wait=True) #
time.sleep(0.5) #暫停python0.5秒
```

#### `zip` 和 `upzip`

```python
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 0]
points = list(zip(x,y))
points
#會是[(1, 6), (2, 7), (3, 8), (4, 9), (5, 0)]

list(zip(*points))
#變成[(1, 2, 3, 4, 5), (6, 7, 8, 9, 0)]

x, y = list(zip(*points))
#x, y回到一開始
```

最後 `*points` 的 `*` 在 Python 只是說 `points` 中的所有元素, 我們也不知有多少個, 就打個 `*` 。

## Jupyter Notebook 介紹

### 魔術指令

```python
%cd 資料夾路徑 #會進入指定資料夾
%matplotlib inline
```

### Tab 鍵的用處

- $\LaTeX$ 碼 +Tab 就能轉換字符
- 程式碼/已命名變數的自動補齊 Shift+Tab 或 Tab


### commond+M：指令/Meta模式

| 指令 | 效果                |
| ---- | ------------------- |
| M    | block 變成 Markdown |

### 互動

```{.python .input}
def f(x):
    print(x)
    
from ipywidgets import interact

interact(f, x=3) # 滑桿會是整數
interact(f, x=3.) # 滑桿會是浮點數
interact(f, x=(1, 10)) # 範圍
interact(f, x="字串") # 會出現輸入框
interact(f, x=List) # 會出現選單
interact(f, x={"字典1":1, "字典2":2}) # 會出現選單，但回傳值會對應字典內的資料
interact(); # 美觀

interact_manual() # 不會直接執行(手動)
```

函數預設值會成為範圍輸入的預設值

## 助教課

###　%matplotlib inline 的用處

不加的話需要用 `plt.show()` 才能顯示出圖，加的話就會直接有圖(plt指的是matplotlib.pyplot)

### matplotlib 相關功能

### Seaborn

`seaborn` 套件可以簡單畫漂亮的圖!

```python
import seaborn as sns
sns.distplot(eggs)
```