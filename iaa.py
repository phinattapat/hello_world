#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

iaa = {"auct":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=AUCT&ssoPageId=11&selectPage=10",
       "bcpg":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=BCPG",
       "bgrim":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=BGRIM&selectPage=10",
       "cbg":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=CBG&ssoPageId=11&selectPage=10",
       "cpf":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=CPF&ssoPageId=11&selectPage=10",
       "mc":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=MC&ssoPageId=11&selectPage=10",
       "ner":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=NER&ssoPageId=11&selectPage=10",
       "or":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=OR&ssoPageId=11&selectPage=10",
       "sappe":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=SAPPE&ssoPageId=11&selectPage=10",
       "tfm":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=TFM",
       "tqm":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TQM&ssoPageId=11&selectPage=10",
       "ttw":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TTW&ssoPageId=11&selectPage=10",
       "whaup":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=WHAUP",
       "xo":"https://portal.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=XO",
       "asefa":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=ASEFA&ssoPageId=11&selectPage=10",
       "drt":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=DRT&selectPage=10",
       "ptt":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=ptt&selectPage=10",
       "qh":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=QH&ssoPageId=9&selectPage=10",
       "lh":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=LH&ssoPageId=11&selectPage=10",
       "bbl":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=BBL&ssoPageId=11&selectPage=10",
       "kbank":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=KBANK&ssoPageId=11&selectPage=10",
       "scb":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=SCB&ssoPageId=11&selectPage=10",
       "ktb":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=ktb",
       "msc":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=MSC&selectPage=10",
       "mcs":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=MCS&ssoPageId=11&selectPage=10",
       "tvo":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TVO&ssoPageId=11&selectPage=10",
       "toa":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TOA&ssoPageId=11&selectPage=10",
       "dpaint":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=DPAINT"}

name = input("iaa: ")
while name not in iaa:
    name = input("iaa: ")

result = requests.get(iaa[name])
import bs4

soup = bs4.BeautifulSoup(result.text, "lxml")
word = soup.select(".text-right")
target = word[(len(word))-2]

price = str(target)
show = ""
for i in range(len(price)):
    if price[i] in ["1","2","3","4","5","6","7","8","9","0","."]:
        show = show+str(price[i])
    show = show
length = len(show)
length = length-2
show = show[0:length]
price = show
print(f"\niaa {name} target price: {price}")


# In[5]:


import requests
import bs4

iaa = {"auct":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=AUCT&ssoPageId=11&selectPage=10",
       "bcpg":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=BCPG",
       "bgrim":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=BGRIM&selectPage=10",
       "cbg":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=CBG&ssoPageId=11&selectPage=10",
       "cpf":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=CPF&ssoPageId=11&selectPage=10",
       "mc":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=MC&ssoPageId=11&selectPage=10",
       "ner":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=NER&ssoPageId=11&selectPage=10",
       "or":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=OR&ssoPageId=11&selectPage=10",
       "sappe":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=SAPPE&ssoPageId=11&selectPage=10",
       "tfm":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=TFM",
       "tqm":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TQM&ssoPageId=11&selectPage=10",
       "ttw":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TTW&ssoPageId=11&selectPage=10",
       "whaup":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=WHAUP",
       "xo":"https://portal.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=XO",
       "asefa":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=ASEFA&ssoPageId=11&selectPage=10",
       "drt":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=DRT&selectPage=10",
       "ptt":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=ptt&selectPage=10",
       "qh":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=QH&ssoPageId=9&selectPage=10",
       "lh":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=LH&ssoPageId=11&selectPage=10",
       "bbl":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=BBL&ssoPageId=11&selectPage=10",
       "kbank":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=KBANK&ssoPageId=11&selectPage=10",
       "scb":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=SCB&ssoPageId=11&selectPage=10",
       "ktb":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=ktb",
       "msc":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=MSC&selectPage=10",
       "mcs":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=MCS&ssoPageId=11&selectPage=10",
       "tvo":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TVO&ssoPageId=11&selectPage=10",
       "toa":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?txtSymbol=TOA&ssoPageId=11&selectPage=10",
       "dpaint":"https://www.settrade.com/AnalystConsensus/C04_10_stock_saa_p1.jsp?selectPage=10&txtSymbol=DPAINT"}

name = ["auct","bcpg","bgrim","cbg","cpf","mc","ner","or","sappe","tfm","tqm","ttw","whaup","xo","asefa","drt","ptt","qh","lh","bbl","kbank","scb","ktb","msc","mcs","tvo","toa","dpaint"]
for x in range((len(iaa))-1):
    result = requests.get(iaa[name[x]])
    soup = bs4.BeautifulSoup(result.text, "lxml")
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
    print(f"{name[x]}")
    print(f"iaa target price: {price}")
    print(f"iaa mos30 price: {mos30}")
    print(f"today price: {today_price}\n")


# In[ ]:





# In[92]:





# In[93]:





# In[94]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





