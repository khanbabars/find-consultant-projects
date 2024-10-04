'''
Created on Mar 14, 2022

@author: pc786
'''
import cx_Oracle

from upgraded.DbConfig import DbConfig


class SentToDb:
    conf = DbConfig()
    cx_Oracle.init_oracle_client(lib_dir= conf.oracle_client_dir)
    connection = cx_Oracle.connect(user = 'general', password= 'BandTraktor17', dsn= 'tcps://adb.eu-frankfurt-1.oraclecloud.com:1522/odb6lykd5axtqk4_db202007031441_high.atp.oraclecloud.com?wallet_location=C:/Users/pc786/cloud/Wallet_DB202007031441')
    ########################UPGRADED DB#####################################
    def insert_to_db (self):
        db  = self.connection 
        cursor = db.cursor()
        for row in cursor.execute('select sysdate from dual'):
            print(row)
  
  
  
  
a = SentToDb()
a.insert_to_db()
            
 