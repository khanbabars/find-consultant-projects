'''
Created on Nov 8, 2021

@author: Shazib Saleem Warraich
'''
from bs4 import BeautifulSoup
import requests
from upgraded.LinkBase import LinkBase
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
       


            


           
#a =     ExtractProjectUrl()
#b = a.get_job_id('https://upgraded.se/lediga-uppdrag/')
#for i in b:
#    print(i)      
    
    
     
        #req = requests.get(url)
        #soup = BeautifulSoup(req.text, "html.parser")
        #job_id_array = []
        #for link in soup.find_all('a'):
        #    job_url  = link.get('href')
        #    job_id = re.search('https://upgraded.se/konsultuppdrag/(.+?)-', job_url)
        #    found = job_id.group(1)            
        #    job_id_url = self.url.project_api_base + found + self.url.project_api_location
        #    job_id_array.append(job_id_url)
        #return job_id_array    
      