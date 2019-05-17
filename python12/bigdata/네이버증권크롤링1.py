import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
print(result)
# print(result.content)
bs_obj = BeautifulSoup(result.content, "html.parser")
# print(bs_obj)

no_today = bs_obj.find("p", {"class":"no_today"})
print(no_today)

blind_now = no_today.find("span", {"class":"blind"})
print(blind_now.text)







