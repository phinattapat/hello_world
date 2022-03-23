import requests
import bs4
from urllib.request import urlopen as request

def iaa(name):
    
    url = f"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol={name}&ssoPageId=11&selectPage=10"
    web_open = request(url)
    page_html = web_open.read()
    web_open.close()
    
    soup = bs4.BeautifulSoup(page_html, "lxml")
    word = soup.select(".text-right")
    today = str(word[0])
    today_price = ""
    target = word[(len(word))-2]
    price = str(target)
    show = ""
    n = 0
    for a in range(len(today)):
        if today[a] in ["1","2","3","4","5","6","7","8","9","0","."]:
            today_price = today_price+str(today[a])
        today_price = today_price
    n = len(today_price)-1
    today_price = today_price[1:n]    
    for i in range(len(price)):
        if price[i] in ["1","2","3","4","5","6","7","8","9","0","."]:
            show = show+str(price[i])
        show = show
        
    length = len(show)
    length = length-2
    show = show[0:length]
    price = show
    try:
        mos30 = float(price)
        mos30 = mos30*0.7
    except:
        price = "-"
        mos30 = "-"
    print(f"{name}")
    print(f"iaa target price: {price}")
    try:
        print(f"iaa mos30 price: {mos30:.2f}")
    except:
        print(f"iaa mos30 price: {mos30}")
    print(f"today price: {today_price}\n")

on = True
while on:
    settrade = input("IAA: ")
    iaa(settrade)
    on_off = input("Exit?(y,n): ")
    on_off.lower()
    while on_off not in ["y","n"]:
        on_off.lower()
        on_off = input("Exit: ")
    
    if on_off=="y":
        on = False
        print()
