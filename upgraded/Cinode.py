'''
Created on Mars 15, 2022

@author: Shazib Saleem Warraich
'''

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from upgraded.LinkBase import LinkBase
from upgraded.SendToDB import SentToDb


class Cinode():
    
    db =  SentToDb()
    url = LinkBase()
    
    '''First fetch all projects url from keyman main url
       and load it into database to filter url text'''
    
    def get_project_url (self):
        rows         = SentToDb()
        url          =    LinkBase.cinode;
        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        req = Request(url,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
        try:
            rows.truncate_url_dump()
            for link in soup.find_all('a'):
                job_url  = link.get('href')
                if len(job_url) > 10:
                    rows.load_url_dump([str(LinkBase.cinode_market+ job_url)])
                print([str(LinkBase.cinode_market+ job_url)])    
        except (TypeError, AttributeError):
            pass 
     

        
    '''After extracting project title '''
    def extract_project_title(self, project_url):  
        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        req = Request(project_url,headers=hdr)
        page = urlopen(req) 
        soup = BeautifulSoup(page,  "html.parser")
        project_title  =  soup.find("meta", property="og:title")
        project_title = project_title["content"] if project_title else "No meta title given"
        print(project_title)
        return project_title



    '''After extracting project detail '''
    def extract_project_page(self, project_url):  
        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        req = Request(project_url,headers=hdr)
        page = urlopen(req) 
        soup = BeautifulSoup(page,  "html.parser")
        project_details  =  soup.find("meta", property="og:description")
        project_details = project_details["content"] if project_details else "No meta title given"
        return project_details
    


    def cinode_main(self):  
        
        db =  SentToDb()
        db.truncate_url_dump()
        print("Truncated URL_DUMP")
        self.get_project_url()
        print("New projects urls are loaded to URL_DUMP")
        print("Ready for data load")
        for url_rows in db.select_cinode_url_dump():
            project_title = self.extract_project_title(url_rows)
            project_page = self.extract_project_page(url_rows)
            project_url = url_rows
            data = [("cinode", project_page, project_title, project_url )]
            print("cinode", project_page, project_title, project_url)
            db.insert_cinode_dump(data)
            print("Cinode load done")


c = Cinode()
#c.get_project_url();
#c.extract_project_title("https://cinode.market/requests/12619")
c.cinode_main()
#b.keyman_main('https://www.keyman.se/data-it/senior-specialist-ad-technician-level-5/')  
