
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **weather phenomena** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **weather phenomena**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **weather phenomena**?  For this category you might want to consider seasonal changes, natural disasters, or historical trends.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[178]:



#This Climate Dataset fro 1901 to 2012 is taken from http//:www.ncdc.noaa.gov/ 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#plt.style.use('seaborn-colorblind')
plt.figure()


# In[168]:

df = pd.read_excel("pr5_1900_2012.xls",names=['Rainfall','Year','Month','Country','ISO3','ISO2'])
df = pd.DataFrame(df)
print(df.head())


# In[169]:

#df.drop('ISO3',axis=1,inplace=True)
df.drop(df.columns[[4, 5]], axis=1,inplace=True) 

type(df)


# In[170]:

#df.set_index('Month',inplace=True)
df2 = pd.DataFrame()
df2["Avg Rain"] = df["Rainfall"]
df2["Month"] = df['Month']
print(df2.head())
df2 = df2.groupby('Month')['Avg Rain'].mean()
print(df2)
#print(df.groupby('Month', as_index=False)['Rainfall'].mean())
#df2['Avg_Rain'] = df.groupby(df.index)[Rainfall].mean()
#df2=[]
#for i in range(1,13):
#    df2.append(np.mean(df.loc[df['Month']==i]['Rainfall (mm)']))
#print(df.columns.values)


# In[165]:

df3 = pd.read_excel("tas5_1900_2012.xls",names=['Temperature','Year','Month','Country','ISO3','ISO2'])
df3 = pd.DataFrame(df3)
print(df3.head())


# In[166]:

df3.drop(df3.columns[[4, 5]], axis=1,inplace=True) 

type(df3)


# In[167]:

df4 = pd.DataFrame()
df4["Avg Temperature"] = df3["Temperature"]
df4["Month"] = df3['Month']
print(df4.head())
df5 = pd.DataFrame()
df5['Max Temp'] = df4.groupby('Month')['Avg Temperature'].max()
df5['Min Temp'] = df4.groupby('Month')['Avg Temperature'].min()
df4 = df4.groupby('Month')['Avg Temperature'].mean()

print(df5)


# In[171]:

df4 = pd.DataFrame(df4)
df2 = pd.DataFrame(df2)
all_data = df2.join(df4)
all_data = all_data.join(df5)
print(all_data)


# In[184]:

x = ['Jan','Feb','Apr','Jun','Aug','Oct','Dec']
ax=plt.gca()
ax2 = ax.twinx()
ax.bar(all_data.index, all_data['Avg Rain'], width = 0.3, color='b')
ax2.plot(all_data.index,all_data['Avg Temperature'],'-',all_data.index,all_data['Max Temp'],'-',all_data.index,all_data['Min Temp'],'-')
#ax=plt.gca()
#ax2 = ax.twinx()
ax.set_xticklabels(x)
plt.title("Correlation of Monthly Avg Rainfall vs Monthly Avg Temp in US from 1901-2012")
ax.set_ylabel("Rainfall (mm)")
ax2.set_ylabel("Temperature (deg C)")
ax.yaxis.label.set_color('b')
ax.tick_params(axis='y', colors='b')
plt.legend(['Avg Temperature','Max Temperature','Min Temperature'])
plt.show()


# In[189]:

plt.figure()
_=pd.tools.plotting.scatter_matrix(all_data)
data_plot = sns.pairplot(all_data, diag_kind='kde', size=2);
plt.subplots_adjust(top=0.9)
data_plot.fig.suptitle('Correlation between Avg Rain and Temp between 1901 to 2012')


# In[190]:

sns.plt.show()


# In[ ]:



