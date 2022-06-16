

class QueryBuilder():

    
    def __init__(self, conn):
        """Construtor da classe"""
              
        self.useTable = ''
        self.useSelect = '*'
        self.useWhereArr = []
        self.useWhere = ''
        self.useOrderBY = ''  
        self.useGroupBy = ''  
        self.useLimit = ''  
       
        
        self.conn = conn
        if self.conn == False : return False
               
        
    def execute(self, sql):
        """Executa uma query

        Args:
            sql (string): sql da query

        Returns:
            bool: 
        """  
        # c = self.conn.cursor()
        try:
            return self.conn.execute(sql)   
        except Exception as err:
            
            return False 
               
               
    def select(self, fields):
        self.useSelect = ''
        for field in fields:
            self.useSelect += rf"{field}," 
        
        self.useSelect = self.__rreplace(self.useSelect, ',', '', 1)
        return self
        
        
    def limit(self, value):        
        self.useLimit= rf"LIMIT {value}"
        return self
        
    
    def table(self, table):
        """Seleciona o nomne da tabela a utilizar na query

        Args:
            table (string): nome da tabela

        Returns:
            Sqlite: A própria classe
        """
        
        self.useTable = table        
        return self
    
    
    
    def createTable(self, fieldsValues):        
        fields = ''
        for field in fieldsValues:                
            fields += rf"{field},"             
            
        fields = self.__rreplace(fields, ',', '', 1) 
        
        sql = rf"CREATE TABLE IF NOT EXISTS {self.useTable} ({fields})"   
       
        result = self.execute(sql)
        if(result == False):
            return False    
        return True
    
    
    
    def dropTable(self):          
        sql = rf"DROP TABLE IF EXISTS {self.useTable}"   
       
        result = self.execute(sql)
        if(result == False):
            return False    
        return True
    
    
    
    def All(self):
        """Retorna uma listagem de todos os registros, não tem acesso aos outros metodos 

        Returns:
            fetchall: lista
        """    
        sql = rf"SELECT {self.useSelect} FROM {self.useTable}"  
        result = self.conn.execute(sql) 
        if(result == False):
            return False    
        regs = result.fetchall()
        if regs == None: return False
      
        colnames = []
        if hasattr(result,'keys') and ismethod(getattr(result,'keys')):            
            for a in result.keys():
                colnames.append(a)               
        else:
            for a in result.description:
                colnames.append(a[0])
         
   
       
        listAll = []
        for reg in regs:
            index=0 
            dict = {} 
            for data in reg:
                dict[colnames[index]] = data           
                index=index+1
            
            listAll.append(dict)
        return listAll
    
    
    
    def get(self): 
        """
        Retorna uma listagem de todos os registros, com tem acesso aos outros metodos 

        Returns:
            array  
        """  
        sql = rf"SELECT {self.useSelect} FROM {self.useTable} {self.useWhere} {self.useGroupBy} {self.useOrderBY} {self.useLimit}"  
        result = self.conn.execute(sql)
        if(result == False):
            return False          
          
        regs = result.fetchall()  
        if regs == None: return False
      
        colnames = []
        if hasattr(result,'keys') and ismethod(getattr(result,'keys')):            
            for a in result.keys():
                colnames.append(a)               
        else:
            for a in result.description:
                colnames.append(a[0])
       
         
        
        listAll = []
        for reg in regs:
            index=0 
            dict = {} 
            for data in reg:
                dict[colnames[index]] = data           
                index=index+1
                
            listAll.append(dict) 
                       
        
        return listAll
    
    
    
    
    def toSql(self):   
        """
        Retorna uma a string da query

        Returns:
            string  
        """      
        sql = rf"SELECT {self.useSelect} FROM {self.useTable} {self.useWhere} {self.useOrderBY}"  
        return sql
    
    
    
    def first(self): 
        """
        Retorna um unico registro

        Returns:
            array
        """
        sql = rf"SELECT {self.useSelect} FROM {self.useTable} {self.useWhere} {self.useGroupBy} {self.useOrderBY}"  
        result = self.execute(sql)      
    
        if(result == False):
            return False        
        
        reg = result.fetchone() 
        if reg == None: return False
      
        colnames = []         
        if hasattr(result,'keys') and ismethod(getattr(result,'keys')):            
            for a in result.keys():
                colnames.append(a)               
        else:
            for a in result.description:
                colnames.append(a[0])
         
        dict = {}
        index=0  
        for data in reg:
            dict[colnames[index]] = data           
            index=index+1     
      
        return dict
    
    
    
    def whereLike(self, fieldsValue): 
        """
        Cria a clausa WHERE LIKE na query

        Returns:
            classe
        """  
        item = rf"{fieldsValue[0]} LIKE '{fieldsValue[1]}'" 
        self.useWhereArr.append(item) 
        self.__where_concat() 
        return self
    
    
    
    def whereBetween(self, field, values):  
        """
        Cria a clausa WHERE BETWEEN na query

        Returns:
            classe
        """   
        item = rf"{field} BETWEEN '{values[0]}' AND '{values[1]}'" 
        self.useWhereArr.append(item) 
        self.__where_concat() 
        return self
    
    
    
    def whereIn(self, field, values):
        """
        Cria a clausa WHERE IN na query

        Returns:
            classe
        """   
        whereIn = ''
        for x in values:
            whereIn += rf"'{x}',"
        
        whereIn = self.__rreplace(whereIn,',','',1)
        
        item = rf"{field} IN ({whereIn})"
        self.useWhereArr.append(item) 
        self.__where_concat() 
        return self 
    
            

    def where(self, fieldsValue): 
        """
        Cria a clausa WHERE = na query

        Returns:
            classe
        """   
        item = rf"{fieldsValue[0]} = '{fieldsValue[1]}'" 
        self.useWhereArr.append(item) 
        self.__where_concat()       
        return self
            

    
    def orderBY(self, field, ordenation = 'ASC'):  
        """
        Faz a ordenação dos registros na query

        Args:
            field (string): campo a ordenar
            ordenation (str, optional): Ordenação. Defaults to 'ASC'.

        Returns:
            classe
        """
        self.useOrderBY = rf"ORDER BY {field} {ordenation}"
        return self    
        
    
    
    def groupBy(self, fields):
        """Agrupa os dados pelas colunas

        Args:
            fields (string): colunas separadas por virgulas
       
        """
        self.useGroupBy = rf"GROUP BY {fields}"
        return self 
            
        
    
    def __where_concat(self, operator = ' AND '):
        """
        Faz o tratamento das clausulas where. Método privado

        Returns:
            classe
        """   
        self.useWhere = ''
        for where in self.useWhereArr:         
            self.useWhere += where + operator 
           
        self.useWhere = self.useWhere.replace('WHERE','')                
        self.useWhere = rf"WHERE {self.useWhere}" 
        self.useWhere = self.__rreplace(self.useWhere, ' AND ', '',1) 
        return   
        
        
        
    def __rreplace(self,text, old, new, count):
        """Replace inverso

        Args:
            text (_type_): texto a pesquisar
            old (_type_): valor antigo
            new (_type_): valor novo
            count (_type_): quantas vezes é para fazer a troca

        Returns:
            _type_: _description_
        """
        return (text[::-1].replace(old[::-1], new[::-1], count))[::-1]
   
   
   
    def insert(self, fieldsValues):
        """
        Insere um ou mais registros no banco

        Args:
            fieldsValues (array): Campos e valores a inserir

        Returns:
            bool
        """
        
        values = ''
        for reg in fieldsValues:  
            value = "("
            for key in reg:                
                value += rf"'{reg[key]}',"
            
            value = self.__rreplace(value, ',', '', 1)
            value += "),"
            values += value              
                
        for reg in fieldsValues:
            fields = ''  
            for field in reg:                
                fields += rf"{field},"             
            
        fields = self.__rreplace(fields, ',', '', 1)        
        values = self.__rreplace(values, ',', '', 1)
        
        
        
        sql = rf"INSERT INTO {self.useTable} ({fields}) VALUES {values}"  
    
        try:                
            result = self.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            
            return False
        
        
    def update(self, fieldsValues):
        
        VALUES = ''
        for reg in fieldsValues:
            value = ''
            for key in reg:
                value += rf"{key} = '{reg[key]}',"
                VALUES += value                
                
        VALUES = self.__rreplace(VALUES, ',', '', 1)       
        
        
        sql = rf"UPDATE {self.useTable} SET {VALUES} {self.useWhere}"
        
      
        try:                
            result = self.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            
            return False
        
            
        
    
    def delete(self):
        """
        Deleta um ou mais registros

        Returns:
            bool
        """
        sql = rf"DELETE FROM {self.useTable} {self.useWhere}"
        try:                
            result = self.execute(sql)
            # self.conn.commit()
            return True
        except Exception as err:
            
            return False
        

       
   