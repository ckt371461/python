# 紙彈簧彈力係數探討

210 19 陳冠廷

## 摘要:

本文旨在探討在不同作用力下所造成紙彈簧彈力係數改變的現象。經由實驗我們看到彈力係數會隨著施力的上升而增加，這與我們在高中時所學到的虎克定律有所不同，為了解釋此現象，我們參考了材料力學中的剪力模型，並做出一種推測，藉此解釋此現象。

## 研究動機:

我們想了解紙彈簧是否符合虎克定律，於是進行了一系列的實驗。

## 實驗器材:

* 彈簧秤
* 不同材質的紙
* 黏著劑
* 剪刀

![](https://i.imgur.com/l0wjPmG.jpg)


## 實驗設計:

對於不同材質的紙彈簧，在單一或並聯的狀態下，加以不同的力(以彈簧秤計數)拉伸時，對其彈力係數產生的改變及影響。

![](https://i.imgur.com/DML9zTd.jpg)

---

紙質(由左到右):a-b-c

![](https://i.imgur.com/7BJjhvH.jpg)
 
紙質(由左到右):c1-c2-c3

![](https://i.imgur.com/hWHL5Zr.jpg)

## 研究數據:

![](https://i.imgur.com/zS6lL6o.png)

![](https://i.imgur.com/xJYLXlZ.png)

![](https://i.imgur.com/PczytMB.png)

## 實驗分析

由實驗數據中可看到，紙彈簧的彈力係數會隨施力的變大而增加，這不符合虎克定律，針對這個問題，我們想探究這個現象產生的原因，於是我們上網查詢了資料，發現利用剪力模數及楊氏模數好像能解釋這個現象，對此，我們做出了以下分析:

標準的虎克定律為: $k=\dfrac{F}{\Delta x}$，$F$代表施力，而$\Delta x$代表伸長量

課本中的彈向係數$k$通常為常量，但在實驗中卻發現彈性係數會上升，這無法用標準的虎克定律描述，經查詢後我們發現下列彈性力學中的「等向性材料的應力與應變關係式」似乎能描述此一現象:

$\begin{aligned}\epsilon _{x}={\frac  {1}{E}}\left[\sigma _{x}-\nu \left(\sigma _{y}+\sigma _{z}\right)\right],\quad \gamma _{{yz}}={\frac  {1}{G}}\tau _{{yz}}\\\epsilon _{y}={\frac  {1}{E}}\left[\sigma _{y}-\nu \left(\sigma _{z}+\sigma _{x}\right)\right],\quad \gamma _{{zx}}={\frac  {1}{G}}\tau _{{zx}}\\\epsilon _{z}={\frac  {1}{E}}\left[\sigma _{z}-\nu \left(\sigma _{x}+\sigma _{y}\right)\right],\quad \gamma _{{xy}}={\frac  {1}{G}}\tau _{{xy}}\\\end{aligned}$

$\epsilon$代表應變，$\sigma$代表應力，$E$代表楊氏模數，$\nu$代表蒲松比，$G$代表剪切模數，$\gamma$代表剪應變，$\tau$代表剪應力

剪切模數的定義為: $G=\dfrac{\tau}{\gamma}$

假如$\tau$上升較多而$\gamma$上升較少時，剪切模數$G$便會上升

在均勻等向性材料中，剪切模數G、楊氏模數E 和蒲松比$\nu$它們之間存在以下關係： $E=2G(1+\nu)$
我們認為紙彈簧的蒲松比$\tau$應為常數，因此當$G$上升時，$E$也會跟著上升

由於楊氏模數的定義為: $E=\dfrac{\sigma}{\epsilon}$，這和虎克定律: $k=\dfrac{F}{\Delta x}$可以對應起來，所以我們推論:

彈力係數的上升是因$F$(對應到$\sigma$)上升時，$\tau$的上升較$\gamma$的上升顯著而導致的結果。

## 結論

從上述的實驗和分析過程中，我們學到:即使像虎克定律這樣簡單的公式，背後其實也隱藏著許多複雜的因素，虎克定律只是一種理想的簡化模式，若要建立更精確的模型，就必須引入更多的數學與物理法則。




## 參考資料:

1. 樹姐姐愛手工:親子摺紙:超級簡單又好玩的紙彈簧。每日頭條。民107年11月15日，取自:https://kknews.cc/zh-tw/news/g9am22m.html
2. 紙彈簧。國立台中教育大學:科學遊戲實驗室。取自:
http://scigame.ntcu.edu.tw/paper/paper-007.html
3. 遁走紙彈簧。國立台中教育大學:科學遊戲實驗室。取自:
http://scigame.ntcu.edu.tw/paper/paper-018.html
4. 方宣燁、陳威豪、黃欣怡、高雅。簡易螺旋紋和紙彈玩具的研究與製作。第32屆全國中小學科展物理科初小組，取自:
https://twsf.ntsec.gov.tw/activity/race-1/32/pdf/32s/001.pdf
5. 吳彥忞、呂浩宇。以彈簧系統模擬固體內原子振動行為。第59屆中小學科學展覽會物理與天文學科高中組，取自:
https://twsf.ntsec.gov.tw/activity/race-1/59/pdf/NPHSF2019-051815.pdf
6. 百「褶」不屈。第54屆中小學科學展覽會物理科高中組，取自:中華民國第54 屆中小學科學展覽會作品說明書
www.tntcsh.tn.edu.tw › ...
7. [維基百科-彈性力學](https://zh.wikipedia.org/wiki/%E5%BC%B9%E6%80%A7%E5%8A%9B%E5%AD%A6?fbclid=IwAR3YYiFTVRK73hzQ_p7CAKYA4A_nhcp2_tbVW8VCbURJrD32z8L76HHg_9s)
8. [維基百科-剪切模量](https://zh.wikipedia.org/wiki/%E5%89%AA%E5%88%87%E6%A8%A1%E9%87%8F?fbclid=IwAR15i19kt6P6GeVVaoqhVP0OL8enwLu-yNLSAEmdBiPQoJDBCOYuVQOXod8)
9. [維基百科-蒲松比](https://zh.wikipedia.org/wiki/%E6%B3%8A%E6%9D%BE%E6%AF%94) 