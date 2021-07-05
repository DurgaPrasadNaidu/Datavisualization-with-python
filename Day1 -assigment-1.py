#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib as mlp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


x=np.arange(0,10)
y=x*x
plt.plot(x,y,'r*',linestyle='dashed',linewidth=2,markersize=12)
plt.xlabel('x-axis',color='blue')
plt.ylabel('y-axis',color='blue')
plt.title('2d-diagram',color='blue')


# In[ ]:




