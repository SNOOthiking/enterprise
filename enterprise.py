# -*- coding: utf-8 -*-
"""
기업 구인구직 시각화 (데이터 분석 파트) 3줄요약  
1. 워크넷 api , 잡코리아 api를 이용해서 기업 정보 데이터 분석 쪽인 기업으로만 크롤링하기 
2. 크롤링 한 데이터를 전처리 컬럼 제거 방향으로 (중복 제거)
3. 데이터화 하면 테블로우 이용해서 시각화 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import rc 
rc('font',family='AppleGothic')
data_manpower = pd.read_csv('/Users/snoo/enterprise/data_manpower.csv',encoding='cp949')
data_manpower= data_manpower.T
data_manpower.columns = data_manpower.iloc[0,:]
data_manpower =data_manpower.drop('데이터직무별(1)',axis=0)
data_manpower.index.name = '년도'

data_manpower.columns.name = ''
data_manpower

plt.bar(data_manpower.index,data_manpower['전체'])
plt.bar(data_manpower.index,data_manpower['데이터직무'])
plt.title('년도별 데이터관련 인력') 