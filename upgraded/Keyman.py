'''
Created on Mars 15, 2022

@author: Shazib Saleem Warraich
'''

from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

from upgraded.LinkBase import LinkBase
from upgraded.SendToDB import SentToDb


class Keyman():
    
    db =  SentToDb()
    url = LinkBase()
    
    '''First fetch all projects url from keyman main url
       and load it into database to filter url text'''
    
    def get_project_url (self):
        rows         = SentToDb()
        url = LinkBase.keyman_main_api
        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        req = Request(url,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
        try:
            rows.truncate_url_dump()
            for link in soup.find_all('a'):
                job_url  = link.get('href')
                if len(job_url) > 50:
                    rows.load_url_dump([str(job_url)])
                print(job_url)    
        except (TypeError, AttributeError):
            pass 
     
    
    '''After extracting project page url then 
       extract the project page'''
    def extract_project_page(self, project_url):  
        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        req = Request(project_url,headers=hdr)
        page = urlopen(req) 
        soup = BeautifulSoup(page,  "html.parser")
        try:
            print (project_url)
            project_details  =  soup.find("tbody").get_text()
            print (project_details)
            return project_details
        except (TypeError, AttributeError):
            pass 
    
 
    '''After extracting project page url then 
       extract the project details'''
    def extract_project_details(self, project_url):   
        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        req = Request(project_url,headers=hdr)
        page = urlopen(req) 
        soup = BeautifulSoup(page,  "html.parser")
        try:
            project_details  =  soup.find("meta", property="og:description")
            project_details = project_details["content"]
            return project_details
        except (TypeError, AttributeError):
            pass 

                  
    def keyman_main(self):  
        
        db =  SentToDb()
        db.truncate_url_dump()
        print("Truncated URL_DUMP")
        self.get_project_url()
        print("New projects urls are loaded to URL_DUMP")
        db.truncate_keyman_dump()
        print("Truncated Keyman dump")
        print("Ready for data load")
        try:
            for url_rows in db.select_url_dump():
                project_page = self.extract_project_page(url_rows)
                project_details = self.extract_project_details(url_rows)
                project_url = url_rows
                data = [("Keyman", project_page, project_details, project_url )]
                print("Keyman", project_page, project_details, project_url)
                db.insert_keyman_db(data)
                print("keyman load done")
        except (TypeError, AttributeError):
            pass         
  

c = Keyman()
#c.get_project_url();
#c.extract_project_page("https://www.keyman.se/sv/category/chefs-och-ledarskapsstod/")
c.keyman_main()
#b.keyman_main('https://www.keyman.se/data-it/senior-specialist-ad-technician-level-5/')  
