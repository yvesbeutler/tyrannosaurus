#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'src/notebooks'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# #  20 Years of Games
# 
# Tutorial is based on https://www.dataquest.io/blog/pandas-python-tutorial
# 
# Author: yvesbeutler
# Date: 13-02-2019
# 

#%%
import numpy as np
import pandas as pd

reviews = pd.read_csv("../../data/ign.csv")


#%%
# remove first unwanted column
reviews = reviews.loc[:,"score_phrase":] # better than reviews.iloc[:,1:]

reviews.head()


#%%
some_reviews = reviews.iloc[10:20,]
some_reviews.head()

# info: some_reviews.loc[9:21,:] doesn't throw an error as expected


#%%
# create a DataFrame out of three Series
s1 = pd.Series([5371, 'Yves Beutler', 'Junior'])
s2 = pd.Series([4365, 'Natalie Kuster', 'Lead'])
s3 = pd.Series([1925, 'Fabio Vivian', 'Professional'])

df = pd.DataFrame([s1, s2, s3],columns=['id', 'name', 'experience'])
# why can't I rename my cols..? :-(

df


#%%
# get the mean score of all games
reviews['score'].mean()

# get the means of all numerical columns
reviews.mean()

#%% [markdown]
# ### Statistical Correlation
# 
# As a rule of thumb, the following guidelines on strength of relationship are often useful (though many experts would somewhat disagree on the choice of boundaries).
# 
# | Value of r                 | Strength of relationship |
# |----------------------------|--------------------------|
# | -1.0 to -0.5 or 1.0 to 0.5 | Strong                   |
# | -0.5 to -0.3 or 0.5 to 0.3 | Moderate                 |
# | -0.3 to -0.1 or 0.3 to 0.1 | Weak                     |
# | -0.1 to 0.1                | None or very weak        |
# 
# Correlation is only appropriate for examining the relationship between meaningful quantifiable data (e.g. air pressure, temperature) rather than categorical data such as gender, color etc.

#%%
# check correlation of our attributes
reviews.corr()


#%%
# create Boolean Series to filter with
score_filter = reviews['score'] > 8

reviews[score_filter]


#%%
# 1. What is the first game ever released?

min_year = reviews['release_year'].min()
year_filter = reviews['release_year'] == min_year
filtered_reviews = reviews[year_filter]

min_month = filtered_reviews['release_month'].min()
month_filter = filtered_reviews['release_month'] == min_month
filtered_reviews = filtered_reviews[month_filter]

min_day = filtered_reviews['release_day'].min()
day_filter = filtered_reviews['release_day'] == min_day
filtered_reviews = filtered_reviews[day_filter]

filtered_reviews[['title','release_year','release_month','release_day']]


