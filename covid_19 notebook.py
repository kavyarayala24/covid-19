#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv (r"C:/Users/hp/Desktop/country_wise_latest.csv")#import dataset
df


# In[16]:


df.head()#first fine rows


# In[17]:


df.tail()#last five rows


# In[18]:


df.shape#total number of rows and columns#last


# In[19]:


df.dtypes#find datatypes


# In[20]:


df.info()#get all information about our dataset


# In[21]:


df.isnull().sum()# find null values


# In[22]:


sns.heatmap(df.isna())#to show the null values in visualise


# In[23]:


print(df.columns)#it shows colomns name in data set


# In[24]:


df.describe()


# In[26]:


df.columns


# In[30]:


df['Country/Region'].unique() # it shows unique values in selected colomn


# In[22]:


df.dropna()# drop null values


# In[5]:


df['Confirmed'].unique()


# In[9]:


df['Confirmed'].value_counts()#count the all values


# In[7]:


df['Deaths'].unique()


# In[6]:


df['Deaths'].value_counts()


# In[10]:


df.corr()# it shows correaltion 


# # maps

# In[12]:


sns.countplot(df['Deaths'])


# In[24]:


sns.displot(df['Deaths'])


# In[25]:


sns.kdeplot(df['Deaths'])


# In[30]:


plt.xticks(rotation=100)
plt.show()


# In[106]:


sns.barplot(df['Deaths'],df['Confirmed'])


# In[32]:


df.groupby(['Deaths']).mean()


# In[33]:


df.groupby(['Deaths']).median()


# In[99]:


labels=df['Deaths'].value_counts().index
colors=['blue','red','green']
sizes=df['Deaths'].value_counts().values
plt.figure(figsize=(5,5))
plt.title('Deaths',fontsize=20)


# In[69]:


plt.pie(sizes,labels=labels,colors=colors,autopct='%2.1f%%')
plt.show()


# ## 

# In[77]:


plt.figure(figsize=(12,10))
sns.set(style='darkgrid')
sns.boxplot(y='Deaths', x='Confirmed',data=df)
plt.show()


# In[95]:


x=df['New deaths']
y=df['New recovered']
plt.title('Barplot',fontsize=10)
plt.xlabel('New deaths')
plt.ylabel('New recovered')
plt.bar(x,y,width=100,color='r')


# In[ ]:




