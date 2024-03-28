import requests, re
from lxml import etree
from fake_useragent import UserAgent

ua = UserAgent()
retnews_url = []

# 请求的网址

# url = "http://sou.chinanews.com/search.do?q=sars&ps=100&start=100&type=&sort=pubtime&time_scope=0&channel=all&adv=1&day1=&day2=&field=&creator="
url='http://sou.chinanews.com/search.do?q=sars&ps=10&start=0'


payload={}
headers = {
  'Host': 'sou.chinanews.com',
  'Connection': 'keep-alive',
  'Cache-Control': 'max-age=0',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# 用etree的方法
selector = etree.HTML(response.content)
print(response.content)
url = selector.xpath('//*[@id="news_list"]/table[.]/tbody/tr[1]/td[2]/ul/li[1]/a/@href')

# url=re.findall('<a href="(http://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|])" target="_blank">',response.text,re.S)


retnews_url = retnews_url + url

print(retnews_url)
