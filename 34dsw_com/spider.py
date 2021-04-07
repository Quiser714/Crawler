import os
import httpx
from bs4 import BeautifulSoup
import re
RootWebSite = 'https://www.34ksw.com'


def getHtml(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
    }
    resp = httpx.get(url, headers=headers).content
    html = BeautifulSoup(resp, 'html.parser')
    return html


def getTextInfo(html):
    btitle = html.find('div', attrs={'class': 'btitle'})
    novelTitle = btitle.find('h1').text  # 小说名
    novelAuthor = btitle.find('i').text  # 作者
    novelDirectory = []  # 小说目录
    dictList = html.find_all('td', attrs={'class': 'L'})
    for td in dictList:
        novelDirectory.append(RootWebSite + td.find('a')['href'])
    return {'title': novelTitle, 'author': novelAuthor, 'directory': novelDirectory}


def getContent(html):
    h2 = re.findall('第.*?章.*', html.find_all('h2')[-1].text)[0]
    cont = html.find('div', attrs={'name': 'content', 'id': 'content'}).text
    return h2 + '\n' + cont


def loadNovel(url):
    novelinfo = getTextInfo(getHtml(url))
    if not os.path.exists('txt'):
        os.mkdir('txt')
    #
    with open('txt'+os.sep+novelinfo['title']+'.txt', 'w', encoding='utf8') as fp:
        # print(type(novelinfo['title']+'\n'+novelinfo['author']))
        fp.write(novelinfo['title']+'\n'+novelinfo['author'])

    for url in novelinfo['directory']:
        with open('txt'+os.sep+novelinfo['title']+'.txt', 'a', encoding='utf8') as fp:
            fp.write('\n'+getContent(getHtml(url)))


if __name__ == '__main__':
    loadNovel('https://www.34ksw.com/read/231846/')





    # with open('out.html', 'w', encoding='utf8') as fp:
    #     loadNovel('https://www.34ksw.com/read/273841/')
    #     # print(getContent(
    #     #     getHtml('https://www.34ksw.com/read/273741/75531526.html')), file=fp)
    # # for i in range(1, 273842):
    # #     getHtml(f'https://www.34ksw.com/read/{i}/')

# https://www.34ksw.com/read/273841/
