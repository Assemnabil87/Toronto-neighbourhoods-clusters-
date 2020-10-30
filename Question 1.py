#!/usr/bin/env python
# coding: utf-8

# <h1>Segmenting and Clustering Neighborhoods in Toronto<h1>

# <h3>Question 1<h3>

# In this assignment, you will be required to explore, segment, and cluster the neighborhoods in the city of Toronto.
# 
# For the Toronto neighborhood data, a Wikipedia page exists that has all the information we need to explore and cluster the neighborhoods in Toronto. You will be required to scrape the Wikipedia page and wrangle the data, clean it, and then read it into a pandas dataframe so that it is in a structured format like the New York dataset.
# 
# Once the data is in a structured format, you can replicate the analysis that we did to the New York City dataset to explore and cluster the neighborhoods in the city of Toronto.

# <b>Scrap content from wiki page<b>

# In[2]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
from pandas.io.json import json_normalize
import folium
from sklearn.cluster import KMeans
import matplotlib.cm as cm
import matplotlib.colors as colors


# In[5]:


source = requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M").text
soup = BeautifulSoup(source, 'lxml')

table = soup.find("table")
table_rows = table.tbody.find_all("tr")

res = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [tr.text for tr in td]
    

    if row != [] and row[1] != "Not assigned":

        if "Not assigned" in row[2]: 
            row[2] = row[1]
        res.append(row)


# In[7]:


df = pd.DataFrame(res, columns = ["PostalCode", "Borough", "Neighborhood"])
df.head(10)


# In[9]:


df["PostalCode"] = df["PostalCode"].str.replace("\n","")
df["Borough"] = df["Borough"].str.replace("\n","")
df["Neighborhood"] = df["Neighborhood"].str.replace("\n","")
df.head(10)


# <b>Group all neighborhoods with the same postal code<b>

# In[11]:


df = df.groupby(["PostalCode", "Borough"])["Neighborhood"].apply(", ".join).reset_index()
df.head(10)


# In[12]:


print("Shape: ", df.shape)


# In[ ]:




