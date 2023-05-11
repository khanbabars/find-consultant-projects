'''
Created on Mars 15, 2022

@author: Shazib Saleem Warraich
'''

from bs4 import BeautifulSoup
import requests
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
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        try:
            for link in soup.find_all('a'):
                job_url  = link.get('href')
                if len(job_url) > 50:
                    #print(job_url)
                    rows.truncate()
                    rows.load_url_dump([str(job_url)])
        except TypeError:
            pass 
     
    
    '''After extracting project page url then 
       extract the project page'''
    def extract_project_page(self, project_url):   
        req = requests.get(project_url)
        soup = BeautifulSoup(req.text,  "html.parser")
        project_details  =  soup.find("article").get_text()
        return project_details
        #print(project_title)
    
    '''After extracting project page url then 
       extract the project details'''
    def extract_project_details(self, project_url):   
        req = requests.get(project_url)
        soup = BeautifulSoup(req.text,  "html.parser")
        project_details  =  soup.find("p").get_text()
        return project_details
        #print(project_title)

                  
    def keyman_main(self):  
        
        db =  SentToDb()
        db.truncate_keyman()
        print("Truncated URL_DUMP")
        self.get_project_url()
        print("New projects urls are loaded to URL_DUMP")
        db.truncate_keyman_dump()
        print("Truncated Keyman dump")
        print("Ready for data load")
        for url_rows in db.select_url_dump():
            project_page = self.extract_project_page(url_rows)
            project_details = self.extract_project_details(url_rows)
            project_url = url_rows
            data = [("Keyman", project_page, project_details, project_url )]
            db.insert_keyman_db(data)
        print("keyman load done")
            


    
#c = SentToDb()
#c.select_url_dump()    

c = Keyman()
c.keyman_main()
#b.keyman_main('https://www.keyman.se/data-it/senior-specialist-ad-technician-level-5/')  
