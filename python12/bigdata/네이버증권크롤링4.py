import requests
from bs4 import BeautifulSoup

def get_names():
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page=1"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    td_list = bs_obj.findAll("td", {"class":"ctg"})
    print(td_list)
    
    print(td_list[0].find("a").text)
    
#     blind_now = no_today[0].find("a") 
get_names()
    

    
    






