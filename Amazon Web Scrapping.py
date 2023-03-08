#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[36]:


# connect to website

URL = 'https://www.amazon.ca/Glad-Black-Garbage-Bags-Easy-Tie/dp/B0094ZK372?ref_=Oct_d_oup_d_6370614011_1&pd_rd_w=MZbfG&content-id=amzn1.sym.d4e7fcd6-4211-4112-9271-0bb0602f2a5d&pf_rd_p=d4e7fcd6-4211-4112-9271-0bb0602f2a5d&pf_rd_r=YC5RXX89XMYTZ3XV553S&pd_rd_wg=YaOCE&pd_rd_r=a0b84763-d166-40f1-ba7b-a901c9ca6dec&pd_rd_i=B0094ZK372&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id= 'productTitle').get_text()

price = soup2.find(id= 'sns-base-price').get_text()

print(title)
print(price)







# In[37]:


price = price.strip()[1:6]
title = title.strip()[0:23]

print(price)
print(title)


# In[43]:


import datetime

today = datetime.date.today()
print(today)


# In[45]:


import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]

#with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    #writer = csv.writer(f)
    #writer.writerow(header)
    #writer.writerow(data)



# In[57]:


import pandas as pd

df = pd.read_csv(r'C:\Users\Kunal\AmazonWebScraperDataset.csv')

print(df)


# In[51]:


# now we are appending data to csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[55]:



def check_price():
    URL = 'https://www.amazon.ca/Glad-Black-Garbage-Bags-Easy-Tie/dp/B0094ZK372?ref_=Oct_d_oup_d_6370614011_1&pd_rd_w=MZbfG&content-id=amzn1.sym.d4e7fcd6-4211-4112-9271-0bb0602f2a5d&pf_rd_p=d4e7fcd6-4211-4112-9271-0bb0602f2a5d&pf_rd_r=YC5RXX89XMYTZ3XV553S&pd_rd_wg=YaOCE&pd_rd_r=a0b84763-d166-40f1-ba7b-a901c9ca6dec&pd_rd_i=B0094ZK372&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= 'productTitle').get_text()

    price = soup2.find(id= 'sns-base-price').get_text()
    
    price = price.strip()[1:6]
    title = title.strip()[0:23]
    
    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    







# In[ ]:


while(True): 
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\Kunal\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:




