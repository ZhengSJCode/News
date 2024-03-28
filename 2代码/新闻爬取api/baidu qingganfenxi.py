# -*- coding=utf-8 -*-

from aip import AipNlp
import news_origin
import csv,random
import time
# 这里不能动!!!!
# 这里不能动!!!!
def newsCrawler(start=9099999,end=9109999,step=1):
    """ 你的 APPID AK SK """
    APP_ID = '23408532'
    API_KEY = 'dOkSxjXpoaGG09DEoptq8nhu'
    SECRET_KEY = 'PUxx5thGeDK6fxGbo88dOGAOEe1KmYMx'

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    # text = "天津是现代工业文明发祥地，有完备的产业体系。在工业全部41个大类中，天津占39个；207个中类里，天津占191个。”天津市工业和信息化局局长尹继辉近日在接受记者采访时表示，发展先进制造业不但是天津的看家本领，更是“十四五”期间天津“在危机中育先机，于变局中开新局”的最大比较优势。天津在制定“十四五”规划和2035年远景目标的过程中，把实体经济作为发展之基，确立“以制造业立市”的发展路径，提出以科技创新为第一动力，全力推动传统支柱产业向高端化迈进。天津市委指出，要紧紧抓住推进京津冀协同发展、“一带一路”建设等重大国家战略的机遇，充分发挥拥有独特的区位、产业、港口、交通等优势，拥有改革开放先行区、金融创新运营示范区、自由贸易试验区、国家自主创新示范区等先行先试的优越条件，在构建以国内大循环为主体、国内国际双循环相互促进的新发展格局中，找准定位、发挥优势，再创天津新辉煌。"

    # 收集新闻 默认值为9383582
    # data=news_origin.search_news(9383582)
    #
    # # print(data)
    # """ 调用情感倾向分析 """
    # text=data['contentNoTag']
    # # print(client.sentimentClassify(text))
    # items=client.sentimentClassify(text)['items']



    with open('20200301-20200327.csv', 'a', newline='') as csvfile:
      #设置标题
      fieldnames=['id',
                  'source',
                  'title',
                  'keyword',
                  'freshTime',
                  'topicName',
                  'contentNoTag',

                  'positive_prob',
                  'confidence',
                  'negative_prob',
                  'sentiment'
                  ]
      writer=csv.DictWriter(csvfile,fieldnames=fieldnames)

      # 注入标题
      writer.writeheader()


      for i in range(start,end,step):
            try:
              # 收集新闻 (默认值为9383582)
              data = news_origin.search_news(i)


              # """ 调用情感倾向分析 """
              if data:
                  text = data['contentNoTag'][:1000]
                  # print(text)

                  # 情感分析返回值
                  baidu_text = client.sentimentClassify(text)
                  # print(baidu_text)
                  items = baidu_text.get('items')
                  print(items)



              time.sleep(random.randint(0,2))

              # 写入数据
              if items and data:
                  writer.writerow(
                      {
                          # 从data中获取
                          'id':             data.get('id'),
                          'source':         data.get('source'),
                          'title':          data.get('title'),
                          'keyword':        data.get('keyword'),
                          'freshTime':      data.get('freshTime'),
                          'topicName':        data.get('topicName'),
                          'contentNoTag':   data.get('contentNoTag'),

                          # 从items中获取
                          'positive_prob':  items[0].get('positive_prob'),
                          'confidence':     items[0].get('confidence'),
                          'negative_prob':  items[0].get('negative_prob'),
                          'sentiment':      items[0].get('sentiment')
                      })
            except:
                print('error')
# 这里不能动!!!!
if __name__ == '__main__':
    # 新闻爬虫!!!
    # 改这里!!!!!
    newsCrawler(start=9120000,end=9140000,step=1)
    # start是第几条新闻开始
    # end是结束
    # step是每次加1

    # 9110000-9130000郑
    # 9130000-9160000罗