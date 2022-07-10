# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:54:45 2022

@author: medici
"""

key = 'WNL596OLQCP7023TCKJPB2VR1HJ'

import requests
import pandas as pd 
from bs4 import BeautifulSoup
import xmltodict
import json

pd.read_excel('/Users/snoo/enterprise/직종 코드.xls').to_csv('/Users/snoo/enterprise/직종코드1.csv',encoding='utf-8')
pd.read_csv('/Users/snoo/enterprise/직종코드1.csv',encoding='utf-8')
url = 'http://openapi.work.go.kr/opi/opi/opia/wantedApi.do?authKey=WNL596OLQCP7023TCKJPB2VR1HJ&callTp=L&returnType=XML&startPage=1&display=100000&occupation=134102'

res = requests.get(url)
text = res.text
text 
soup = BeautifulSoup(text,'lxml-xml')
soup.find_all(c_info[0])[1]
soup.find(c_info[0])

c_info = ['company','title','minEdubg','sal','basicAddr','holidayTpNm','career','regDt','closeDt']

worknet = pd.DataFrame(columns=['회사명','모집내용','학력','연봉','주소','근무형태','경력','지원시작일','지원마감일'])

for i in range(int(soup.find('total').text)):
    append_list = []
    for j in range(len(c_info)):
        append_list.append(soup.find_all(c_info[j])[i].text) 
    print(append_list)
    worknet = worknet.append(pd.Series(append_list,index=worknet.columns),ignore_index=True) 
    j=0
    print(i)

worknet.to_csv('/User/snoo/enterprise/worknet_df.csv',index=False)
