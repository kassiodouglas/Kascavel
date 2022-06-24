from datetime import datetime
from src.core.Storage import Storage
from src.app.configs.log import *
import csv

class Log():      
   
  
         
    
    def __init__(self) -> None:       
        self.now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._conn = log['conn']
        self._table = log['table']
        self._driver = log['driver']
        self._logoff = log['logoff']
    
    
    def log(self, namelog, log):
       
        print(self.now +" | "+ namelog +" | "+ log)
        
        if(self._logoff != False):
            self.save(namelog, log)
        
        
    def save(self, namelog, log):        
      
        if self._driver == 'csv':
            path = Storage().basePath('src\\logs')
            
            with open(rf"{path}/{namelog}.csv", 'a', newline="") as csvfile:
                csv.writer(csvfile, delimiter=',').writerow([self.now, namelog, log ])  
            
        if self._driver == 'txt':
            pass
        elif self._driver == 'db':    
            try:       
                self._conn.table(self._table).insert({'namelog': namelog,'text': log})
            except Exception as err:
                print(str(self.now) +" | "+ str(err))
        
        