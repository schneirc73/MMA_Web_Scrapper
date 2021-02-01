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


# Event Dict
Event_title = []
Date = []
Location = []

#Fight Dict
Name_A = []
Sig_Strike_A = []
Sig_Strike_Percentage_A = []
Total_Strikes_Landed_A = []
Takedowns_A = []
Takedown_Acc_A = []
Subs_A = []
Reversal_A = []
Control_A = []
Name_B = []
Sig_Strike_B = []
Sig_Strike_Percentage_B = []
Total_Strikes_Landed_B = []
Takedowns_B = []
Takedown_Acc_B = []
Subs_B = []
Reversal_B = []
Control_B = []
event_Title = []
weight = []
method = []
round_Stopage = []
time_Stopage = []
max_Rounds = []
referee = []
judgeA = []
judgeA_Score = []
judgeB = []
judgeB_Score = []
judgeC = []
judgeC_Score = []

# Fighter Dict
Name_AA = []
Height_AA = []
Weight_AA = []
Reach_AA = []
Stance_AA = []
DOB_AA = []
Current_Record_AA = []


# In[ ]:


start = time.time()
Event_urls = []
Fight_urls = []
Fighter_urls = []
url = 'http://www.ufcstats.com/statistics/events/completed?page=8'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for a in soup.find_all('a', href=True):  # This for Loop grabs all the event links on the event page
    Event_urls.append(a['href'])
t=Event_urls[5:30] # Puts all the event links of interes

for url in t: #This places each event into the url to allow for scrapping of each event on a page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    Event_title1=soup.select_one('.b-content__title-highlight').next.strip()
    Event_title.append(Event_title1)
    Date_Occured=soup.select_one('.b-list__box-list').next.next.next.next.next.next.strip()
    Date.append(Date_Occured)
    Location1=soup.select_one('.b-list__box-list').next.next.next.next.next.next.next.next.next.next.next.next.strip()
    Location.append(Location1)
    sleep(randint(5,10))
for urltt in t:          
    response = requests.get(urltt)
    soup = BeautifulSoup(response.content, "lxml")
    P=soup.find_all("a", {'class':"b-flag b-flag_style_green"})
    sleep(randint(5,10))
    for i in P:
        Fight_urls.append(i['href'])
for urlF in Fight_urls: #Uses each fight detail url to grab needed information
    respone = requests.get(urlF)
    soup = BeautifulSoup(respone.content, 'html.parser')
    Fighter_A=soup.select_one('td.b-fight-details__table-col').next.next.next.next.next
    Name_A.append(Fighter_A)
    Fighter_B=soup.select_one('td.b-fight-details__table-col').next.next.next.next.next.next.next.next.next.next.next
    Name_B.append(Fighter_B)
    Event_Title=soup.select_one('.b-content__title').text.strip()
    event_Title.append(Event_Title)
    Weight=soup.select_one('.b-fight-details__fight-title').text.strip()
    weight.append(Weight)
    Method=soup.select_one('i.b-fight-details__text-item_first').text.strip().split()[1]
    method.append(Method)
    Round_Stopage=soup.select_one('.b-fight-details__text-item').text.strip().split()[1]
    round_Stopage.append(Round_Stopage)
    Time_Stopage=soup.select_one('.b-fight-details__text-item').next.next.next.next.next.next.text.strip().split()[1]
    time_Stopage.append(Time_Stopage)
    Max_Rounds=soup.select_one('.b-fight-details__text-item').next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[2:4]
    max_Rounds.append(Max_Rounds)
    Referee=soup.select_one('.b-fight-details__text-item').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip()
    referee.append(Referee)
    Significant_Strikes_A=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Sig_Strike_A.append(Significant_Strikes_A)
    Significant_Strikes_B=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Sig_Strike_B.append(Significant_Strikes_B)
    Significant_Strike_Percentage_A=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Sig_Strike_Percentage_A.append(Significant_Strike_Percentage_A)
    Significant_Strike_Percentage_B=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[1]
    Sig_Strike_Percentage_B.append(Significant_Strike_Percentage_B)
    Total_Strikes_Landed_AA=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Total_Strikes_Landed_A.append(Total_Strikes_Landed_AA)
    Total_Strikes_Landed_BB=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[3]
    Total_Strikes_Landed_B.append(Total_Strikes_Landed_BB)
    Takedowns_AA=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0:3]
    Takedowns_A.append(Takedowns_AA)
    Takedowns_BB=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[3:6]
    Takedowns_B.append(Takedowns_BB)
    Takedown_Acc_AA=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Takedown_Acc_A.append(Takedown_Acc_AA)
    Takedown_Acc_BB=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[1]
    Takedown_Acc_B.append(Takedown_Acc_BB)
    Sub_Attempts_A=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Subs_A.append(Sub_Attempts_A)
    Sub_Attempts_B=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[1]
    Subs_B.append(Sub_Attempts_B)
    Reversal_AA=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Reversal_A.append((Reversal_AA))
    Reversal_BB=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[1]
    Reversal_B.append(Reversal_BB)
    Control_AA=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[0]
    Control_A.append(Control_AA)
    Control_BB=soup.select_one('.b-fight-details__table-text').next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.strip().split()[1]
    Control_B.append(Control_BB)
    sleep(randint(5,10))
for urlttt in t:
    response = requests.get(urlttt)
    soup = BeautifulSoup(response.content, "lxml")
    QT=soup.find_all("a", {'class': 'b-link b-link_style_black'})
    sleep(randint(5,10))
    for QYT in QT:
        Fighter_urls.append(QYT['href'])



end = time.time()
print(end - start)


# In[ ]:


Events = pd.DataFrame({
    'Event_Title': Event_title,
    'Date' : Date,
    'Location': Location
})
Events
# Fight DF
fights = pd.DataFrame({
    'Name_A' : Name_A,
    'Sig_Strike_A': Sig_Strike_A,
    'Sig_Strike_Percentage_A' : Sig_Strike_Percentage_A,
    'Total_Strikes_Landed_A': Total_Strikes_Landed_A,
    'Takedowns_A' : Takedowns_A,
    'Takedown_Acc_A' : Takedown_Acc_A,
    'Subs_A' : Subs_A,
    'Reversal_A': Reversal_A,
    'Control_A' : Control_A,
    'Name_B' : Name_B,
    'Sig_Strike_B' : Sig_Strike_B,
    'Sig_Strike_Percentage_B' : Sig_Strike_Percentage_B,
    'Total_Strikes_Landed_B' : Total_Strikes_Landed_B,
    'Takedowns_B' : Takedowns_B,
    'Takedown_Acc_B' : Takedown_Acc_B,
    'Subs_B' : Subs_B,
    'Reversal_B' : Reversal_B,
    'Control_B' : Control_B,
    'event_Title': event_Title,
    'weight' : weight,
    'method' : method,
    'round_Stopage': round_Stopage,
    'time_Stopage': time_Stopage,
    'max_Rounds' : max_Rounds,
    'referee' : referee,

})

## When pulling information from FightMetric, the winner tag is an imagie, so a way to work around this is to pull the name of the fighters from the event page,
## and because on the event page the first name on the list is the winner when we merge it later we can take 1,3,....,n and match it to Name_A column in the larger
## dataset giving us a fragile workaround but one that will work

fighters_list= []
Winners =[]

start = time.time()
Event_urls = []

url = 'http://www.ufcstats.com/statistics/events/completed?page=5'

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for a in soup.find_all('a', href=True):  # This for Loop grabs all the event links on the event page
    Event_urls.append(a['href'])
t=Event_urls[5:30] # Puts all the event links of interes

for url in t: #This places each event into the url to allow for scrapping of each event on a page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    p=soup.find_all('a',  {'class':"b-link b-link_style_black"})
    for i in p:
        TT=i.text.strip()
        fighters_list.append(TT)

    sleep(randint(2,5))
end = time.time()
print(end - start)

Winners = fighters_list[::2] # This grabs 1,3,......,n aka the winner from each fight.

## This Dataframe will be the same length as the larger fight database and will be ordered in the same way so by creating a fake column for both we can merge and fix the issue
## of not being able to pull the winner from the fight tables.
Winner_DF = pd.DataFrame({

    'Winners' : Winners
})
Winner_DF




