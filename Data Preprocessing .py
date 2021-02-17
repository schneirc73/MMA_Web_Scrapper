#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 
import datetime


# In[2]:


df = pd.read_excel('C:/Users/schne/Desktop/MMA Prediction Files/DoubledUp.xlsx')
df
df.fillna(0)


# In[5]:


# Takedowns Fighter_A
tk_A = df["Takedowns_A"].str.split("of", n = 1, expand = True) 
df['Takedowns_Landed_A']=tk_A[0].str.replace(r'\D', '').astype(int)
df['Takedowns_Attempted_A'] =tk_A[1].str.replace(r'\D', '').astype(int)
# Takedowns_Fighter_B
tk_B = df["Takedowns_B"].str.split("of", n = 1, expand = True) 
df['Takedowns_Landed_B']=tk_B[0].str.replace(r'\D', '').astype(int)
df['Takedowns_Attempted_B'] =tk_B[1].str.replace(r'\D', '').astype(int)
#Round Information
max_round = df["max_Rounds"].str.split(",", n = 1, expand = True) 
df['Max_Round']=max_round[0].str.replace(r'\D', '').astype(int)


# In[6]:


df[[ 'Sig_Strike_Percentage_A', 'Takedown_Acc_A', 'Sig_Strike_Percentage_B', 'Takedown_Acc_B']] = df[['Sig_Strike_Percentage_A', 'Takedown_Acc_A', 'Sig_Strike_Percentage_B', 'Takedown_Acc_B']].apply(pd.to_numeric)


# In[7]:


df['Sig_Strike_Percentage_A'] = df['Sig_Strike_Percentage_A'] / 100
df['Sig_Strike_Percentage_B'] = df['Sig_Strike_Percentage_B'] / 100
df['Takedown_Acc_A'] = df['Takedown_Acc_A'] / 100
df['Takedown_Acc_B'] = df['Takedown_Acc_B'] / 100
df['Strike_Defence_A'] = 1 - df['Sig_Strike_Percentage_B']
df['Takedown_Def_A'] = 1 - df['Takedown_Acc_B']
df['Date'] =df['Date'].apply(pd.to_datetime)


# In[8]:


df.drop(['Takedowns_A', 'Takedowns_B'], axis=1, inplace=True)


# In[9]:


pd.set_option('display.max_columns', None)
df.head()


# In[10]:


Unique_Fighters=len(df.NAME_A.unique())
Unique_Fighters_List = df.NAME_A.unique().tolist()
print("This is the amount of unique fighters within the dataset")
Unique_Fighters


# In[12]:


dfsorty=df.sort_values(by = 'Date', ascending = False)
df.to_excel('C:/Users/schne/Desktop/MMA Prediction Files/UseforViz.xlsx')
dfsorty


# In[109]:


# P=df.loc[df['event_Title'] == 'Marina Rodriguez']
# Event_List = df.event_Title.unique().tolist()
Event_List =df.event_Title.unique().tolist()
Event_Objects = list()
Fights_To_Use = list()
PT=df.loc[df['event_Title'] == 'UFC 258: Usman vs. Burns'].select_dtypes(include=['bool', 'object'])
#     Event_Objects.append(PT)
RT=df.loc[df['event_Title'] == 'UFC 258: Usman vs. Burns']
Fighter_Name_List=PT.NAME_A.tolist()
Fighter = Fighter_Name_List
Time=df.loc[df.loc[df['event_Title'] == 'UFC 258: Usman vs. Burns'].reset_index().Date[0] > df['Date']]
Time.sort_values(by = 'Date', ascending = False)

for Fighter in Fighter_Name_List:
    Fights_To_Use.append((Time[Time['NAME_A']==Fighter].sort_values(by='Date',ascending = False)[:1]))
#     Event_Objects.append(df.loc[df['event_Title'] == 'UFC 258: Usman vs. Burns'].select_dtypes(include=['bool', 'object']))
    Lenny=len((Time[Time['NAME_A']==Fighter]))
    if Lenny <= 1 :
        print('Not Enough Records ' + Fighter)
    else:
        print('Enough ' + Fighter)
Fights_To_Use


# In[113]:


mean_matrix = pd.concat(Fights_To_Use, axis=1)
mean_matrix
mean_matrix.to_excel('C:/Users/schne/Desktop/MMA Prediction Files/UNOUFC258.xlsx')


# In[16]:


Event_List =df.event_Title.unique().tolist()
for i in Event_List:
    print(i)


# In[70]:



mean_matrix.to_excel(Path)

