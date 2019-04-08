# 2019 Spring NCTS Course - Python ML & AI Intro. (Student Works)

這是「Python 機器學習與人工智慧入門」課程學生 [Wei-Pin Hsiao](https://www.facebook.com/weipin.hsiao.1) 的公開成果，所有成果皆放在 [AI_Math/student_hwp_work/](student_hwp_work) 資料夾下供交流學習使用，其餘皆為老師在 GitHub 上公開分享之課程檔案

## 作業

目前已公開作業如下：

- [HW1-1](student_hwp_work/20190222%20NCTS%20AI%20MATH%20-%20HW1_1.ipynb)：繪圖作業，嘗試繪出 Iris data 的散布圖
- [HW1-2](student_hwp_work/20190225%20NCTS%20AI%20MATH%20-%20HW1_2.ipynb)：學生嘗試熟悉 Python 基礎語法，由於 1-1 已經自行嘗試過迴圈、讀入外部資料檔，故此作業嘗試熟悉自訂義函數與呼值方式，並試圖僅以型別更動函數、基本數學運算符、find 函式，建構自訂義四捨五入函數
- [HW2-1](student_hwp_work/20190309%20NCTS%20AI%20MATH%20-%20HW2_1.ipynb)：利用 ipywidgets 的 interact，來製作中央極限定理的互動教學小程式
- [HW3-2](student_hwp_work/20190320%20NCTS%20AI%20MATH%20-%20HW3_2.ipynb)：熟悉 NumPy，由於 NumPy 可以執行矩陣運算，故嘗試利用矩陣運算自行撰寫 Fuzzy C-Mean 演算法，並嘗試比較相同資料跟相同精度下，自行撰寫之函數是否比公開 Package 還快
- [HW4-1](student_hwp_work/20190324%20NCTS%20AI%20MATH%20-%20HW4_1.ipynb)：熟悉 Pandas，由於個人希望可以取得房地產實價登錄網的往期批次資料檔(為壓縮檔)，故比課堂老師所教授之方法多增加了利用程式下載官方壓縮檔以及讀取壓縮檔內資料表的程式
- [HW5-1](student_hwp_work/20190404%20NCTS%20AI%20MATH%20-%20HW5_1.ipynb)：線性迴歸分析，使用美國資料分析各地區人均所得狀況，由於為多變數迴歸模型，稍微採用了比較不同呈現方式與分析模組

## 上課筆記

其中個人筆記與課外學習放置於 [AI_Math/student_hwp_work/Note and Learn/](https://github.com/PeterHsi/AI_Math/tree/master/student_hwp_work/Note%20and%20Learn)

## 工具使用心得分享

有關已發表公開之 Markdown 學習資料如下：

- [.md Guide](https://hackmd.io/p/Byk-LDoDV#/)：講述一些 markdown 文檔的使用方式，主要集中在做學習資料跟分享報告上
  - 其原始為報失敗的 [3/8 閃電秀](https://hackmd.io/p/SyrVwwF8V#/)
  - 更多有關於如何用 Rmarkdown 的內容個人曾經另外分享過 [快速上手數學報告](https://hackmd.io/c/HyJ0JKdhX/) 系列文，有興趣者可以參考  
- [JupyterLab 調整懶人包](https://hackmd.io/p/BkWDdZOwN#/)
  - 詳細學習筆記請至 [Jupyter 校調學習日誌](https://hackmd.io/c/Sy_DHe8DE/) 參考，由於目前個人正在拚論文當中，暫停更新。

(以下為課程原始說明檔)

---

![課程圖示](images/course_title.jpeg)

# Python 機器學習與人工智慧入門

這裡是「Python 機器學習與人工智慧入門」課程相關資訊、程式碼等的網頁。目前 2019 年 2 月 22 日起在台大理論中心開課中。上課時間是每週五 9:10--12:10, 第三節課是演習課。

【線上直播連結】
http://bit.ly/aimath_video

直播都會錄影。

## 修課作業

如果是修課同學, 請一定要加入 Facebook 社團:

【政大魔法程式家】
https://www.facebook.com/groups/159902691120219/

作業直接在上面回應。正式修課同學不要忘了回應要加上 `[NCTS]` 字眼, 方便登記成績。

## 期中個人小專題

期中每位同學要交一個小專題! 不一定要很難很大, 主要是在不斷的作業中, 看看有沒有什麼有趣的想法。

## 期末專題

用深度學習解決一個實務上的問題! 這是小組作業 (堅持要個人也可以), 我們會讓大家提專題的計畫, 你可以招集對這個問題有興趣的同學一起來!

## 閃電秀

每週最多五位同學, 可以參加「閃電秀」。自選一個小小的主題, 比方說 Python 小技巧。每位同學最長不超過五鐘! 參加閃電秀的同學, 我們「真人教室」第一排有為大家準備的保留席!