#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Simulation for 10 days with 90 newspapaer
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt

day_by_day = []
all_day = []
rn_for_NT = 0
NT = 0
rn_demand = 0

demand = 0
revenue = 0
lp = 0
scrap = 0
purchase_value_of_90_np = round((.33 * 90), 2)
dp = 0

def rn_for_nt(k):
    global day_by_day, rn_for_NT
    for i in range(k):
        day_by_day = []  
        user_rn_nt = int(input("Enter a random number for NT (0-100): "))  
        rn_for_NT = user_rn_nt if 0 <= user_rn_nt <= 100 else randrange(100)  
        day_by_day.append(i + 1)
        day_by_day.append(rn_for_NT)
        type_of_news_day()

def type_of_news_day():
    global NT
    if rn_for_NT < 36:
        NT = "good"
    elif rn_for_NT < 81:
        NT = "fair"
    elif rn_for_NT < 101:
        NT = "poor"
    day_by_day.append(NT)
    rn_for_demand()

def rn_for_demand():
    global rn_demand
    user_rn_demand = int(input("Enter a random number for Demand (0-100): "))  
    rn_demand = user_rn_demand if 0 <= user_rn_demand <= 100 else randrange(100)  
    day_by_day.append(rn_demand)
    _demand()

def _demand(): 
    global demand
    if NT == "poor" and rn_demand < 45:
        demand = 40
    elif NT == "poor" and rn_demand < 67:
        demand = 50
    elif NT == "poor" and rn_demand < 83:
        demand = 60
    elif NT == "poor" and rn_demand < 95:
        demand = 70
    elif NT == "poor" and rn_demand < 101:
        demand = 80
    elif NT == "fair" and rn_demand < 11:
        demand = 40
    elif NT == "fair" and rn_demand < 29:
        demand = 50
    elif NT == "fair" and rn_demand < 69:
        demand = 60
    elif NT == "fair" and rn_demand < 89:
        demand = 70
    elif NT == "fair" and rn_demand < 97:
        demand = 80
    elif NT == "fair" and rn_demand < 101:
        demand = 90
    elif NT == "good" and rn_demand < 4:
        demand = 40
    elif NT == "good" and rn_demand < 9:
        demand = 50
    elif NT == "good" and rn_demand < 24:
        demand = 60
    elif NT == "good" and rn_demand < 44:
        demand = 70
    elif NT == "good" and rn_demand < 79:
        demand = 80
    elif NT == "good" and rn_demand < 94:
        demand = 90
    elif NT == "good" and rn_demand < 101:
        demand = 100
    else:
        demand = 0
    
    day_by_day.append(demand)
    _revenue() 
    
def _revenue(): 
    global revenue
    if demand >= 90 :
        revenue = 45
    else :
        revenue = demand * .5
    day_by_day.append(revenue)
    profit_lost() 
    
def profit_lost(): 
    global lp
    if demand > 90:
        lp = (demand - 90) * .17
    else:
        lp = 0
    day_by_day.append(round(lp, 2))
    Scrap() 

def Scrap(): 
    global scrap
    if demand < 90:
        scrap = (90 - demand) * .07
    else:
        scrap = 0
    day_by_day.append(scrap)
    daily_profit()

def daily_profit(): 
    global dp
    dp = revenue - purchase_value_of_90_np - lp + scrap
    day_by_day.append(round(dp, 2))
    day_by_day.append(purchase_value_of_90_np)
    all_day.append(day_by_day)
    
    
rn_for_nt(10) 


df = pd.DataFrame(all_day, columns=['Day', ' RN for NT ', ' NT ', ' RN for Demand ', ' Demand ', ' Revenue ', ' Lost Profit ', ' Scrap ', ' Daily Profit ', ' Purchase Value of 90'])
df = df.set_index('Day')
pd.set_option('display.colheader_justify', 'center')

print(df)

print("##################################################")
# Calculate and print the total daily profit
total_profit = df[' Daily Profit '].sum()
print("Total Daily Profit: $", total_profit)

# Extract demand and profit data for plotting
demand = df[' Demand ']
profit = df[' Daily Profit ']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(demand, profit, marker='o', linestyle='-')
plt.xlabel('Demand (Number of Purchased Newspapers)')
plt.ylabel('Daily Profit')
plt.title('Demand vs. Profit (90 Newspapers)')
plt.grid(True)

# Display the plot
plt.show()


# In[16]:


# Simulation for 10 days with 80 newspapaer
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt

day_by_day = []
all_day = []
rn_for_NT = 0
NT = 0
rn_demand = 0

demand = 0
revenue = 0
lp = 0
scrap = 0
purchase_value_of_80_np = round((.33 * 80), 2)
dp = 0

def rn_for_nt(k):
    global day_by_day, rn_for_NT
    for i in range(k):
        day_by_day = [] 
        user_rn_nt = int(input("Enter a random number for NT (0-100): "))  
        rn_for_NT = user_rn_nt if 0 <= user_rn_nt <= 100 else randrange(100)  
        day_by_day.append(i + 1)
        day_by_day.append(rn_for_NT)
        type_of_news_day()

def type_of_news_day():
    global NT
    if rn_for_NT < 36:
        NT = "good"
    elif rn_for_NT < 81:
        NT = "fair"
    elif rn_for_NT < 101:
        NT = "poor"
    day_by_day.append(NT)
    rn_for_demand()

def rn_for_demand():
    global rn_demand
    user_rn_demand = int(input("Enter a random number for Demand (0-100): ")) 
    rn_demand = user_rn_demand if 0 <= user_rn_demand <= 100 else randrange(100)  
    day_by_day.append(rn_demand)
    _demand()

def _demand(): #5 function
    global demand
    if NT == "poor" and rn_demand < 45:
        demand = 40
    elif NT == "poor" and rn_demand < 67:
        demand = 50
    elif NT == "poor" and rn_demand < 83:
        demand = 60
    elif NT == "poor" and rn_demand < 95:
        demand = 70
    elif NT == "poor" and rn_demand < 101:
        demand = 80
    elif NT == "fair" and rn_demand < 11:
        demand = 40
    elif NT == "fair" and rn_demand < 29:
        demand = 50
    elif NT == "fair" and rn_demand < 69:
        demand = 60
    elif NT == "fair" and rn_demand < 89:
        demand = 70
    elif NT == "fair" and rn_demand < 97:
        demand = 80
    elif NT == "fair" and rn_demand < 101:
        demand = 90
    elif NT == "good" and rn_demand < 4:
        demand = 40
    elif NT == "good" and rn_demand < 9:
        demand = 50
    elif NT == "good" and rn_demand < 24:
        demand = 60
    elif NT == "good" and rn_demand < 44:
        demand = 70
    elif NT == "good" and rn_demand < 79:
        demand = 80
    elif NT == "good" and rn_demand < 94:
        demand = 90
    elif NT == "good" and rn_demand < 101:
        demand = 100
    else:
        demand = 0
    
    day_by_day.append(demand)
    _revenue()
    
def _revenue(): 
    global revenue
    if demand >= 80 :
        revenue = 40
    else :
        revenue = demand * .5
    day_by_day.append(revenue)
    profit_lost() 
    
def profit_lost(): 
    global lp
    if demand > 80:
        lp = (demand - 80) * .17
    else:
        lp = 0
    day_by_day.append(round(lp, 2))
    Scrap() 

def Scrap(): 
    global scrap
    if demand < 80:
        scrap = (80 - demand) * .07
    else:
        scrap = 0
    day_by_day.append(scrap)
    daily_profit() 

def daily_profit(): 
    global dp
    dp = revenue - purchase_value_of_80_np - lp + scrap
    day_by_day.append(round(dp, 2))
    day_by_day.append(purchase_value_of_80_np)
    all_day.append(day_by_day)
    
    
rn_for_nt(10) 


df = pd.DataFrame(all_day, columns=['Day', ' RN for NT ', ' NT ', ' RN for Demand ', ' Demand ', ' Revenue ', ' Lost Profit ', ' Scrap ', ' Daily Profit ', ' Purchase Value of 40'])
df = df.set_index('Day')
pd.set_option('display.colheader_justify', 'center')

print(df)

print("##################################################")
# Calculate and print the total daily profit
total_profit = df[' Daily Profit '].sum()
print("Total Daily Profit: $", total_profit)

# Extract demand and profit data for plotting
demand = df[' Demand ']
profit = df[' Daily Profit ']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(demand, profit, marker='o', linestyle='-')
plt.xlabel('Demand (Number of Purchased Newspapers)')
plt.ylabel('Daily Profit')
plt.title('Demand vs. Profit (80 Newspapers)')
plt.grid(True)

# Display the plot
plt.show()


# In[17]:


# Simulation for 10 days with 70 newspapaer
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt

day_by_day = []
all_day = []
rn_for_NT = 0
NT = 0
rn_demand = 0

demand = 0
revenue = 0
lp = 0
scrap = 0
purchase_value_of_70_np = round((.33 * 70), 2)
dp = 0

def rn_for_nt(k):
    global day_by_day, rn_for_NT
    for i in range(k):
        day_by_day = []  
        user_rn_nt = int(input("Enter a random number for NT (0-100): "))  
        rn_for_NT = user_rn_nt if 0 <= user_rn_nt <= 100 else randrange(100)  
        day_by_day.append(i + 1)
        day_by_day.append(rn_for_NT)
        type_of_news_day()

def type_of_news_day():
    global NT
    if rn_for_NT < 36:
        NT = "good"
    elif rn_for_NT < 81:
        NT = "fair"
    elif rn_for_NT < 101:
        NT = "poor"
    day_by_day.append(NT)
    rn_for_demand()

def rn_for_demand():
    global rn_demand
    user_rn_demand = int(input("Enter a random number for Demand (0-100): "))  
    rn_demand = user_rn_demand if 0 <= user_rn_demand <= 100 else randrange(100)  
    day_by_day.append(rn_demand)
    _demand()

def _demand():
    global demand
    if NT == "poor" and rn_demand < 45:
        demand = 40
    elif NT == "poor" and rn_demand < 67:
        demand = 50
    elif NT == "poor" and rn_demand < 83:
        demand = 60
    elif NT == "poor" and rn_demand < 95:
        demand = 70
    elif NT == "poor" and rn_demand < 101:
        demand = 80
    elif NT == "fair" and rn_demand < 11:
        demand = 40
    elif NT == "fair" and rn_demand < 29:
        demand = 50
    elif NT == "fair" and rn_demand < 69:
        demand = 60
    elif NT == "fair" and rn_demand < 89:
        demand = 70
    elif NT == "fair" and rn_demand < 97:
        demand = 80
    elif NT == "fair" and rn_demand < 101:
        demand = 90
    elif NT == "good" and rn_demand < 4:
        demand = 40
    elif NT == "good" and rn_demand < 9:
        demand = 50
    elif NT == "good" and rn_demand < 24:
        demand = 60
    elif NT == "good" and rn_demand < 44:
        demand = 70
    elif NT == "good" and rn_demand < 79:
        demand = 80
    elif NT == "good" and rn_demand < 94:
        demand = 90
    elif NT == "good" and rn_demand < 101:
        demand = 100
    else:
        demand = 0
    
    day_by_day.append(demand)
    _revenue() 
    
def _revenue(): 
    global revenue
    if demand >= 70 :
        revenue = 35
    else :
        revenue = demand * .5
    day_by_day.append(revenue)
    profit_lost() 
    
def profit_lost(): 
    global lp
    if demand > 70:
        lp = (demand - 70) * .17
    else:
        lp = 0
    day_by_day.append(round(lp, 2))
    Scrap() 

def Scrap():
    global scrap
    if demand < 70:
        scrap = (70 - demand) * .07
    else:
        scrap = 0
    day_by_day.append(scrap)
    daily_profit() 

def daily_profit(): 
    global dp
    dp = revenue - purchase_value_of_70_np - lp + scrap
    day_by_day.append(round(dp, 2))
    day_by_day.append(purchase_value_of_70_np)
    all_day.append(day_by_day)
    
    
rn_for_nt(10) 


df = pd.DataFrame(all_day, columns=['Day', ' RN for NT ', ' NT ', ' RN for Demand ', ' Demand ', ' Revenue ', ' Lost Profit ', ' Scrap ', ' Daily Profit ', ' Purchase Value of 40'])
df = df.set_index('Day')
pd.set_option('display.colheader_justify', 'center')

print(df)

print("##################################################")
# Calculate and print the total daily profit
total_profit = df[' Daily Profit '].sum()
print("Total Daily Profit: $", total_profit)

# Extract demand and profit data for plotting
demand = df[' Demand ']
profit = df[' Daily Profit ']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(demand, profit, marker='o', linestyle='-')
plt.xlabel('Demand (Number of Purchased Newspapers)')
plt.ylabel('Daily Profit')
plt.title('Demand vs. Profit (70 Newspapers)')
plt.grid(True)

# Display the plot
plt.show()


# In[18]:


# Simulation for 10 days with 60 newspapaer
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt

day_by_day = []
all_day = []
rn_for_NT = 0
NT = 0
rn_demand = 0

demand = 0
revenue = 0
lp = 0
scrap = 0
purchase_value_of_60_np = round((.33 * 60), 2)
dp = 0

def rn_for_nt(k):
    global day_by_day, rn_for_NT
    for i in range(k):
        day_by_day = []  
        user_rn_nt = int(input("Enter a random number for NT (0-100): "))  
        rn_for_NT = user_rn_nt if 0 <= user_rn_nt <= 100 else randrange(100)  
        day_by_day.append(i + 1)
        day_by_day.append(rn_for_NT)
        type_of_news_day()

def type_of_news_day():
    global NT
    if rn_for_NT < 36:
        NT = "good"
    elif rn_for_NT < 81:
        NT = "fair"
    elif rn_for_NT < 101:
        NT = "poor"
    day_by_day.append(NT)
    rn_for_demand()

def rn_for_demand():
    global rn_demand
    user_rn_demand = int(input("Enter a random number for Demand (0-100): "))  
    rn_demand = user_rn_demand if 0 <= user_rn_demand <= 100 else randrange(100) 
    day_by_day.append(rn_demand)
    _demand()

def _demand(): 
    global demand
    if NT == "poor" and rn_demand < 45:
        demand = 40
    elif NT == "poor" and rn_demand < 67:
        demand = 50
    elif NT == "poor" and rn_demand < 83:
        demand = 60
    elif NT == "poor" and rn_demand < 95:
        demand = 70
    elif NT == "poor" and rn_demand < 101:
        demand = 80
    elif NT == "fair" and rn_demand < 11:
        demand = 40
    elif NT == "fair" and rn_demand < 29:
        demand = 50
    elif NT == "fair" and rn_demand < 69:
        demand = 60
    elif NT == "fair" and rn_demand < 89:
        demand = 70
    elif NT == "fair" and rn_demand < 97:
        demand = 80
    elif NT == "fair" and rn_demand < 101:
        demand = 90
    elif NT == "good" and rn_demand < 4:
        demand = 40
    elif NT == "good" and rn_demand < 9:
        demand = 50
    elif NT == "good" and rn_demand < 24:
        demand = 60
    elif NT == "good" and rn_demand < 44:
        demand = 70
    elif NT == "good" and rn_demand < 79:
        demand = 80
    elif NT == "good" and rn_demand < 94:
        demand = 90
    elif NT == "good" and rn_demand < 101:
        demand = 100
    else:
        demand = 0
    
    day_by_day.append(demand)
    _revenue() 
    
def _revenue():
    global revenue
    if demand >= 60 :
        revenue = 30
    else :
        revenue = demand * .5
    day_by_day.append(revenue)
    profit_lost() 
    
def profit_lost(): 
    global lp
    if demand > 60:
        lp = (demand - 60) * .17
    else:
        lp = 0
    day_by_day.append(round(lp, 2))
    Scrap() 

def Scrap(): 
    global scrap
    if demand < 60:
        scrap = (60 - demand) * .07
    else:
        scrap = 0
    day_by_day.append(scrap)
    daily_profit() 

def daily_profit(): 
    global dp
    dp = revenue - purchase_value_of_60_np - lp + scrap
    day_by_day.append(round(dp, 2))
    day_by_day.append(purchase_value_of_60_np)
    all_day.append(day_by_day)
   
    
rn_for_nt(10) 


df = pd.DataFrame(all_day, columns=['Day', ' RN for NT ', ' NT ', ' RN for Demand ', ' Demand ', ' Revenue ', ' Lost Profit ', ' Scrap ', ' Daily Profit ', ' Purchase Value of 40'])
df = df.set_index('Day')
pd.set_option('display.colheader_justify', 'center')

print(df)

print("##################################################")
# Calculate and print the total daily profit
total_profit = df[' Daily Profit '].sum()
print("Total Daily Profit: $", total_profit)

# Extract demand and profit data for plotting
demand = df[' Demand ']
profit = df[' Daily Profit ']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(demand, profit, marker='o', linestyle='-')
plt.xlabel('Demand (Number of Purchased Newspapers)')
plt.ylabel('Daily Profit')
plt.title('Demand vs. Profit (60 Newspapers)')
plt.grid(True)

# Display the plot
plt.show()


# In[19]:


# Simulation for 10 days with 50 newspapaer
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt

day_by_day = []
all_day = []
rn_for_NT = 0
NT = 0
rn_demand = 0

demand = 0
revenue = 0
lp = 0
scrap = 0
purchase_value_of_50_np = round((.33 * 50), 2)
dp = 0

def rn_for_nt(k):
    global day_by_day, rn_for_NT
    for i in range(k):
        day_by_day = []  
        user_rn_nt = int(input("Enter a random number for NT (0-100): "))  
        rn_for_NT = user_rn_nt if 0 <= user_rn_nt <= 100 else randrange(100)  
        day_by_day.append(i + 1)
        day_by_day.append(rn_for_NT)
        type_of_news_day()

def type_of_news_day():
    global NT
    if rn_for_NT < 36:
        NT = "good"
    elif rn_for_NT < 81:
        NT = "fair"
    elif rn_for_NT < 101:
        NT = "poor"
    day_by_day.append(NT)
    rn_for_demand()

def rn_for_demand():
    global rn_demand
    user_rn_demand = int(input("Enter a random number for Demand (0-100): "))  
    rn_demand = user_rn_demand if 0 <= user_rn_demand <= 100 else randrange(100)  
    day_by_day.append(rn_demand)
    _demand()

def _demand(): 
    global demand
    if NT == "poor" and rn_demand < 45:
        demand = 40
    elif NT == "poor" and rn_demand < 67:
        demand = 50
    elif NT == "poor" and rn_demand < 83:
        demand = 60
    elif NT == "poor" and rn_demand < 95:
        demand = 70
    elif NT == "poor" and rn_demand < 101:
        demand = 80
    elif NT == "fair" and rn_demand < 11:
        demand = 40
    elif NT == "fair" and rn_demand < 29:
        demand = 50
    elif NT == "fair" and rn_demand < 69:
        demand = 60
    elif NT == "fair" and rn_demand < 89:
        demand = 70
    elif NT == "fair" and rn_demand < 97:
        demand = 80
    elif NT == "fair" and rn_demand < 101:
        demand = 90
    elif NT == "good" and rn_demand < 4:
        demand = 40
    elif NT == "good" and rn_demand < 9:
        demand = 50
    elif NT == "good" and rn_demand < 24:
        demand = 60
    elif NT == "good" and rn_demand < 44:
        demand = 70
    elif NT == "good" and rn_demand < 79:
        demand = 80
    elif NT == "good" and rn_demand < 94:
        demand = 90
    elif NT == "good" and rn_demand < 101:
        demand = 100
    else:
        demand = 0
    
    day_by_day.append(demand)
    _revenue() 
    
def _revenue(): 
    global revenue
    if demand >= 50 :
        revenue = 25
    else :
        revenue = demand * .5
    day_by_day.append(revenue)
    profit_lost() 
    
def profit_lost():
    global lp
    if demand > 50:
        lp = (demand - 50) * .17
    else:
        lp = 0
    day_by_day.append(round(lp, 2))
    Scrap() 

def Scrap(): 
    global scrap
    if demand < 50:
        scrap = (50 - demand) * .07
    else:
        scrap = 0
    day_by_day.append(scrap)
    daily_profit() 

def daily_profit(): 
    global dp
    dp = revenue - purchase_value_of_50_np - lp + scrap
    day_by_day.append(round(dp, 2))
    day_by_day.append(purchase_value_of_50_np)
    all_day.append(day_by_day)
    
    
rn_for_nt(10) 


df = pd.DataFrame(all_day, columns=['Day', ' RN for NT ', ' NT ', ' RN for Demand ', ' Demand ', ' Revenue ', ' Lost Profit ', ' Scrap ', ' Daily Profit ', ' Purchase Value of 40'])
df = df.set_index('Day')
pd.set_option('display.colheader_justify', 'center')

print(df)

print("##################################################")
# Calculate and print the total daily profit
total_profit = df[' Daily Profit '].sum()
print("Total Daily Profit: $", total_profit)

# Extract demand and profit data for plotting
demand = df[' Demand ']
profit = df[' Daily Profit ']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(demand, profit, marker='o', linestyle='-')
plt.xlabel('Demand (Number of Purchased Newspapers)')
plt.ylabel('Daily Profit')
plt.title('Demand vs. Profit (50 Newspapers)')
plt.grid(True)

# Display the plot
plt.show()


# In[20]:


# Simulation for 10 days with 40 newspapaer
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt

day_by_day = []
all_day = []
rn_for_NT = 0
NT = 0
rn_demand = 0

demand = 0
revenue = 0
lp = 0
scrap = 0
purchase_value_of_40_np = round((.33 * 40), 2)
dp = 0

def rn_for_nt(k):
    global day_by_day, rn_for_NT
    for i in range(k):
        day_by_day = []  
        user_rn_nt = int(input("Enter a random number for NT (0-100): "))  
        rn_for_NT = user_rn_nt if 0 <= user_rn_nt <= 100 else randrange(100)  
        day_by_day.append(i + 1)
        day_by_day.append(rn_for_NT)
        type_of_news_day()

def type_of_news_day():
    global NT
    if rn_for_NT < 36:
        NT = "good"
    elif rn_for_NT < 81:
        NT = "fair"
    elif rn_for_NT < 101:
        NT = "poor"
    day_by_day.append(NT)
    rn_for_demand()

def rn_for_demand():
    global rn_demand
    user_rn_demand = int(input("Enter a random number for Demand (0-100): "))  
    rn_demand = user_rn_demand if 0 <= user_rn_demand <= 100 else randrange(100)  
    day_by_day.append(rn_demand)
    _demand()

def _demand(): 
    global demand
    if NT == "poor" and rn_demand < 45:
        demand = 40
    elif NT == "poor" and rn_demand < 67:
        demand = 50
    elif NT == "poor" and rn_demand < 83:
        demand = 60
    elif NT == "poor" and rn_demand < 95:
        demand = 70
    elif NT == "poor" and rn_demand < 101:
        demand = 80
    elif NT == "fair" and rn_demand < 11:
        demand = 40
    elif NT == "fair" and rn_demand < 29:
        demand = 50
    elif NT == "fair" and rn_demand < 69:
        demand = 60
    elif NT == "fair" and rn_demand < 89:
        demand = 70
    elif NT == "fair" and rn_demand < 97:
        demand = 80
    elif NT == "fair" and rn_demand < 101:
        demand = 90
    elif NT == "good" and rn_demand < 4:
        demand = 40
    elif NT == "good" and rn_demand < 9:
        demand = 50
    elif NT == "good" and rn_demand < 24:
        demand = 60
    elif NT == "good" and rn_demand < 44:
        demand = 70
    elif NT == "good" and rn_demand < 79:
        demand = 80
    elif NT == "good" and rn_demand < 94:
        demand = 90
    elif NT == "good" and rn_demand < 101:
        demand = 100
    else:
        demand = 0
    
    day_by_day.append(demand)
    _revenue() 
    
def _revenue(): 
    global revenue
    if demand >= 40 :
        revenue = 20
    else :
        revenue = demand * .5
    day_by_day.append(revenue)
    profit_lost() 
    
def profit_lost(): 
    global lp
    if demand > 40:
        lp = (demand - 40) * .17
    else:
        lp = 0
    day_by_day.append(round(lp, 2))
    Scrap()

def Scrap(): 
    global scrap
    if demand < 40:
        scrap = (40 - demand) * .07
    else:
        scrap = 0
    day_by_day.append(scrap)
    daily_profit() 

def daily_profit(): 
    global dp
    dp = revenue - purchase_value_of_40_np - lp + scrap
    day_by_day.append(round(dp, 2))
    day_by_day.append(purchase_value_of_40_np)
    all_day.append(day_by_day)
    
    
rn_for_nt(10) 


df = pd.DataFrame(all_day, columns=['Day', ' RN for NT ', ' NT ', ' RN for Demand ', ' Demand ', ' Revenue ', ' Lost Profit ', ' Scrap ', ' Daily Profit ', ' Purchase Value of 40'])
df = df.set_index('Day')
pd.set_option('display.colheader_justify', 'center')

print(df)

print("##################################################")
# Calculate and print the total daily profit
total_profit = df[' Daily Profit '].sum()
print("Total Daily Profit: $", total_profit)

# Extract demand and profit data for plotting
demand = df[' Demand ']
profit = df[' Daily Profit ']

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(demand, profit, marker='o', linestyle='-')
plt.xlabel('Demand (Number of Purchased Newspapers)')
plt.ylabel('Daily Profit')
plt.title('Demand vs. Profit (40 Newspapers)')
plt.grid(True)

# Display the plot
plt.show()


# In[ ]:




