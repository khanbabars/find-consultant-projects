'''
Created on Nov 8, 2021

@author: Shazib Saleem Warraich
'''

class LinkBase():
    upgraded_main_api    = 'https://upgraded.se/lediga-uppdrag/'
    project_api_base     = 'https://upgraded.workbuster.com/jobs/'
    project_api_location = '?_=0.17910003100031924&ref=&language=sv'
    ###### KEYMAN UPPDRAG ####
    keyman_main_api      = 'https://www.keyman.se/uppdrag'
    cinode               ="https://cinode.market/requests"
    cinode_market        = "https://cinode.market"
    
    def get_project_url(self , job_id):
        project_url = self.project_api_base+job_id+self.project_api_location
        print(project_url)
        return project_url
        
        

#a =   LinkBase()
#a.get_project_url('123')      