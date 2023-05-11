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
        project_detail =  soup.find("meta", {"property": "og:description"})  
        startDatum = soup.find("div", {"class": "fusion-text fusion-text-4 fusion-text-no-margin"}).get_text()
        slutDatum = soup.find("div", {"class": "fusion-text fusion-text-5 fusion-text-no-margin"}).get_text()
        omfattning = soup.find("div", {"class": "fusion-text fusion-text-3 fusion-text-no-margin"}).get_text()
        ort = soup.find("div", {"class": "fusion-text fusion-text-2 fusion-text-no-margin"}).get_text()
        ansok = soup.find("div", {"class": "fusion-text fusion-text-7 fusion-text-no-margin"}).get_text()
        reference = soup.find("div", {"class": "fusion-text fusion-text-1 fusion-text-no-margin"}).get_text()
        return  project_detail["content"]+"              "+"Om uppdraget"+startDatum+slutDatum+omfattning+ort+ansok+reference
    
    def project_contact(self, project_url):    
        url = project_url
        req = requests.get(url)
        soup = BeautifulSoup(req.text,  "html.parser")   
        project_contact = soup.find("div", {"style": "border:0px solid blue; width:75%; float: left; padding-left: 15px;"}).get_text()
        return "Kontaktuppgifter              "+project_contact       









#c = ExtractProjectDetail()

#url = "https://upgraded.workbuster.com/jobs/180074?_=0.17910003100031924&ref=&language=sv"

#a =  ExtractProjectUrl()
#b = a.get_job_id('https://upgraded.workbuster.com/?_=0.8957893780895969&ref=&language=sv')
#for i in b:
#    f = c.project_title(i)
#    j = c.project_detail(i)
#    k = c.project_contact(i)
#    print(i +j+ f + k)      
    
#d = ExtractProjectDetail()
#d.project_data(url)
#req = requests.get(url)

#soup = BeautifulSoup(req.text,  "html.parser")
#data = soup.find("div", {"id": "page-block-3246"}) 
#str = data.get_text()
#print(str)



#data2 = soup.find("div", {"id": "page-block-3247"}) 
#str2 = data2.get_text()
#print(str2)




#data3 = soup.find("div", {"id": "page-block-3337"}) 
#str3 = data3.get_text()
#print(str3)





#rows = [ (company, str[0: 3000])]
#obj.insert_to_db(rows)
#for data in soup.find_all("p"): 

 #   print(data.get_text()) 


#soup = BeautifulSoup(req.text,  "html.parser")
#str = soup.find("div", {"id": "page-job-details"})
#print(str.get_text())
#rows = [ (company, str )]
#obj.insert_to_db(rows)

#for link in str:
#    str = link.get_text()
#    print (str)
    #obj.insert_to_db(rows)
#    print(str)
    #print("Encoding method :", soup.original_encoding)

# providing url
#url = "https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed"




