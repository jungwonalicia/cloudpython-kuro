import requests
from bs4 import BeautifulSoup

#각 페이지별 회사 이름 리스트 get. 
def get_names(page):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="+str(page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    td_list = bs_obj.findAll("td", {"class":"ctg"})
#     print(td_list)
    company_names = []
    
    for td in td_list:
        company_names.append(td.find("a").text)
    
#     print(company_names)
    
    return company_names    


#각 페이지별 회사 주식가 리스트 get. 
def get_now_price(page):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="+str(page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    td_list = bs_obj.findAll("td", {"class":"number_2"})
#     print(td_list)
    
    now_price_list = []
    
    td_list_count = len(td_list)
    
    for index in range(0, td_list_count, 4):
        now_price_list.append(td_list[index].text)
    
#     print(now_price_list)
    
    return now_price_list


#1페이지의 회사명과 주식가를 가지고 와서 한번에 출력
def total_info():
    company_names = get_names()
    now_price_list = get_now_price()
    
    print("회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        print(name, "\t", price)
        
#입력한 페이지의 회사명과 주식가를 가지고 와서 한번에 출력
def total_info2(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    print(page, ":페이지>> 회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        print(name, "\t\t", price)

#입력한 페이지의 회사명과 주식가를 한번에 가지고와서 리턴        
def total_info3(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    return company_names, now_price_list

#입력한 페이지의 회사명과 주식가를 가지고 와서 파일에 저장
def total_info4(page):
    file = open(str(page) + ".txt", "w")
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    print(page, ":페이지>> 회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        file.write(name+"\t"+price+"\n")

# 1페이지부터 10페이지까지 파일 생성하는 함수 호출        
# for page in range(1, 11, 1):        
#     total_info4(page)

#파일을 읽어와서 각 줄 프린트
# file2 = open("1.txt", "r")
# for line in range(0, 10):
#     print(file2.readline())
    
#파일을 읽어와서 분리하여 프린트
# file2 = open("1.txt", "r")
# for line in range(0, 10):
#     line = file2.readline()
#     contents = line.split("\t")
#     print(contents[0])
#     print(contents[1])
 
#파일을 읽어와서 분리하여 ","를 제거후,int로 변환
# file2 = open("1.txt", "r")
# for line in range(0, 10):
#     line = file2.readline()
#     contents = line.split("\t")
#     print(contents[0])
#     print(int(contents[1].replace(",",""))+100000)
#     #int로 변환여부 확인위해 100000을 더해봄.
    
#파일을 읽어와서 분리하여 ","를 제거후,int로 변환하여 리스트로 저장/출력
name_list = []
price_list = []
file2 = open("1.txt", "r")
for line in range(0, 10):
    line = file2.readline()
    contents = line.split("\t")
    name_list.append(contents[0])
    price_list.append(int(contents[1].replace(",","")))

print(name_list)
print(price_list)
print()


#pandas로 두 개의 리스트를 하나의 DataFrame으로 생성하여 np이용 분석 예제
import pandas as pd
df = pd.DataFrame({"회사이름" : name_list, "주식가" : price_list})
print(df)
print()

import numpy as np
print("최고가", np.max(df['주식가']))
print(df.describe())

import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 

plt.figure(figsize=(10,6))
index = df.index
plt.scatter(df['회사이름'], df['주식가'], s=50)
plt.xlabel('회사이름')
plt.ylabel('주식가')
plt.grid()

plt.show()

#################################
plt.figure()
plt.ylabel('회사이름')
plt.xlabel('주식가')
df['주식가'].sort_values().plot(kind='barh', grid=True, figsize=(10, 10))

plt.show()


 