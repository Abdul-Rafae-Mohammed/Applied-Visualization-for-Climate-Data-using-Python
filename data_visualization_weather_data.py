
# coding: utf-8



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



