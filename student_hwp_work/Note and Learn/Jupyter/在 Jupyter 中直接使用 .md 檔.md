---
tags: Jupyter, Python
---

# 在 Jupyter 中直接使用 .md 檔


[notedown](https://github.com/aaren/notedown) 是一個 python package 用來橋接 markdown 文件與 Jupyter 的 `.ipynb` 文件，對我們最重要的功能就是在 Jupyter 下可以直接把 `.md` 讀入成  `.ipynb` 文件。


在安裝 notedown 之前我們在 Jupyter 打開 `.md` 檔會是這樣的：

![](https://i.imgur.com/eH0aMxY.png)


## 安裝 [notedown](http://github.com/aaren/notedown) 並設定

1. 在終端機內以下列指令安裝

   ```bash
   pip install notedown
   ```

2. 生成 Jupyter 設定

   ```bash
   jupyter notebook --generate-config
   ```

   執行完會在資料夾生成 Jupyter 設定檔

   ![](https://i.imgur.com/bYBXLKp.png)

3. 去輸出的路徑尋找 `jupyter_notebook_config.py` 檔案，並在檔案最後加入下列指令：

   ```
   c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'
   ```

   ![](https://i.imgur.com/fN70lBk.png)


現在安裝完成後，再用 Jupyter 開啟 `.md` 檔會是這樣：

![](https://i.imgur.com/eRB5M8L.png)


安裝完後， `.md` 還是會在 Jupyter 中以 `.md` 檔存檔，要轉換成 `.ipynb` 文件請另存新檔。