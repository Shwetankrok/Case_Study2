#!/usr/bin/env python
# coding: utf-8

# # Case Study 2

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv("C:/Users/shwer/OneDrive/Desktop/archive/casestudy.csv")


# In[3]:


data.head()


# In[4]:


# Answering question


# # 1: Total revenue for the current year

# In[5]:



yearly_sales = data.groupby(['year'])['net_revenue'].sum() #sum function
print(yearly_sales)


# In[6]:


year_sales=yearly_sales.to_frame() # Since it is a Series conmverting to Dataframe to plot further


# In[7]:


year_sales


# In[8]:


year_sales.reset_index(inplace=True)


# In[9]:


year_sales


# In[10]:


sns.barplot(x='year',y='net_revenue',hue='year',data=year_sales)


# # Observations: 
# <b><br> 2017 year has highest Net Revenue 31 M while 2016 has lowest Net Revenue of 25 M </br></b>

# In[11]:


# Question2: New Customer Revenue 
# Finding Net Revenue of new customers only which are not present in previous years


# In[12]:


g1=data.groupby(['year','customer_email'])['net_revenue'].sum()


# In[13]:


g1


# In[14]:


g1.to_csv("C:/Users/shwer/OneDrive/Desktop/archive/yearly_revenue_cust.csv")


# In[15]:


df=pd.read_csv("C:/Users/shwer/OneDrive/Desktop/archive/yearly_revenue_cust.csv")


# In[16]:


df


# In[17]:


# Reference: https://stackoverflow.com/questions/53672456/finding-new-existing-customers-from-a-dataframe
# Findind duplicates
a=df.assign(Occurence=np.where(~df['customer_email'].duplicated(),'New','Existing'))


# In[18]:


a


# In[19]:


a[(a['customer_email']=='aaaqpobaaa@gmail.com')]


# In[20]:


x=a[a['Occurence']=='Existing']


# In[21]:


x


# In[22]:


x1=a[a['Occurence']=='New']


# In[23]:



new_customers = x1.groupby(['year'])['net_revenue'].sum() #sum function
print(new_customers)


# In[24]:


new_cust=new_customers.to_frame() # Since it is a Series conmverting to Dataframe to plot further


# In[25]:


new_cust.reset_index(inplace=True)


# In[26]:


new_cust


# In[27]:


sns.barplot(x='year',y='net_revenue',hue='year',data=new_cust)


# # Observations:
# <br>New Customer Revenue for 2016: 18.24 M </br>
# <br>New Customer Revenue for 2017: 28.67 M </br>

# # Question: Total Customers Per Year

# In[28]:


data=pd.read_csv("C:/Users/shwer/OneDrive/Desktop/archive/casestudy.csv")
d_2015=data[data['year']==2015]
d_2016=data[data['year']==2016]
d_2017=data[data['year']==2017]


# In[29]:


print(len(d_2015['customer_email'].unique()))
print(len(d_2016['customer_email'].unique()))
print(len(d_2017['customer_email'].unique()))


# In[30]:


x=[231294,204646,249987]
y=[2015,2016,2017]
sns.barplot(x=y,y=x)


# # Observations:
# <br> Total Unique Customers in 2015 are 231294 </br>
# <br> Total Unique Customers in 2016 are 204646 </br>
# <br> Total Unique Customers in 2017 are 249987 </br>

# # Question : Count of New Customers per year

# In[31]:


# Question : Count of New Customers per year
x1=a[a['Occurence']=='New']
new_2015=x1[x1['year']==2015]
new_2016=x1[x1['year']==2016]
new_2017=x1[x1['year']==2017]


# In[32]:


print(len(new_2015['customer_email'].unique()))
print(len(new_2016['customer_email'].unique()))
print(len(new_2017['customer_email'].unique()))


# In[33]:


x=[231294,145062,228262]
y=[2015,2016,2017]
sns.barplot(x=y,y=x)


# # Observations: 
# <br> Total Unique New Customers in 2015 are 231294 </br>
# <br> Total Unique New Customers in 2016 are 145062 </br>
# <br> Total Unique New Customers in 2017 are 228262 </br>

# # Question: Lost Customers
# 

# In[34]:


a


# In[35]:


df=pd.read_csv("C:/Users/shwer/OneDrive/Desktop/archive/yearly_revenue_cust.csv")
l_2015=df[df['year']==2015]
l_2016=df[df['year']==2016]
l_2017=df[df['year']==2017]


# In[36]:


l_2015[~l_2015['customer_email'].isin(l_2016['customer_email'])]


# In[37]:


# Observations: As 2015 total Customers are 231294
# Lost Customers i.e. Customers which are present in 2015 but absent in 2016 = 59584


# In[38]:


l_2016[~l_2016['customer_email'].isin(l_2017['customer_email'])]


# In[39]:


# Observations: As 2016 total Customers are 204646
# Lost Customers i.e. Customers which are present in 2016 but absent in 2017 = 183687


# # Observations:
# <b><br> Lost Customers i.e. Customers which are present in 2015 but absent in 2016 = 59584 </br></b>
# <b><br> Lost Customers i.e. Customers which are present in 2016 but absent in 2017 = 183687 </br></b>

# # Question: Existing Customer Growth

# In[40]:


df=pd.read_csv("C:/Users/shwer/OneDrive/Desktop/archive/yearly_revenue_cust.csv")
df_2015=df[df['year']==2015]
df_2016=df[df['year']==2016]
df_2017=df[df['year']==2017]


# In[41]:


df_2015


# In[42]:


z=df_2015.merge(df_2016, left_on='customer_email', right_on='customer_email')


# In[43]:


z


# In[44]:


z['Existing_Customer_growth']=z['net_revenue_y']-z['net_revenue_x']


# In[45]:


z


# In[74]:


z['Existing_Customer_growth'].sum()


# In[75]:


# Merge z with 2017 year data
z1=df_2016.merge(df_2017, left_on='customer_email', right_on='customer_email')


# In[76]:


z1


# In[77]:


z1['Existing_Customer_growth_2016-2017']=z1['net_revenue_y']-z1['net_revenue_x']


# In[78]:


z1


# In[80]:


z1['Existing_Customer_growth_2016-2017'].sum()


# # Observations:
# <b><br> Existing Customer Growth where Revenue 2016 - Revenue 2015 for customers present in both years is 20335.4 in Total</br></b>
# <b><br> Existing Customer Growth where Revenue 2017 - Revenue 2016 for customers present in both years is 20611.34 in Total </br></b>

# # Existing Customer Current Revenue
# ##### Getting Total revenue in 2015 for customers which are also present in 2016

# In[81]:


z['net_revenue_x'].sum()


# In[82]:


z['net_revenue_y'].sum()


# # Observations:
# <br> Total Revenue in 2015 for customers which are present in 2015 and 2016 both is 7.46 M </br>
# <br> Total Revenue in 2016 for customers which are present in 2015 and 2016 both is 7.48 M </br>

# ##### Getting Total revenue in 2016 for customers which are also present in 2017

# In[83]:


z1['net_revenue_x'].sum()


# In[84]:


z1['net_revenue_y'].sum()


# # Observations:
# <br> Total Revenue in 2016 for customers which are present in 2017 and 2016 both is 2.62 M </br>
# <br> Total Revenue in 2017 for customers which are present in 2017 and 2016 both is 2.64 M </br>

# # Summary
# <br> Total Revenue in 2015 for customers which are present in 2015 and 2016 both is 7.46 M </br>
# <br> Total Revenue in 2016 for customers which are present in 2015 and 2016 both is 7.48 M </br>
# <br> Total Revenue in 2016 for customers which are present in 2017 and 2016 both is 2.62 M </br>
# <br> Total Revenue in 2017 for customers which are present in 2017 and 2016 both is 2.64 M </br>

# # Question: Revenue Lost from attrition
# ## I am finding Revenue lost each year </b>

# In[50]:


year_sales


# In[51]:


year_sales['Difference']=0


# In[52]:


year_sales


# In[53]:


for index,row in year_sales.iterrows():
        if index == 0:
            continue
        elif row['year'] == 2016:
            year_sales['Difference'][index] =year_sales['net_revenue'][index]-year_sales['net_revenue'][index-1]
        else:
            year_sales['Difference'][index] = year_sales['net_revenue'][index]-year_sales['net_revenue'][index-1]


# In[54]:


year_sales


# # Observations:
# <br><b> So Year 2016 made a loss of 3305805 of Net Revenue from year 2015</b> </br>
# <br><b> Year 2017 made a profit of 5686551 of Net Revenue from year 2016 </b></br>

# # Now Answering the same question where Finding Total Revenue lost in the year 2016(Customers which are absent in year 2016 but present in 2015) and similarly for 2017

# In[55]:


df=pd.read_csv("C:/Users/shwer/OneDrive/Desktop/archive/yearly_revenue_cust.csv")
l_2015=df[df['year']==2015]
l_2016=df[df['year']==2016]
l_2017=df[df['year']==2017]


# In[56]:


q=l_2015[~l_2015['customer_email'].isin(l_2016['customer_email'])]


# In[57]:


q['net_revenue'].sum()


# In[58]:


q1=l_2016[~l_2016['customer_email'].isin(l_2017['customer_email'])]


# In[59]:


q1['net_revenue'].sum()


# # Observations: 
# <b><br>Revenue lost from customers which are present in 2015 but not in 2016 is 21 M </br></b>
# <b><br>Revenue lost from customers which are present in 2016 but not in 2017 is 23 M </br></b>

# # Finding customers which are present in all 3 years and contribute most to Net Revenue

# In[60]:


z1


# In[61]:


z1['Total_revenue']=z1['net_revenue_x']+ z1['net_revenue_y']+z1['net_revenue']


# In[62]:


z1


# In[65]:


d=z1.sort_values(by='Total_revenue', ascending=False)


# In[69]:


c=d.head(5)


# In[72]:


# Reference: https://drawingfromdata.com/seaborn/matplotlib/visualization/rotate-axis-labels-matplotlib-seaborn.html
plt.figure(figsize=(10,5))
chart = sns.barplot(x='customer_email',y='Total_revenue',data=c)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45,fontsize='x-large')


# # Observations:
# <br> These 5 customers are there for 3 years and contribute most to the Net_Revenue </br> 

# In[ ]:




