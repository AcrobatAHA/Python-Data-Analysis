#!/usr/bin/env python
# coding: utf-8

# # Weather Data analysis in python

# # About Data: Here The Weather dataset is a time-series data set with per-hours information about the weather conditions at a particular location.It records temperature, Dew point temperature,Relative humidity, Wind speed,Visibility, Pressure and Conditions.
# 
# This data is available as a .csv file and To analyze this dataset I'm using the Pandas DataFrame.

# In[1]:


import pandas as pd


# In[2]:


Weather_DataSet = pd.read_csv(r"C:\Users\ASUS\Desktop\Power BI\Weather DataSet\Weather Data.csv")


# In[16]:


Weather_DataSet


# # How to Analyze DataFrames?
# 
# .head()
# 
# It shows the 1st N rows in the data(By default N=5)

# In[19]:


Weather_DataSet.head(10)


# # .shape
# 
# It shows the total no of Rows and columns in the dataframe

# In[20]:


Weather_DataSet.shape


# # .index
# 
# This attribute provides the index of the dataframe

# In[21]:


Weather_DataSet.index


# # .columns
# 
# To show the name of each column

# In[22]:


Weather_DataSet.columns

.dtypes

Shows the datatype of each column
# In[23]:


Weather_DataSet.dtypes


# # .unique()
# 
# Shows the unique values of a single column only.

# In[24]:


Weather_DataSet['Weather'].unique


# In[25]:


Weather_DataSet['Weather'].unique()


# # .nunique()
# 
# Shows the total number of unique values of every column. It can be applied on a single column or full dataframe

# In[26]:


Weather_DataSet.nunique()


# In[28]:


Weather_DataSet['Wind Speed_km/h'].nunique()


# # .count()
# 
# Shows the total number of non-null values of each column. It can be applied on a single column or entire dataframe

# In[29]:


Weather_DataSet.count()


# In[32]:


Weather_DataSet['Weather'].count()


# # .Value_counts()
# 
# Shows the unique values with their count. It can be applied on a single column only

# In[36]:


Weather_DataSet['Weather'].value_counts()


# # .info()
# 
# provides basic info about the dataframe

# In[37]:


Weather_DataSet.info()


# # 1 Find all the unique wind speed values of the data?

# In[5]:


Weather_DataSet['Wind Speed_km/h'].unique()


# In[8]:


print("Total unique values of the wind speed is=",Weather_DataSet['Wind Speed_km/h'].nunique())


# # 2 Find number of times when the weather is exactly clear?
There are 3 ways to solve this problem value_counts(), filtering and groupby command
# In[9]:


Weather_DataSet['Weather'].value_counts()


# In[14]:


#filtering
Weather_DataSet[Weather_DataSet['Weather']=='Clear']


# In[15]:


#groupby()
Weather_DataSet.groupby('Weather').get_group('Clear') #get_group used to pick a particular element from the column 


# # 3 Find the number of times when the wind speed was 4 km/h?

# In[17]:


Weather_DataSet[Weather_DataSet['Wind Speed_km/h']==4]


# # 4 Find out all the null values in the data?
There are 2 ways to solve this problem using isnull() and notnull()
# In[18]:


Weather_DataSet.isnull().sum()


# In[19]:


Weather_DataSet.notnull().sum()


# # 5 Rename the column name Weather to 'Weather Condition' 

# In[35]:


Weather_DataSet.rename(columns={'Weather':'Weather Condition'}) #This comand replace the name temporary, to do it parmanently we have to use inplace=Ture


# In[37]:


Weather_DataSet.rename(columns={'Weather':'Weather Condition'},inplace=True)


# # 6 what is the mean value of 'Visibility' column?

# In[38]:


Weather_DataSet['Visibility_km'].mean()


# # 7 what is the Standard deviation value of 'Pressure' column?

# In[39]:


Weather_DataSet['Press_kPa'].std()


# # 8 What is the Variance of 'Relative Humidity' in this data ?

# In[40]:


Weather_DataSet['Rel Hum_%'].var()


# # 9 Find all instances when 'Snow' was recorded?

# # There are 3 ways to solve this problem value_counts(), filtering and str.contains() command

# In[8]:


Weather_DataSet['Weather'].value_counts()


# In[9]:


#Filtering
Weather_DataSet[Weather_DataSet['Weather']=='Snow']


# In[10]:


#str.contains it shows all the data those have Snow key word
Weather_DataSet[Weather_DataSet['Weather'].str.contains('Snow')]


# In[13]:


Weather_DataSet[Weather_DataSet['Weather'].str.contains('Snow')].tail(25)


# # 10 Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'

# In[16]:


Weather_DataSet[(Weather_DataSet['Wind Speed_km/h']>24) & (Weather_DataSet['Visibility_km']==25)].head(5)


# # 11 What is the Mean value of each column against each 'Weather Condition'?

# In[20]:


Weather_DataSet.groupby('Weather').mean()


# # 12 What is the Minimum & Maximum value of each column against each 'Weather Condition'?

# In[21]:


Weather_DataSet.groupby('Weather').max()


# In[22]:


Weather_DataSet.groupby('Weather').min()


# # 13 Show all the Records where Weather Condition is Fog

# In[24]:


Weather_DataSet[Weather_DataSet['Weather']=='Fog']


# # 14 Find all instances when 'Weather is Clear' or 'Visibility is above 40'

# In[30]:


Weather_DataSet[(Weather_DataSet['Weather']=='Clear') | (Weather_DataSet['Visibility_km']>40)]


# # 15 Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'

# In[31]:


Weather_DataSet[(Weather_DataSet['Weather']=='Clear') & (Weather_DataSet['Rel Hum_%']>50) | (Weather_DataSet['Visibility_km']>40)]

