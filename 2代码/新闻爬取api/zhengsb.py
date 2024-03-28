import requests
import re,json
url = "https://m.chinanews.com/wap/detail/chs/zw/9383582.shtml"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Accept': 'application/json, text/plain, */*',
  'accessToken': '2320fc8e5cc7cdbf516755352cf73267',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/87.0.664.75',
  'appKey': 'CNSAPP',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://m.chinanews.com/wap/detail/chs/zw/9383581.shtml',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6',
  'Cookie': '__jsluid_h=5421499b4a415bf0e33294dacc0e5bf9; __jsluid_s=63b293fcea5e9282f7025a8461b078e3; cnsuuid=c3fcd5aa-5484-599f-d95c-e3f57efcec389846.443503798526_1610254739921; Hm_lvt_0da10fbf73cda14a786cd75b91f6beab=1610254822,1610255128'
}

response = requests.request("GET", url, headers=headers, data=payload)


# print(response.text)

# 数据清理(正则表达式选取json内容)
re_data_str = re.findall('{"home":.*}}', response.text)[0]
# print(re_data_str)

js_data=json.loads(re_data_str)

nn=js_data.get('detail').get('item').get('contentNoTag')
print(nn)

