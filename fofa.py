# -*- coding: UTF-8 -*-
import base64
import time
import requests
from lxml import etree

#搜索内容
search_data = '填写你的fofa语法，如：body="**网络科技"'

#登录cookie
headers={
'cookie': '填写cookie'
}  #这里是因为我没有会员，所以需要cookie

#构造网址
for yeshu in range(1,6):
    search_data_bs = str(base64.b64encode(search_data.encode('utf-8')),'utf-8')

    print('正在读取第'+ str(yeshu) + '页')
    url = 'https://fofa.so/result?qbase64=' + search_data_bs + '&page=' + str(yeshu) + '&page_size=10'
    print(url)
    try:
        #print(url)
        #开始访问，返回数据
        result = requests.get(url,headers=headers,timeout=1).content
        #print(result)
        #对搜索结果进行提取
        soup = etree.HTML(result)
        ip_data = soup.xpath('//a[@target="_blank"]/@href')

        #将IP进行保存
        ip = '\n'.join(ip_data)
        print(ip)
        with open(r'IP返回所存放的文件地址，如：result/weblogic2.txt', 'a+') as f:
            f.write(ip)
            f.close()
    except Exception as e:
        pass