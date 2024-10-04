'''
Created on Nov 10, 2021

@author: Shazib Saleem Warraich
'''

from upgraded.ExtractProjectDetail import ExtractProjectDetail
from upgraded.ExtractProjectUrl import ExtractProjectUrl
from upgraded.SendToDB import SentToDb


class Main:
    def run(self):
        rows         = SentToDb()
        rows.truncate()
        upgraded_url      = ExtractProjectUrl()
        detail    = ExtractProjectDetail()
        
        project_api = upgraded_url.get_job_id('https://upgraded.se/lediga-uppdrag/') #Upgraded main api Url
        print("Uploading upgraded project to the datbase") 
        for project_url in project_api:
            get_title   = detail.project_title(project_url)
            get_detail  = detail.project_detail(project_url)
            get_contact = detail.project_contact(project_url)
            data = [("Upgraded", get_title, get_detail, get_contact, project_url )]
            rows.insert_to_db(data)
            print( project_url + get_title)
             
        
#p(consultant_company, project_heading, project_details, project_contact, project_url)


a = Main()
a.run()
#a =     ExtractProjectUrl()
#b = a.get_job_id('https://upgraded.workbuster.com/?_=0.8957893780895969&ref=&language=sv')
#for i in b:
#    print(i)      
            