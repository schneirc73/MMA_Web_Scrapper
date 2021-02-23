#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import json
from time import sleep
from random import randint
import time


# In[ ]:


start = time.time()
fighters_list= [] #List for fighter's name in upcoming Event
url = 'http://www.ufcstats.com/statistics/events/completed?page=1'  #Reads the location to the link of the upcoming event

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for a in soup.find_all('a', href=True):  # This for Loop grabs all the event links on the event page
    Event_urls.append(a['href'])
t=Event_urls[5:6] # 5:6 indicates the upcoming event, this is mostly updated after the previous upcoming event is completed

for url in t: #Visits the upcoming event url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    p=soup.find_all('a',  {'class':"b-link b-link_style_black"})
    for i in p:
        TT=i.text.strip() # Strips extra text from the names
        fighters_list.append(TT) # Places striped names into the list

    sleep(randint(2,5)) 
    


# In[ ]:


print(len(fighters_list))
fighters_list
fighters_list = [x for x in fighters_list if x != 'Privacy Policy'] # Removes 'Privacy Policy' from the list
fighters_list = [x for x in fighters_list if x != 'View Matchup'] # Removes 'View Matchup' from the list
fighters_list = [x for x in fighters_list if x != 'View'] # Removes 'View' from the list


print(len(fighters_list))
fighters_list


# In[ ]:


# Places names into dataframe used later to create upcoming prediction file
Winner_DF = pd.DataFrame({

    'Winners' : fighters_list
})
Winner_DF


# In[ ]:


Winner_DF.to_excel('C:/Users/schne/Desktop/MMA Prediction Files/UpcomingFightList.xlsx')

