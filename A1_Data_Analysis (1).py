#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Create New Cond Col


# In[3]:


import pandas as pd

# Create a sample DataFrame
data = {'sales': [1000, 800, 1200, 1500],
        'profit': [500, 400, 600, 750],
        'ship_mode': ['Same Day', 'First Class', 'Standard Class', 'Second Class']}
df = pd.DataFrame(data)

# Define a function to calculate the surcharge
def calculate_surcharge(ship_mode):
    if ship_mode == "Same Day":
        return 0.2
    elif ship_mode == "First Class":
        return 0.1
    elif ship_mode == "Standard Class":
        return 0.05
    else:
        return 0

df['surcharge'] = df['ship_mode'].apply(calculate_surcharge)


df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])


print(df)


# In[ ]:




