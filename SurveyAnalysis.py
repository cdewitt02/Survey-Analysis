#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd

df = pd.read_csv('C://Users/charl/Python/survey_results_public.csv') #location may have to change to wherever you placed the survey

#df['Blockchain'].value_counts().plot(kind = "bar") #outputs bar graph showing interest in crypto

#df['MainBranch'].value_counts(normalize = True).plot(kind = "pie") #outputs pie chart showing why a person is into coding

# filtered = df[(df['Knowledge_3'] == 'Strongly disagree') & (df['Country'] == 'United States of America')]
# print(filtered['Country'].value_counts()) #displays all surveyors who live in the US who stronlgy disagree with question 'Knowledge_3'

# filtered = df[(df['OpSysProfessional use'] != df['OpSysPersonal use'])]
# print(filtered['OpSysProfessional use'].value_counts()) #displays all the professionally used OS's that don't match the surveyors personal OS

# filtered = df[(df['OrgSize'] == '10,000 or more employees') & (df['YearsCodePro'])]
# print(filtered['YearsCodePro'].value_counts()) #displays the coding experience in years for employees at companies with more than 10,000 employees



# In[ ]:





# In[ ]:




