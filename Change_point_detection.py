#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


get_ipython().system('pip install ruptures')
get_ipython().system('pip install xlrd')
get_ipython().system('pip install pandas')
import matplotlib.pyplot as plt
import ruptures as rpt
import pandas as pd
import numpy as np
df=pd.read_excel(io='C:/Users/Prof. Santanu Paul/Downloads/foodMonitoringData.xlsx', sheet_name='Simple Data',usecols='B')
detector = rpt.Pelt(model="rbf").fit(df.values)
change_points = detector.predict(pen=30)
fig,ax=plt.subplots()
ax.plot(df,color='tab:red')
plt.title('MQval')
for r in change_points:
    ax.axvline(x=r,color='k',linestyle='--')
    breaks_rpt = []
for i in change_points:
    breaks_rpt.append(df.index[i-1])
for i in breaks_rpt:
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




