import os
import re
import sys
import threading
import time
import requests
from bs4 import BeautifulSoup as bs


class SpyForMagnet:
    def __init__(self):
        super().__init__()
        self.mainPage = r'https://www.sugarfh.vip/page/'
        self.pageNum = 1
        
        self.TextFile = None
        print('{:20}'.format('番号'), "磁力链", file=self.TextFile)
        self.TextLock = threading.Lock()

        self.threads = []

    def getHtml(self, url):  # 返回指定网页的Html
        headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
        }
        req = requests.get(url, headers=headers)
        html = bs(req.text, 'html.parser')
        return html

    def getItemHref(self, html) -> list:  # 返回主页某一页中嵌入的网页列表
        HrefList = []
        articles = html.find_all('article')
        
        if len(articles) != 0:
            for article in articles:
                href = article.find_all(
                    'a', attrs={'class': 'wp-post-image-link'})[0]['href']
                HrefList.append(href)
        return HrefList

    def getMagnet(self, html) -> str:  # 返回页面包含的磁力链
        html = str(html)
        # with open('index.html', 'w', encoding='utf8') as f:
        #     print(html, file=f)
        reg = re.compile('href="magnet.*?"')
        magnet = reg.findall(html)
        if len(magnet) >= 1:
            magnet = magnet[0][6:-1]
            return magnet
        else:
            print('No Magnet Found!')
            print(magnet)
            return 'none'

    def getOnePage_ForOneThread(self, pageNum):
        pageList = self.getItemHref(self.getHtml(
            self.mainPage + str(pageNum) + '/'))
        magnetList = []
        for page in pageList:
            magnetList.append(self.getMagnet(self.getHtml(page)))
        self.TextLock.acquire()
        for i in range(len(pageList)):
            print('{:20}'.format(pageList[i][24:-1]),
                  magnetList[i], file=self.TextFile)
        self.TextLock.release()

    def run(self):
        self.TextFile = open('MagnetListFile.txt', 'w', encoding='utf8')
        while self.pageNum < 326:
            if threading.activeCount() == 1:
                for i in range(20):
                    th = threading.Thread(
                        target=self.getOnePage_ForOneThread, kwargs={'pageNum': self.pageNum})
                    self.threads.append(th)
                    th.start()
                    print(self.pageNum)
                    self.pageNum += 1
            else:
                time.sleep(3)

        while threading.activeCount() == 1:
            self.TextFile.close()
            for thread in self.threads:
                thread.join()
            return
        else:
            pass


if __name__ == '__main__':
    MySpy = SpyForMagnet()
    MySpy.run()
