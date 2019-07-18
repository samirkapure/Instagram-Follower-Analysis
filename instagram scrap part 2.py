# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:56:08 2019
<section class="zwlfE">
@author: SG-A6
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 01:40:00 2019

@author: SG-A6
"""
#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests

#getting the url:
rest = requests.get("https://www.instagram.com/motivation_daily12345/")
print(rest.status_code)
dat = rest.text

#applying beautifulsoup to the texted html sources
soup = BeautifulSoup(dat, 'html.parser')
soup
#importing the title (get to see if code work correctly)
titles = soup.find_all('ui',{'class' : 'zwlfE'})
for title in titles :
    print(title.text)
#unable to parse anything.