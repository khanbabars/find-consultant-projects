'''
Created on Nov 9, 2021

@author: Shazib Saleem Warraich
'''
import cx_Oracle

from upgraded.DbConfig import DbConfig


class SentToDb:
    conf = DbConfig()
    cx_Oracle.init_oracle_client(lib_dir= conf.oracle_client_dir)
    connection = cx_Oracle.connect(user = conf.atp_user, password= conf.atp_password, dsn= 'tcps://adb.eu-frankfurt-1.oraclecloud.com:1522/odb6lykd5axtqk4_db202007031441_high.atp.oraclecloud.com?wallet_location=C:/Users/pc786/cloud/Wallet_DB202007031441')
    ########################UPGRADED DB#####################################
    def insert_to_db (self, rows):
        db  = self.connection 
        cursor = db.cursor()
        cursor.executemany("insert into upgraded_dump(consultant_company, project_heading, project_details, project_contact, project_url) values (:1, :2, :3, :4, :5)", rows)
        db.commit()
        return
    
    def truncate(self):
        db  = self.connection 
        cursor = db.cursor()
        cursor.execute("""begin
                   execute immediate 'truncate table upgraded_dump';
                     end;""")
        db.commit()
        return
    
    ########################KEYMAN DB#####################################
    def truncate_keyman(self):
        db  = self.connection 
        cursor = db.cursor()
        cursor.execute("""begin
                   execute immediate 'truncate table url_dump';
                     end;""")
        db.commit()
        return
    
    
    
    def truncate_url_dump(self):
        db  = self.connection 
        cursor = db.cursor()
        cursor.execute("""begin
                   execute immediate 'truncate table url_dump';
                     end;""")
        db.commit()
        return
    
    
      
    def load_url_dump(self, found_href):
        db  = self.connection 
        cursor = db.cursor()
        cursor.execute("insert into url_dump(url) values (:1)", found_href)
        db.commit()
        return
    
    def select_url_dump(self):
        try:
            db  = self.connection 
            cursor = db.cursor()
            url_array = []
            rows = cursor.execute("select distinct url from url_dump where url like '%data-it%' or url like '%administration-ekonomi-juridik%' or url like '%management%'  or url like 'verksamhets-och%' or url like '%chefs-och-ledarskapsstod%' or url like 'miljo-hallbarhet-csr%'")    
            for url in rows:
                url_array.append(url[0])
            return url_array
        except None:
            pass   
       
    
    def truncate_keyman_dump(self):
        db  = self.connection 
        cursor = db.cursor()
        cursor.execute("""begin
                   execute immediate 'truncate table keyman_dump';
                     end;""")
        db.commit()
        return
       
       
    def insert_keyman_db (self, rows):
        db  = self.connection 
        cursor = db.cursor()
        cursor.executemany("insert into keyman_dump(consultant_company, project_page ,project_details, project_url) values (:1, :2, :3, :4)", rows)
        db.commit()
        return
    
    
    ########################CINODE DB#####################################    
    
    def select_cinode_dump(self):
        try:
            db  = self.connection 
            cursor = db.cursor()
            url_array = []
            rows = cursor.execute("select distinct url from url_dump where url like '%cinode.market/requests/%' and url not in (select project_url from cinode_dump)")    
            for url in rows:
                url_array.append(url[0])
            return url_array
        except None:
            pass 
        
    
    def select_cinode_url_dump(self):
        try:
            db  = self.connection 
            cursor = db.cursor()
            url_array = []
            rows = cursor.execute("select distinct url from url_dump where url like '%cinode.market/requests/%' and url not in (select project_url from cinode_dump)")    
            for url in rows:
                url_array.append(url[0])
            return url_array
        except None:
            pass   
           
    
    
    def insert_cinode_dump (self, rows):
        db  = self.connection 
        cursor = db.cursor()
        cursor.executemany("insert into cinode_dump(consultant_company, project_page ,project_title, project_url) values (:1, :2, :3, :4)", rows)
        db.commit()
        return
    
    
