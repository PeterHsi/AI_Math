---
tags: Jupyter, Python
---

# 讓 Jupyter 有變數監看功能

> [name=Peter Hsiao][time=Thu, Mar 14, 2019 2:05 PM]

許多 IDE 尤其是資料科學的 IDE 如 MatLab、RStudio 都有變數監看(Variable Explorer)的功能窗格，可以幫助我們更有效率的測試程式碼。由於 Jupyter 沒有內建此功能，要實現必須要透過外掛。

## Jupyter Notebook

- 安裝法 1：直接勾選啟用(以前安裝過 jupyter_contrib_nbextensions)

  由於是安裝在 jupyter_contrib_nbextensions，若有安裝的話，在 Notebook 的 Nbextensions 頁籤勾選即可設定(如下圖)

  ![](https://i.imgur.com/XrYwOiQ.png)


- 安裝法 2：透過終端機命令列安裝並啟用
  
  在終端機使用以下命令
  
  ```shell=
  # 安裝 jupyter_contrib_nbextensions
  conda install -c conda-forge jupyter_contrib_nbextensions
  # 啟用 varInspector/main
  jupyter nbextension enable varInspector/main
  ```

[參考來源](https://volderette.de/jupyter-notebook-variable-explorer/)

## Jupyter Lab 

Lab 環境下的外掛功能比 Notebook 強大許多(見下圖，不只可以監看目前變數，還可以點開看詳細)，但安裝上也有比多需要注意的地方：

![](https://i.imgur.com/mR6z2WG.gif)

1. 似乎不是所有瀏覽器都很配合，至少我本身使用的 Firefox 在功能上支援不完整，Chrome 卻運行正常。
2. 需要其他 Python 的 package：numpy、pandas、pyspark、tensorflow、keras。
3. 建議在安裝完成後，先執行一次 `jupyter lab build` 指令。

安裝指令：

```shell=
jupyter labextension install @lckr/jupyterlab_variableinspector
jupyter lab build
```

安裝完後右鍵選單會多出 Open Variable Inspector 的選項，若需要快捷鍵的話在 Lab 的 Setting 頁籤的 keyboard shortcut 加入

```javascript=
"variableinspector:open":{
    "command": "variableinspector:open",
    "keys": ["Ctrl I"],
    "selector": ".jp-Notebook"
}
```

(這邊示範的是用 Ctrl+I 當快捷鍵，因為本來 Lab 的 Ctrl+I 就是開一個空白的 inspector 頁籤)

[參考來源](https://github.com/lckr/jupyterlab-variableInspector)
