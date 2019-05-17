import requests
from bs4 import BeautifulSoup

def get_price(code):
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
    print(result)
    # print(result.content)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    # print(bs_obj)
    
    no_today = bs_obj.find("p", {"class":"no_today"})
    print(no_today)
    
    blind_now = no_today.find("span", {"class":"blind"})
    print(blind_now.text)
    
get_price("005930")
get_price("027740")
get_price("068270")









