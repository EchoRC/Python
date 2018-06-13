#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
import bs4

# 要抓取的目标页码地址
# url = 'http://list.mogujie.com/book/accessories/10061955?mt=12.18940.r153160.24443&acm=3.mce.1_10_188k2.18940..iOPIAqQwjmQFc.pos_0-m_192141-sd_119-mf_15261_944839-idx_0-mfs_46-dm1_5000&ptp=1._mf1_1239_15261.0.0.mVsdTMSI'
url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# 抓取页码内容，返回响应对象
response = requests.get(url)

encod = response.encoding
# print(encod)
# 查看响应状态码
status_code = response.status_code
# print(status_code)
content = bs4.BeautifulSoup(
    response.content.decode(encod).encode(encod), "lxml")
# print(content)

texts = content.find_all('div', class_='el title')
print(texts)

test = content.find_all('p', class_='t1')
print(test)
# for qu in quots:
#     urls = qu.find_all('li')
#     for ur in urls:
#         hl = ur.find('a')
#         a = hl['href']
#         strs = re.findall(r'[^()]+', ur.text)
#         if strs and 2 == len(strs):
#             b = re.findall(r'[^()]+', ur.text)[0]
#             c = re.findall(r'[^()]+', ur.text)[1]
#             d = 'sbcl'
#             c.encode('utf-8')
#             print('name is :' + b)
#             print('code is :' + c)
#             print('url is :' + a)
#             print(d)
