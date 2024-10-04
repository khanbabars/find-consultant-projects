'''
Created on Mar 14, 2022

@author: pc786
'''
import re
import time
import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ExtractProjectUrl():
    
   def get_job_id (self, url):
        driver = webdriver.Chrome(executable_path="C:/Users/pc786/Desktop/blog/blog selenium/chromedriver")
        driver.get(url)
        time.sleep(4)
        elems = driver.find_elements_by_xpath("//a[@href]")
        url_array =[]
        for elem in elems:
            job_url = elem.get_attribute("href") 
            if (len(job_url))>45:
                url_array.append(job_url)
        #print(url_array)        
        return url_array
                #print(url_array)
                
                
                
                
                
                
a =     ExtractProjectUrl()
b = a.get_job_id('https://upgraded.se/lediga-uppdrag/')
for i in b:
    print(i)                      
                
                
  #  url_array.append(job_url)
   # for i in url_array:
    #    print(url_array)
        
     
#url = "https://upgraded.se/konsultuppdrag/5559-senior-backend-developer-2/"
#req = requests.get(url)
#soup = BeautifulSoup(req.text,  "html.parser")
#project_title  =  soup.find("meta", {"property": "og:description"})
#print(project_title["content"])
#to_fetch = "Om uppdragetStartdatum: OmgåendeSlutdatum: 2023-12-31Omfattning: 100%Ort: GöteborgAnsök senast: 2023-05-22Referensnummer: 243232"

#startDatum = soup.find("div", {"class": "fusion-text fusion-text-4 fusion-text-no-margin"}).get_text()
#slutDatum = soup.find("div", {"class": "fusion-text fusion-text-5 fusion-text-no-margin"}).get_text()
#omfattning = soup.find("div", {"class": "fusion-text fusion-text-3 fusion-text-no-margin"}).get_text()
#ort = soup.find("div", {"class": "fusion-text fusion-text-2 fusion-text-no-margin"}).get_text()
#ansok = soup.find("div", {"class": "fusion-text fusion-text-7 fusion-text-no-margin"}).get_text()
#reference = soup.find("div", {"class": "fusion-text fusion-text-1 fusion-text-no-margin"}).get_text()
#print(project_title["content"]+"              "+"Om uppdraget"+startDatum+slutDatum+omfattning+ort+ansok+reference)


#project_contact = soup.find("div", {"style": "border:0px solid blue; width:75%; float: left; padding-left: 15px;"}).get_text()
#print("Kontaktuppgifter              "+project_contact) 
#print(project_title)