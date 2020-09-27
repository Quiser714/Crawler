import re
import os
import sys
import threading
import urllib.request


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Mobile Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf8')
    return html


def downloadImg(urlList):
    if not os.path.exists('images'):
        os.mkdir('images')
    ths = []
    for url in urlList:
        th = threading.Thread(target=urllib.request.urlretrieve, kwargs={
                              'url': url, 'filename': './images/'+url[-20:]})
        ths.append(th)
        th.start()
        print(th.name, 'start')
    for th in ths:
        th.join()
        print(th.name, 'join')


def getImgList(page):
    URL = r'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=6823116&page_num={}&page_size=30&biz=all'.format(
        page)
    html = getHtml(URL)
    reg = re.compile('"https://i0.*?"')
    tmpList = reg.findall(html)
    imgList = []
    for i in tmpList:
        imgList.append(i[1:-1])
    lengthOfImgList = len(imgList)  # == a*10 + b
    a = lengthOfImgList//10
    b = lengthOfImgList % 10
    for i in range(a):
        downloadImg(imgList[i*10:i*10+10])
    downloadImg(imgList[-b:])


if __name__ == '__main__':
    threads = []
    for page in range(11):
        th = threading.Thread(target=getImgList, args=(page,))
        threads.append(th)
        th.start()
    for th in threads:
        th.join()
