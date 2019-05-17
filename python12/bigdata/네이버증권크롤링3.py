import requests
from bs4 import BeautifulSoup

def get_price(code):
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
#     print(result)
    # print(result.content)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    # print(bs_obj)
    
    no_today = bs_obj.find("p", {"class":"no_today"})
#     print(no_today)
    
    blind_now = no_today.find("span", {"class":"blind"})
    
    return blind_now.text

    
company_codes = ["005930", "027740", "068270"]
company_names = ["삼성전자", "마니커", "하이닉스"]

index = 0
for code in company_codes:
    price = get_price(code)
    name = company_names[index]
    print(name, " : ", price)
    index =  index + 1
    






