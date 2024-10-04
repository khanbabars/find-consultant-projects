'''
Created on Nov 8, 2021

@author: Shazib Saleem Warraich
'''
import re
import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from upgraded.LinkBase import LinkBase


class ExtractProjectUrl():
    
    url = LinkBase()
   
    def get_job_id (self, url):
        url = self.url.upgraded_main_api
        driver = webdriver.Chrome(executable_path="C:/Users/pc786/Desktop/blog/blog selenium/chromedriver")
        driver.get(url)
        time.sleep(4)
        elems = driver.find_elements_by_xpath("//a[@href]")
        url_array =[]
        for elem in elems:
            job_url = elem.get_attribute("href") 
            if (len(job_url))>45:
                url_array.append(job_url)
        return url_array
       


            

