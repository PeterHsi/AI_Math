---
tags: Jupyter, Python
---

# 多 Kernel 安裝教學

[TOC]

## Python X.X.X 多環境

本節主要參考：[Jupyter Notebook 使用技巧彙整：建置不同程式語言的核心](https://medium.com/pyradise/jupyter-notebook-tricks-kernels-9350502ccb69)(by Yao-Jen Kuo)

### 安裝環境

Anaconda 本身提供多版本 python 環境，其安裝指令如下

```shell=
conda create -n 你想要命名的環境名稱 python=版本號
```

例如我今天要安裝一個叫做 py36 的 python 3.6 版環境，就是：

```shell=
conda create -n py36 python=3.6
```

版本號可以詳細或粗略指定，例如你可以指定到 2 這樣單獨的數字，或是細道諸如 3.7.1 這樣都可以。

請記住這個環境很多 package 是不會從 anaconda 的 base 環境(預設安裝的對象)帶進來，需要進入環境重新安裝。

### 啟用環境並安裝 ipykernel

先啟用環境

```shell=
# 啟用環境 Windows 版
activate py36

# 啟用環境 Mac/Linux 版
source activate py36
```

然後安裝 ipykernel

```
pip install ipykernel
python -m ipykernel install --user --name python3.6 --display-name "Python 3.6"
```

在 --name 後面接的你要安裝的 kernel 名稱(跟之前環境名稱不同，名稱可一樣可不一樣，兩者是不同的東西)，而 --display-name 則是在 Jypyter 環境下 UI 顯示的名稱，若不放的話就會直接顯示 kernel 的名稱。

## R 核心

請在命令列進入 R (儘量不要用 RStudio，有時會導致安裝 package 失敗)，安裝 IRkernel package：

```shell=
R
install.packages('IRkernel', repos = 'https://cloud.r-project.org/')
IRkernel::installspec(user = FALSE)
```

(至於 R 的安裝就不教學了，單純從官網下載執行安裝程式就好了。)

## Juila 核心

類似 R

```
julia
using Pkg
Pkg.add("IJulia")
```

---

安裝完成後你的 Jupyter 就會有很壯觀的景象：

![](https://i.imgur.com/wnAtLkL.png)

假如我們要移除掉 kernel 該怎麼辦呢？

# 移除不要的 Kernel (與 anaconda 環境)

## Kernel 移除

使用如下指令反安裝 kernel

```shell=
jupyter kernelspec uninstall kernel名稱
```

假如忘記名稱怎麼辦？使用如下指令查詢已安裝的 kernel

```shell=
jupyter kernelspec list
```

## anaconda 環境移除

調出環境列表：

```shell=
conda env list
```

環境移除：

```shell=
conda env remove --name 我想要移除的環境名稱
```

更多關於環境管理的教學(例如移除某環境的 package 等等)，可以參考這篇文章：[用conda建立及管理python虛擬環境](https://medium.com/python4u/%E7%94%A8conda%E5%BB%BA%E7%AB%8B%E5%8F%8A%E7%AE%A1%E7%90%86python%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83-b61fd2a76566)(by Steven Lo)
