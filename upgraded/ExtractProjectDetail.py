'''
Created on Nov 8, 2021

@author: Shazib Saleem Warraich
'''

from bs4 import BeautifulSoup
import requests


class ExtractProjectDetail:
    
    def project_title(self, project_url):    
        url = project_url
        req = requests.get(url)
        soup = BeautifulSoup(req.text,  "html.parser")
        project_title  =  soup.find("meta", {"property": "og:title"})
        return project_title["content"]
    
    def project_detail(self, project_url):    
        url = project_url
        req = requests.get(url)
        soup = BeautifulSoup(req.text,  "html.parser")
        try:
            project_detail =  soup.find("meta", {"property": "og:description"})  
            startDatum = soup.find("div", {"class": "fusion-text fusion-text-5 fusion-text-no-margin"}).get_text()
            slutDatum = soup.find("div", {"class": "fusion-text fusion-text-6 fusion-text-no-margin"}).get_text()
            omfattning = soup.find("div", {"class": "fusion-text fusion-text-4 fusion-text-no-margin"}).get_text()
            ort = soup.find("div", {"class": "fusion-text fusion-text-3 fusion-text-no-margin"}).get_text()
            ansok = soup.find("div", {"class": "fusion-text fusion-text-8 fusion-text-no-margin"}).get_text()
            reference = soup.find("div", {"class": "fusion-text fusion-text-2 fusion-text-no-margin"}).get_text()
            return  project_detail["content"]+"              "+"Om uppdraget"+startDatum+slutDatum+omfattning+ort+ansok+reference
        except: 
            pass
    
    def project_contact(self, project_url):    
        url = project_url
        req = requests.get(url)
        soup = BeautifulSoup(req.text,  "html.parser")   
        try:
            project_contact = soup.find("div", {"style": "border:0px solid blue; width:75%; float: left; padding-left: 15px;"}).get_text()
            return "Kontaktuppgifter              "+project_contact       
        except:
            pass

