import requests
from bs4 import BeautifulSoup

def get_names():
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page=1"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    td_list = bs_obj.findAll("td", {"class":"ctg"})
#     print(td_list)
    company_names = []
    
    for td in td_list:
        company_names.append(td.find("a").text)
    
#     print(company_names)
    
    return company_names    

def get_now_price():
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page=1"
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

def total_info():
    company_names = get_names()
    now_price_list = get_now_price()
    
    print("회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        print(name, "\t", price)

total_info()




    

    
    






