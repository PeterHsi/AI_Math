---
tags: Jupyter, python
---

# Jupyter 的介面調整概念(未完成)

> 研究了幾天 Jupyter，發現有許多可以自訂義的功能，也有蠻多眉眉角角的細節需要注意，故寫了這個日誌，供人參考也作為個人筆記紀錄。
> 
> 這個 hackmd 的筆記本將開放編輯權限給 "登入 HackMD" 的使用者，想要分享或更正的歡迎大家集思廣益，謝謝。
> 
> P.s. 更動目錄表請至 https://hackmd.io/Sy_DHe8DE/
> 
> [name=Peter Hsiao][time=Thu, Mar 14, 2019 1:06 PM]

## Jupyter 能自訂義的內容

1. 選擇使用 Lab 或 Notebook

   Jupyter Lab 跟 Jupyter Notebook 幾乎是兩個不一樣的系統(尤其在外掛這方面)，雖然說 Lab 是現在 Jupyter project 主力發展的計畫，其介面也強大完整(以主流 IDE 為衡量標準，比 Notebook 還好很多)，但由於發展較晚以及不相容 Notebook 的外掛，很多已經在 Notebook 很成熟的外掛或功能設定，反而 Lab 沒有提供。
   
   | 功能 | Jupyter Lab | Jupyter Notebook |
   |:----:| ----------- | ---------------- |
   | UI   | 整合度較高 | 比較類似分別網頁的概念(分頁要靠瀏覽器) |
   | 啟動行為 | 會回復之前工作狀態 | 重新開啟現在的檔案夾(若用 Anaconda 自帶的捷徑會是預設是開啟使用者資料夾) |
   | App Like | 更像一個應用軟體 | 比較像在網站填寫表格 |
   | 程式碼提示(Tab) | 很漂亮 | 陽春 |
   | extension | 使用 labextension 系列，目前並不非常完善，安裝相對繁瑣 | 使用 nbextension 系列，功能齊全，爾且安裝相對容易 |
   
2. 設定(Setting)
   - 直接至 .jupyter 資料夾設定 (待完成)
       - .jupyter/custom/custom.js
       - .jupyter/jupyter_notebook_config.py
   - 透過 UI 設定 (待完成)
3. 外掛
   1. 使用命令列安裝並設定 (待完成)
   2. 使用管理外掛的官方外掛設定 (待完成)
      - Notebook 的管理外掛 (待完成)
      - Lab 的管理外掛 (待完成)
