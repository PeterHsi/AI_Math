---
tags: Jupyter, Python 
---

# 程式碼美化(Code Beautify)外掛

程式碼美化本身的規則 package 是放在 python 底下，目前常用的有三種：

```shell=
# 則一安裝即可，不需要全裝(當然你想要全裝也可以)
pip install black
pip install yapf
pip install autopep8
```

這個要先安裝下面的才能用。

## Notebook 外掛

Notebook 的外掛本身包在 jupyter_contrib_nbextensions 這個大補帖裡面：

```shell=
conda install -c conda-forge jupyter_contrib_nbextensions
```

安裝後直接進筆記本在 NBextensions 頁籤啟用即可。

## Lab 外掛

[@ryantam626/jupyterlab_code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter)

安裝與啟用指令：

```shell=
jupyter labextension install @ryantam626/jupyterlab_code_formatter
pip install jupyterlab_code_formatter
jupyter serverextension enable --py jupyterlab_code_formatter
# 請注意如此僅有安裝格式化外掛本身，格式化規則需要另外安裝
```

要安裝格式化規則需要回到 pip 裡面

安裝完成後可以用 lab 的 commend panel 點選 [jupyterlab code formatter:格式化規則] 指令執行(錯誤碼會藏在 lab 的 cmd 視窗裡面，若沒動作記得回去看)。

但這樣很麻煩，所以我們會需要設定快速鍵((Ctrl+\`)進入進階設定頁籤)：

```javascript=
{"jupyterlab_code_formatter:black":{
    "command": "jupyterlab_code_formatter:black",
    "keys": [
       "你要的快速鍵組合" 
    ],
    "selector": ".jp-Notebook.jp-mod-editMode"
}}
```
```