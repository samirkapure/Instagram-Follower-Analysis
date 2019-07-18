# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:07:26 2019

@author: SG-A6
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests


import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json

"""url = "https://www.instagram.com/motivation_daily12345/"""
class Insta_Info_Scraper:

    def getinfo(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'})
        text = data[0].get('content').split()
        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        print ('User:', user)
        print ('Followers:', followers)
        print ('Following:', following)
        print ('Posts:', posts)
        print ('---------------------------')

    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        
        with open('users.txt') as f:
            self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            self.getinfo(url)


if __name__ == '__main__':
    obj = Insta_Info_Scraper()
    obj.main()