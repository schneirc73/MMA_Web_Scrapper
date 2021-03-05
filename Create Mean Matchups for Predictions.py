#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import datetime


# In[ ]:


df = pd.read_excel('C:/Users/schne/Desktop/MMA Prediction Files/UseForViz.xlsx')
df


# In[ ]:


df['Strike_Difference_A'] = df['Sig_Strike_A'] - df['Sig_Strike_B']
df['Strike_Difference_B'] = df['Sig_Strike_B'] - df['Sig_Strike_A']

df['Total_Strike_Difference_A'] = df['Total_Strikes_Landed_A'] - df['Total_Strikes_Landed_B']
df['Total_Strike_Difference_B'] = df['Total_Strikes_Landed_B'] - df['Total_Strikes_Landed_A']


# df['Strike_Defence_Value_A'] = df['Strike_Defence_A'] * df['Sig_Strike_B']


df['Strike_Accuracy_Difference_A'] = df['Sig_Strike_Percentage_A'] - df['Sig_Strike_Percentage_B']
df['Strike_Accuracy_Difference_B'] = df['Sig_Strike_Percentage_B'] - df['Sig_Strike_Percentage_A']


df['Takedown_Difference_A'] = df['Takedowns_Landed_A'] - df['Takedowns_Landed_B']
df['Takedown_Difference_B'] = df['Takedowns_Landed_B'] - df['Takedowns_Landed_A']


df['Takedown_Accuracy_Difference_A'] = df['Takedown_Acc_A'] - df['Takedown_Acc_B']
df['Takedown_Accuracy_Difference_B'] = df['Takedown_Acc_B'] - df['Takedown_Acc_A']

df['Total_Control_Time_Seconds_A'] = (df['Control_A_Mintues'] * 60) + df['Control_A_Seconds']
df['Total_Control_Time_Seconds_B'] = (df['Control_B_Minutes'] * 60) + df['Control_B_Seconds']

df['Control_Difference_A'] = df['Total_Control_Time_Seconds_A'] - df['Total_Control_Time_Seconds_B']
df['Control_Difference_B'] = df['Total_Control_Time_Seconds_B'] - df['Total_Control_Time_Seconds_A']


# In[ ]:


Newest=df.sort_values(by = 'Date', ascending = False)


# In[ ]:


Fighter_A = []
Fighter_B = []
Weight = []
Time_Of_Event = []
Event_Name = []
Method_of_Outcome = []
Winner_Name = []
Outcome_of_Fight = []
Significant_Strikes_Landed_A = []
Significant_Strike_Accuracy_A = []
Total_Strikes_Landed_A = []
Takedowns_Landed_A = []
Takedowns_Attempted_A = []
Takedown_Accuarcy_A = []
Strike_Avoidance_A = []
Significant_Strikes_Landed_B = []
Significant_Strike_Accuracy_B = []
Fight_Count_A = []
Fight_Count_B = []
Total_Strikes_Landed_B = []
Takedowns_Landed_B = []
Takedowns_Attempted_B = []
Takedown_Accuarcy_B = []
Strike_Avoidance_B = []
Strike_Difference_A = []
Strike_Difference_B = []
Total_Strike_Difference_A = []
Total_Strike_Difference_B = []
Strike_Defence_Value_A = []
Strike_Defence_Value_B = []
Strike_Accuracy_Difference_A =[]
Strike_Accuracy_Difference_B =[]
Takedown_Difference_A = []
Takedown_Difference_B = []
Takedown_Accuracy_Difference_A = []
Takedown_Accuracy_Difference_B = []
Control_Time_Seconds_A = []
Control_Time_Seconds_B =  []
Control_Time_Difference_A = []
Control_Time_Difference_B = []
Prev_Fights_Percentage_A = []
Prev_Fights_Percentage_B = []
Size_Good_For_A = []
Size_Good_For_B = []


# In[ ]:


# Good Stuff
Size = 3
Event_List =Newest.event_Title.unique().tolist()
Fights_To_Use = list()
value = list()
Event_inQuestion = list()
# Event_List = Event_List[:1]
# B = list()
for Event in Event_List:
    Time = df.loc[df.loc[df['event_Title'] == Event].reset_index().Date[0] > df['Date']]  # Used to select fights before the current one
    EventOI = df[df['event_Title'] == Event]
    Fighters=EventOI.NAME_A.tolist()
    Fighters_B = EventOI.Name_B.tolist()
    
    for Fighter in Fighters:
        A=EventOI.loc[EventOI['NAME_A'] == Fighter]
        Winner_Name.append(A.Winner.to_list())
        Outcome_of_Fight.append(A.Outcome_A.to_list())
        Fighter_A.append(A.NAME_A.to_list())
        Fighter_B.append(A.Name_B.to_list())
        Weight.append(A.weight.to_list())
        Event_Name.append(A.event_Title.to_list())
        Time_Of_Event.append(A.Date.to_list())
        Method_of_Outcome.append(A.method.to_list())
        Prev_Fights_A_Len = len(Time[Time['NAME_A'] == Fighter].sort_values(by= 'Date', ascending = False)[:Size])
        if Prev_Fights_A_Len >= Size:
            Prev_Fights_A = Time[Time['NAME_A'] == Fighter].sort_values(by= 'Date', ascending = False)[:Size].mean()
            Fight_Count_A = len(Time[Time['NAME_A'] == Fighter].sort_values(by= 'Date', ascending = False)[:Size])
            Significant_Strikes_Landed_A.append(Prev_Fights_A.Sig_Strike_A)
            Significant_Strike_Accuracy_A.append(Prev_Fights_A.Sig_Strike_Percentage_A)
            Total_Strikes_Landed_A.append(Prev_Fights_A.Total_Strikes_Landed_A)
            Takedowns_Landed_A.append(Prev_Fights_A.Takedowns_Landed_A)
            Takedowns_Attempted_A.append(Prev_Fights_A.Takedowns_Attempted_A)
            Takedown_Accuarcy_A.append(Prev_Fights_A.Takedown_Acc_A)
            Strike_Avoidance_A.append(Prev_Fights_A.Strike_Defence_A)
            Strike_Difference_A.append(Prev_Fights_A.Strike_Difference_A)
            Total_Strike_Difference_A.append(Prev_Fights_A.Total_Strike_Difference_A)
    #         Strike_Defence_Value_A.append(Prev_Fights_A.Strike_Defence_Value_A)
            Strike_Accuracy_Difference_A.append(Prev_Fights_A.Strike_Accuracy_Difference_A)
            Takedown_Difference_A.append(Prev_Fights_A.Takedown_Difference_A)
            Takedown_Accuracy_Difference_A.append(Prev_Fights_A.Takedown_Accuracy_Difference_A)
            Control_Time_Seconds_A.append(Prev_Fights_A.Total_Control_Time_Seconds_A)
            Control_Time_Difference_A.append(Prev_Fights_A.Control_Difference_A)
            Prev_Fights_Percentage_A.append(Prev_Fights_A.Outcome_A)
            Size_Good_For_A.append('Yes')
        else :
            Significant_Strikes_Landed_A.append('NA')
            Significant_Strike_Accuracy_A.append('NA')
            Total_Strikes_Landed_A.append('NA')
            Takedowns_Landed_A.append('NA')
            Takedowns_Attempted_A.append('NA')
            Takedown_Accuarcy_A.append('NA')
            Strike_Avoidance_A.append('NA')
            Strike_Difference_A.append('NA')
            Total_Strike_Difference_A.append('NA')
    #         Strike_Defence_Value_A.append(Prev_Fights_A.Strike_Defence_Value_A)
            Strike_Accuracy_Difference_A.append('NA')
            Takedown_Difference_A.append('NA')
            Takedown_Accuracy_Difference_A.append('NA')
            Control_Time_Seconds_A.append('NA')
            Control_Time_Difference_A.append('NA')
            Prev_Fights_Percentage_A.append('NA')
            Size_Good_For_A.append('No')

        
        
    for Fighter_Bb in Fighters_B:
#         B = EventOI.loc[EventOI['Name_B'] == Fighter_Bb]
        Prev_Fights_B_Len = len(Time[Time['NAME_A'] == Fighter_Bb].sort_values(by= 'Date', ascending = False)[:Size])
        if Prev_Fights_B_Len >= Size:
            Prev_Fights_B = Time[Time['NAME_A'] == Fighter_Bb].sort_values(by= 'Date', ascending = False)[:Size].mean()
    #         Fight_Count_B = len(Time[Time['NAME_A'] == Fighter_Bb].sort_values(by= 'Date', ascending = False)[:Size])
    #         Fight_Count_B.apply(len(Time[Time['NAME_A'] == Fighter_Bb].sort_values(by= 'Date', ascending = False)[:Size])
            Significant_Strikes_Landed_B.append(Prev_Fights_B.Sig_Strike_A)
            Significant_Strike_Accuracy_B.append(Prev_Fights_B.Sig_Strike_Percentage_A)
            Total_Strikes_Landed_B.append(Prev_Fights_B.Total_Strikes_Landed_A)
            Takedowns_Landed_B.append(Prev_Fights_B.Takedowns_Landed_A)
            Takedowns_Attempted_B.append(Prev_Fights_B.Takedowns_Attempted_A)
            Takedown_Accuarcy_B.append(Prev_Fights_B.Takedown_Acc_A)
            Strike_Avoidance_B.append(Prev_Fights_B.Strike_Defence_A)
            Strike_Difference_B.append(Prev_Fights_B.Strike_Difference_A)
            Total_Strike_Difference_B.append(Prev_Fights_B.Total_Strike_Difference_A)
    #         Strike_Defence_Value_B.append(Prev_Fights_B.Strike_Defence_Value_A)
            Strike_Accuracy_Difference_B.append(Prev_Fights_B.Strike_Accuracy_Difference_A)
            Takedown_Difference_B.append(Prev_Fights_B.Takedown_Difference_A)
            Takedown_Accuracy_Difference_B.append(Prev_Fights_B.Takedown_Accuracy_Difference_A)
            Control_Time_Seconds_B.append(Prev_Fights_B.Total_Control_Time_Seconds_A)
            Control_Time_Difference_B.append(Prev_Fights_B.Control_Difference_A)
            Prev_Fights_Percentage_B.append(Prev_Fights_B.Outcome_A)
            Size_Good_For_B.append('Yes')
        else:
            Significant_Strikes_Landed_B.append('NA')
            Significant_Strike_Accuracy_B.append('NA')
            Total_Strikes_Landed_B.append('NA')
            Takedowns_Landed_B.append('NA')
            Takedowns_Attempted_B.append('NA')
            Takedown_Accuarcy_B.append('NA')
            Strike_Avoidance_B.append('NA')
            Strike_Difference_B.append('NA')
            Total_Strike_Difference_B.append('NA')
    #         Strike_Defence_Value_B.append(Prev_Fights_B.Strike_Defence_Value_A)
            Strike_Accuracy_Difference_B.append('NA')
            Takedown_Difference_B.append('NA')
            Takedown_Accuracy_Difference_B.append('NA')
            Control_Time_Seconds_B.append('NA')
            Control_Time_Difference_B.append('NA')
            Prev_Fights_Percentage_B.append('NA')
            Size_Good_For_B.append('No')
   


# In[ ]:


Test = pd.DataFrame({
    'Size_Good_For_A': Size_Good_For_A,
    'Size_Good_For_B' : Size_Good_For_B,
    'Outcome_of_Fight' : Outcome_of_Fight,
    'Method_of_Outcome' : Method_of_Outcome,
    'Winner_Name' : Winner_Name,
    'Fighter_A': Fighter_A,
    'Fighter_B' : Fighter_B,
    'Weight' : Weight,
    'Event' : Event_Name,
    'Date' : Time_Of_Event,
    'Prev_Fights_Percentage_A' : Prev_Fights_Percentage_A,
    'Significant_Strikes_Landed_A' : Significant_Strikes_Landed_A,
    'Significant_Strike_Accuracy_A' :Significant_Strike_Accuracy_A,
    'Total_Strikes_Landed_A': Total_Strikes_Landed_A,
    'Takedowns_Landed_A' : Takedowns_Landed_A, 
    'Takedowns_Attempted_A' :Takedowns_Attempted_A,
    'Takedown_Accuarcy_A' :Takedown_Accuarcy_A,
    'Strike_Avoidance_A' : Strike_Avoidance_A,
    'Strike_Difference_A' : Strike_Difference_A,
    'Total_Strike_Difference_A' : Total_Strike_Difference_A,
    'Strike_Accuracy_Difference_A' : Strike_Accuracy_Difference_A,
    'Takedown_Difference_A' : Takedown_Difference_A,
    'Takedown_Accuracy_Difference_A' : Takedown_Accuracy_Difference_A,
#     'Strike_Defence_Value_A' : Strike_Defence_Value_A,
    'Control_Time_Seconds_A' : Control_Time_Seconds_A,
    'Control_Time_Difference_A' : Control_Time_Difference_A,
    'Prev_Fights_Percentage_B' : Prev_Fights_Percentage_B,
    'Significant_Strikes_Landed_B' : Significant_Strikes_Landed_B,
    'Significant_Strike_Accuracy_B' : Significant_Strike_Accuracy_B,
   'Total_Strikes_Landed_B' : Total_Strikes_Landed_B,
    'Takedowns_Landed_B' : Takedowns_Landed_B,
    'Takedowns_Attempted_B' : Takedowns_Attempted_B,
    'Takedown_Accuarcy_B' : Takedown_Accuarcy_B,
    'Strike_Avoidance_B' : Strike_Avoidance_B,
    'Strike_Difference_B' : Strike_Difference_B,
    'Total_Strike_Difference_B' : Total_Strike_Difference_B,
#     'Strike_Defence_Value_B' : Strike_Defence_Value_B,
    'Strike_Accuracy_Difference_B' : Strike_Accuracy_Difference_B,
    'Takedown_Difference_B': Takedown_Difference_B,
    'Takedown_Accuracy_Difference_B' : Takedown_Accuracy_Difference_B,
    'Control_Time_Seconds_B' : Control_Time_Seconds_B,
    'Control_Time_Difference_B' : Control_Time_Difference_B
})
Test

