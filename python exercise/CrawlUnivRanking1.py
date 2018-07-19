#e20.1CrawUnivRanking.py
import requests
from bs4 import BeautifulSoup
allUniv=[]
def GetHTMLText(url):
    try:
      r=requests.get(url,timeout=30)
      r.raise_for_status()
      r.encoding='utf-8'
      return r.text
    except:
      return ""
def fillUnivList(soup):
    data=soup.find_all('tr')
    for tr in data:
      ltd=tr.find_all('td')
      if len(ltd)==0:
         continue
      singleUniv=[]
      for td in ltd:
        singleUniv.append(td.string)
      allUniv.append(singleUniv)
def writeUnivList(num):
    fo=open(r'C:\Users\lanxiuting\Desktop\Learning-python\UnivRanking.txt', 'w')
    Ls=str(allUniv)
    fo.writelines(ls)
    fo.seek(0)
    for line in fo:
        print(line)
    fo.close()
def main(num):
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=GetHTMLText(url)
    soup=BeautifulSoup(html,"html.parser")
    fillUnivList(soup)
    writeUnivList(num)
main(10)
