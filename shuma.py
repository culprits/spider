import requests,re
from bs4 import BeautifulSoup

url = 'http://www.shuma.in/price/'

def Gethtml(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    date = soup.find('div',{'class':'span7'}).get_text()
    if ':' in date:
        date = date.replace(':','-')
    if '最后更新时间： ' in date:
        date = date.replace('最后更新时间： ','手机行情')
    list = soup.find('div',{'class':'row'}).find_all('div',{'class':'span2'})
    for item in list[10:-1]:
        price = item.get_text()
        Down_price(price,date)

def Down_price(price,date):
    with open('{}.txt'.format(date),'a',encoding='utf-8') as f:
        f.write(price + '\n')
        f.close()


if __name__ == '__main__':
    Gethtml(url)
    print('爬取完毕！！！！')