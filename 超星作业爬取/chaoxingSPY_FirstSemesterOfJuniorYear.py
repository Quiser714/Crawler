import os
import sys
import time

import requests
from bs4 import BeautifulSoup as bs

__consola__ = sys.stdout


def rewriteCookie():
    with open('cookie', 'w') as f:
        sys.stdout = __consola__
        f.write(input('cookie过期，粘贴新的cookie到这里，然后重启：'))


def titTxtParser(tittxt: bs):
    p = tittxt.find('p', attrs={'class': 'clearfix'})
    a = p.find('a', attrs={'title': True})
    title = a['title']

    spans = tittxt.find_all('span', attrs={'class': 'pt5'})
    startTime = spans[0].text
    endTime = spans[1].text
    status = spans[2].find('strong').text.strip()

    return title, startTime, endTime, '作业状态：'+status


def spyder(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Mobile Safari/537.36'
    }
    with open('cookie', 'r') as f:
        headers['cookie'] = f.readline()
    req = requests.get(url, headers=headers).text
    page = bs(req, 'html.parser')

    headTitle = page.find('head').find('title').text
    print(headTitle, '\n')
    titTxts = page.find_all('div', attrs={'class': 'titTxt'})
    for t in titTxts:
        # print(titTxtParser(t))
        l = titTxtParser(t)
        for i in l:
            print(i)
        print('')
    print('\n*************\n')


def main():
    urlList = [
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32653188&courseId=214845178&isdisplaytable=2&mooc=1&ut=s&enc=fdabd5bb11eade2794d2864b85f3a6d5&cpi=66855220&openc=c6820a3dea7b5a97fffbf4e6fe98380a',
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32653179&courseId=214845175&isdisplaytable=2&mooc=1&ut=s&enc=6e80a929f8c1029ba298253328e50ca1&cpi=66855220&openc=e02b28b031a8baa00d796aeb3d32d202',
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32514531&courseId=214793854&isdisplaytable=2&mooc=1&ut=s&enc=219e29936f7da9a5951ee13e0159747c&cpi=66855220&openc=85cb38d67917aecbb6393adb0825f2d8',
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32514498&courseId=214793841&isdisplaytable=2&mooc=1&ut=s&enc=1cc9be3b9d1181080a9182e7e126832d&cpi=66855220&openc=03189c9acb8054dd1f23e29d62a4267a',
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32415808&courseId=214757407&isdisplaytable=2&mooc=1&ut=s&enc=62bf7a85ba9de017122ae34bb3dbae0a&cpi=66855220&openc=87405bed7051ab4523567ccdced04b13',
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32415654&courseId=214757367&isdisplaytable=2&mooc=1&ut=s&enc=4292a84ec0ac1ea923d1b17a2ab4b179&cpi=66855220&openc=65d4fe0cc48fa2f4ac55eec29ceed154',
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32197597&courseId=214671201&isdisplaytable=2&mooc=1&ut=s&enc=e586bd3aef751cba2d526cecbbeba0c7&cpi=66855220&openc=884e7668772f30399498eda8b29ae286',
        'https://mooc1-1.chaoxing.com/work/getAllWork?classId=32197489&courseId=214671158&isdisplaytable=2&mooc=1&ut=s&enc=631b4adbf234c75cb6b89d310a53fad2&cpi=66855220&openc=f184020dfb177643271a72239c4f2410'
    ]
    with open('{}.txt'.format(time.strftime("%Y-%m-%d", time.localtime())), 'w', encoding='utf8') as todayF:
        sys.stdout = todayF
        for i in urlList:
            spyder(i)
        fileName = todayF.name
    os.system('notepad E:\\QSpider\\Qspi_chaoxing\\{}'.format(fileName))


if __name__ == '__main__':
    main()
