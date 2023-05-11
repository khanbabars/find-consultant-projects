'''
Created on Nov 9, 2021

@author: Shazib Saleem Warraich
'''
import cx_Oracle
from upgraded.DbConfig import DbConfig


class SentToDb:
    conf = DbConfig()
    cx_Oracle.init_oracle_client(lib_dir= conf.oracle_client_dir)
    connection = cx_Oracle.connect(user = conf.atp_user, password= conf.atp_password, dsn= conf.atp_dsn)
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
            rows = cursor.execute("select distinct url from url_dump where url like '%data-it%'")    
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
       
# Create a table

#cursor.execute("""begin
#                     execute immediate 'drop table pytab';
#                     exception when others then if sqlcode <> -942 then raise; end if;
#                     
#                                       end;""")
#cursor.execute("create table pytab (id number, data varchar2(20))")

# Insert some rows

#rows = [ (1, "First" ),
#         (2, "Second" ),
#         (3, "Third" ),
#         (4, "Fourth" ),
#         (5, "Fifth" ),
#         (6, "Sixth" ),
#         (7, "Seventh" ) ]

#cursor.executemany("insert into pytab(id, data) values (:1, :2)", rows)

#connection.commit()  # uncomment to make data persistent

# Now query the rows back

#for row in cursor.execute('select * from load_extracted_dump'):
#    print(row)
