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

def get_githubpgs():
    """
    This function will create a list of all the url pages in the google repos section
    """
    urls = []
    for i in range(1,68):
        
        url = f'https://github.com/google?page={i}'
        urls.append(url)
    return urls





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
        link  = f'https://github.com/{link_suffix}'
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

