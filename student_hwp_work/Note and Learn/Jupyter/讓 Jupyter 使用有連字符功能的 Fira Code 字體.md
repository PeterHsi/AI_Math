---
tags: Jupyter, Python
---

# 讓 Jupyter 使用有連字符功能的 Fira Code 字體

> [name=Peter Hsiao][time=Thu, Mar 14, 2019 1:56 PM]

![](https://i.imgur.com/AzHHDuR.png)


Fira Code 是一個美觀的等寬字型，同時支援連字符，若有開啟編輯器的連字符功能並將字體設定為 Fira Code，一些特殊符號會更接近人類平時的閱讀習慣(例如 `>=` 會接近 $\geq$)，增加程式碼可讀性。

更多關於 Fira Code 的範例與說明，可以參考其 Github 專案：https://github.com/tonsky/FiraCode

## 在 Notebook 環境使用 Fira Code

在 .jupyter 資料夾內建立 custom 資料夾，並建立 custom.js 的文字檔，將下列 javascript 寫入。 

```javascript=
@font-face {
  font-family: 'Fira Code';
  src: url("https://cdn.rawgit.com/dunovank/jupyter-themes/1e851888/jupyterthemes/fonts/monospace/firacode/firacode.otf") format("opentype");
}

.CodeMirror {
  font-family: 'Fira Code';
  font-variant-ligatures: initial;
}

.cm-string {
    font-variant-ligatures: none;
}
```

[參考來源][ref1]


[ref1]: https://gist.github.com/mutsune/14bb6bb34679f04b76dba2de6e0f3549

## 在 Lab 環境使用 Fira Code

雖然說看官方說明是在 Advence Setting (Ctrl+\`) 中的 Text Editor 就能設定 fontFamily，但個人測試後不管用，需要安裝外掛 [@deathbeds/jupyterlab-fonts](https://github.com/deathbeds/jupyterlab-fonts)：

```shell=
# 安裝字型管理外掛(要安裝過後才才能正常裝字型外掛)
jupyter labextension install @deathbeds/jupyterlab-fonts
# 安裝外掛下的字型
jupyter labextension install @deathbeds/jupyterlab-font-fira-code
```

這個外掛可以設定單獨 .ipynb 的字型或全體 .ipynb 的字型，我們可以依此設定全體字形：在最上面的選單的 Settings ▶ Fonts ▶ Global Fonts 下可以設定

(這個外掛還有提供更多字型，可以自己安裝)
