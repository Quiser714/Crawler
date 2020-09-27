# bilibili壁纸站
在[B站网页端](http://www.bilibili.com)的底部有一个[壁纸站](https://space.bilibili.com/6823116#/album)，适合用来写爬虫练练手。
<br />
<img src="https://miro.medium.com/max/875/1*Vl3UZh7liI4RKj4Bv_eYqA.png" height="200" width="460">
-------
b站页面加载是动态的，无法直接从获取到的HTML中获得页面信息，需要抓包，这就很蛋疼。
不知道有什么抓包的好方法没有，只能打开F12去一个一个找，写这个爬虫最花时间的地方就是这儿。
返回的界面信息是JSON，由于目前没有系统的学习JSON，这里就直接用正则表达式去匹配了。
-------
对于多线程的资源调配以一个很傻逼的方式写完了（因为用锁总是不知道哪里出问题）
