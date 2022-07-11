# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:23:39 2022

@author: medici
"""

import json
import requests
import pandas as pd
import datetime
key = 'db9a2d79eb9fdaac9ca5f3fe6f93e5de'

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
    headers = {"Authorization": "KakaoAK "+key}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address']

    return float(match_first['y']), float(match_first['x'])


worknet = pd.read_csv('C:/SEONWOO/enterprise/worknet_df.csv')

worknet['주소']
coord = []
for i in range(len(worknet)):
    coord.append(getLatLng(worknet.loc[i]['주소']))
len(coord)

coord = list(map(lambda x: str(x).split('(')[1].split(')')[0], worknet['좌표']))
coord_x = list(map(lambda x: str(x).split(',')[0], worknet['좌표']))
coord_y = list(map(lambda x: str(x).split(',')[1], worknet['좌표']))
worknet['위도'] = coord_x
worknet['경도'] = coord_y
worknet.drop('좌표', axis=1, inplace=True)
worknet.columns


worknet[worknet['근무형태'].isna()]

worknet.loc[38]['근무형태'] = '주5일근무'
worknet.loc[42]['근무형태'] = '주5일근무'
worknet['지원마감일'][1].replace('채용시까지  ', '')
len(worknet['지원마감일'][0])

datetime.datetime.strptime(
    worknet['지원마감일'][0], '%y-%M-%d').strftime('%Y-%M-%d')
last_d = list(map(lambda x: x.replace('채용시까지  ', ''), worknet['지원마감일']))
worknet['지원마감일'] = last_d
last_d1 = list(map(lambda x: datetime.datetime.strptime(
    x, '%y-%M-%d').strftime('%Y-%M-%d'), worknet['지원마감일']))
first_d1 = list(map(lambda x: datetime.datetime.strptime(
    x, '%y-%M-%d').strftime('%Y-%M-%d'), worknet['지원시작일']))

worknet['지원마감일'] = last_d1
worknet['지원시작일'] = first_d1
# worknet.to_csv('C:/SEONWOO/enterprise/worknet_df1.csv') 윈도우 기반

worknet = pd.read_csv(
    '/Users/snoo/enterprise/worknet_df1.csv', index_col='Unnamed: 0')

worknet.columns
int('100,399,659,000'.replace(',', ''))/5000
10/20079932


2000000 * 5000
10000000000


len(worknet)
worknet['주소']
jeju = pd.read_csv('C:/SEONWOO/jeju/jeju_Final_df2.csv', encoding='cp949')
jeju.info()

jeju.isna().sum()
jeju.loc[4211]['소재지전체주소']

for i in jeju[jeju['소재지전체주소'].isna()].index:
    jeju.loc[i]['소재지전체주소'] = jeju.loc[i]['도로명전체주소']

jeju.isna().sum()

getLatLng('제주특별자치도 제주시 오등동 10-14번지')

# 좌표는 소제지 전체주소로 딸까
aaa