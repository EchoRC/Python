#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
import bs4
import pymysql
import time
# 打开数据库连接
db = pymysql.connect("101.132.195.63", "rc", "rc123", "pydb", charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
print('start')
m = 1
while m <= 73:

    # 要抓取的目标页码地址
    # url = 'http://list.mogujie.com/book/accessories/10061955?mt=12.18940.r153160.24443&acm=3.mce.1_10_188k2.18940..iOPIAqQwjmQFc.pos_0-m_192141-sd_119-mf_15261_944839-idx_0-mfs_46-dm1_5000&ptp=1._mf1_1239_15261.0.0.mVsdTMSI'
    # url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,' + '%d' % m + \
        '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    print('url is :' + url)
    m = m + 1
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

    texts = content.find_all('div', class_='el')

    jobinfo = texts[17:len(texts)]
    # print(jobinfo)
    for infos in jobinfo:
        t1info = infos.find_all('p', class_='t1')
        t2info = infos.find_all('span', class_='t2')
        t3info = infos.find_all('span', class_='t3')
        t4info = infos.find_all('span', class_='t4')
        t5info = infos.find_all('span', class_='t5')
        a, b, c, d, e, f, g, h = '0', '1', '2', '3', '4', '5', '6', '51job'
        for t1 in t1info:
            t1hr = t1.find('a')
            t1strs = t1hr['href']
            e = t1strs
            # c = t1hr.text.split()
            for cs in t1hr.text.split():
                c = cs
            print(c)
            # print(t1strs + '---------' + t1hr.text)
        for t2 in t2info:
            t2hr = t2.find('a')
            t2strs = t2hr['href']
            f = t2strs
            b = t2hr.text
            # print(t2strs + '---------' + t2hr.text)
        for t3 in t3info:
            d = t3.text
            # print('---------' + t3.text)
        for t4 in t4info:
            # print('---------' + t4.text)
            g = t4.text
        for t5 in t5info:
            # print('---------' + t5.text)
            a = t5.text
            cursor.execute('insert into wuyoujob (public_date, companyname, title, work_add,job_url,company_url,salary,source) values(%s,%s,%s,%s,%s,%s,%s,%s)', (
                a, b, c, d, e, f, g, h))

            # 提交到数据库执行
            db.commit()
        # sleep(5)
print('end')
