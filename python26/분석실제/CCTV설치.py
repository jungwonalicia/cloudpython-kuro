import pandas as pd


# In[115]:


CCTV_seoul = pd.read_csv('data/cctv_seoul.csv', encoding='utf-8')


# In[116]:


CCTV_seoul.head()


# In[117]:


CCTV_seoul.columns


# In[118]:


CCTV_seoul.rename(columns={CCTV_seoul.columns[0]:'구별'}, inplace=True)


# In[119]:


CCTV_seoul.head()


# In[120]:


# pop_Seoul = pd.read_excel('data/pop_seoul.xls', encoding='utf-8')


# In[121]:


# pop_Seoul.head()


# In[122]:


pop_Seoul = pd.read_excel('data/pop_Seoul.xls', 
                          header = 2,
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8')
pop_Seoul.head()


# In[123]:


CCTV_seoul.sort_values(by='소계', ascending=True).head()


# In[124]:


CCTV_seoul.sort_values(by='소계', ascending=False).head()


# In[125]:


pop_Seoul.head(5)


# In[126]:


pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                          pop_Seoul.columns[1] : '인구수',
                          pop_Seoul.columns[2] : '한국인',
                          pop_Seoul.columns[3] : '외국인',
                          pop_Seoul.columns[4] : '고령자',
                            }, inplace=True)
pop_Seoul.head()


# In[127]:


pop_Seoul.drop([0], inplace=True)
pop_Seoul.head()


# In[128]:


pop_Seoul['구별'].unique()


# In[129]:


pop_Seoul[pop_Seoul['구별'].isnull()]


# In[130]:


pop_Seoul.drop([26], inplace=True)


# In[131]:


pop_Seoul[pop_Seoul['구별'].isnull()]


# In[132]:


pop_Seoul['외국인비율'] = pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul.head()


# In[133]:


pop_Seoul['고령자비율'] = pop_Seoul['고령자']/pop_Seoul['인구수']*100
pop_Seoul.head()


# In[134]:


pop_Seoul.sort_values(by='인구수', ascending=False).head(5)


# In[135]:


pop_Seoul.sort_values(by='인구수', ascending=True).head(5)


# In[136]:


pop_Seoul.sort_values(by='외국인비율', ascending=True).head(5)


# In[137]:


pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5)


# In[138]:


pop_Seoul.sort_values(by='고령자비율', ascending=False).head(5)


# In[139]:


CCTV_seoul['최근증가율'] = (CCTV_seoul['2016년'] + 
                           CCTV_seoul['2015년']+
                           CCTV_seoul['2014년']) / CCTV_seoul['2013년도 이전'] * 100
CCTV_seoul.head()


# In[140]:


CCTV_seoul.sort_values(by='최근증가율', ascending=False).head(5)


# In[141]:


data_result =  pd.merge(CCTV_seoul, pop_Seoul, on = '구별')
data_result.head()


# In[142]:


del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']

data_result.head()


# In[143]:


data_result.set_index('구별', inplace=True)


# In[144]:


data_result.head()


# In[145]:


import numpy as np


# In[146]:


np.corrcoef(data_result['고령자비율'], data_result['소계'])


# In[147]:


np.corrcoef(data_result['외국인비율'], data_result['소계'])


# In[148]:


np.corrcoef(data_result['인구수'], data_result['소계'])


# In[149]:


data_result.sort_values(by = '인구수', ascending=False).head()


# In[150]:


np.corrcoef(data_result['최근증가율'], data_result['소계'])


# In[151]:


import matplotlib.pyplot as plt


# In[152]:


plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1])
plt.show()


# In[153]:


t = np.arange(0, 12, 0.01)
y = np.sin(t)
z = np.cos(t)

plt.figure(figsize=(10,6))

plt.plot(t, y, label='sin', lw=5)
plt.plot(t, z, 'g^', label='cos')
plt.legend()

plt.grid()
plt.xlabel('time')
plt.ylabel('yvalue')
plt.title('my graph')

plt.show()


# In[154]:


plt.figure(figsize=(10,6))

t = np.arange(0, 5, 0.5)

plt.plot(t, t, 'r--')
plt.plot(t, t*2, 'bs')
plt.plot(t, t*3, 'g^')
plt.plot(t, t*4, color='green', linestyle='dashed', marker='o')



plt.show()


# In[155]:


s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.figure(figsize=(10,6))
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()


# In[156]:


plt.figure(figsize=(10,6))
plt.boxplot((s1, s2, s3))
plt.grid()
plt.show()


# In[157]:


import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 


# In[158]:


data_result.head()


# In[159]:


plt.figure()

data_result['소계'].plot(kind='barh', grid=True, figsize=(10, 10))

plt.show()


# In[160]:


plt.figure()

data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10, 10))

plt.show()


# In[161]:



data_result['CCTV비율'] = data_result['소계']/data_result['인구수'] * 100

plt.figure()

data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10, 10))

plt.show()








# In[162]:


plt.figure(figsize=(6,6))

plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV 소계')
plt.grid()

plt.show()

