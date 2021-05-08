import numpy as np
import pandas as pd
import os
import json
from typing import Dict, List, Optional, Union, cast

from env import github_token, github_username

import acquire_zach as az

# acquire
from requests import get
from bs4 import BeautifulSoup
from time import sleep
import os

import unicodedata
import re

import warnings
warnings.filterwarnings("ignore")

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

'''
*------------------*
|                  |
|     ACQUIRE      |
|                  |
*------------------*
'''

def get_githubpgs():
    """
    This function will create a list of all the url pages in the google repos section
    """
    urls = []
    for i in range(1,67):
        
        url = f'https://github.com/google?page={i}'
        urls.append(url)
    return urls





def get_repo_links():
    """
    This function will concat a base url with the repo suffix
    and create a list of all appended repo links on a single page.
    """
    repos = []
    for i in range(0,29):
        link_suffix = soup.find_all('a', itemprop='name codeRepository')[i].get('href')
        link  = f'https://github.com{link_suffix}'
        repos.append(link)
    return repos





def souper(site):
    """
    This function takes in a website string
    parses the html
    returns the html of the site as text 
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = get(site, headers=headers)
    
    html = response.text
    soup = BeautifulSoup(html)
    
    return soup





def get_all_repo_links():
    """
    This function takes a list of urls
    - parses the html of the page
    - retrieves the links of all of the repo sites on the page
    returns the  appended list of all the repo links
    """
    repo_links = []
    
    urls = get_githubpgs()
    
    for url in urls:
        soup = souper(url)
        
        repos = get_repo_links()
        repo_links.append(repos)
    
    return repo_links

'''
*------------------*
|                  |
|     PREPARE      |
|                  |
*------------------*
'''


def clean(text, extra_words = ['r', 'u', '2', 'ltgt', "'"]):
    """
    A simple function to cleanup text data:
    takes in a string of text,
    pulls in `nltk`s stopwords and appends any additional `extra_words`
    returns a string filtered for stopwords & lemmatized    
    """
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') + extra_words
    text = (unicodedata.normalize('NFKD', text)
             .encode('ascii', 'ignore')
             .decode('utf-8', 'ignore')
             .lower())
    words = re.sub(r'[^\w\s]', '', text).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]





def remove_columns(df, cols_to_remove):  
    """
    This function removes columns listed in arguement
    - cols_to_remove = ["col1", "col2", "col3", ...]
    returns DF w/o the columns.
    """
    df = df.drop(columns=cols_to_remove)
    return df





def get_length(column):
    """
    This function reads the length of each readme and
    appends it to a list.
    """
    
    length = []
    for i in range(0,1943):
        text_len = len(df.column[i])
        length.append(text_len)
    
    return length






def df_features():
    """
    This function creates new features as columns:
    - readme_length: word count of readme's
    - clean_content: cleaned readme content
    - cleaned_length: word count of cleaned readme's
    """
    
    df['readme_length'] = get_length("readme_contents")
    
    df['clean_content'] = df.readme_contents.apply(w.clean)
    
    df['cleaned_length'] = get_length("clean_content")
    
    





def split(df, stratify_by=None):
    """
    3 way split for train, validate, and test datasets
    To stratify, send in a column name
    """
    
    
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
    
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test





