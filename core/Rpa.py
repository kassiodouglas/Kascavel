from operator import imod
from selenium import webdriver
from core.Storage import Storage
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from core import Log
from pathlib import Path
import os
import shutil

class Rpa():
    
    def __init__(self, config = {"showBrowser":False, "namelog":"rpa"}) -> None:
        
        """Instancia o RPA"""   
        
        self._config = config             
        self.Log = Log()        
        
        self.element_selected = None
        self.fileToDownload = None
        
        try:  
            options = webdriver.ChromeOptions()
            options.add_experimental_option(
                "prefs", 
                {
                "download.default_directory": Storage().basePath('core\\chromedriver\\downloads'),
                "download.prompt_for_download":  False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
                }
            )
            options.add_experimental_option('excludeSwitches', ['enable-logging'])    
            
            if(self._config['showBrowser'] == False):   
                options.add_argument("--headless")      
            self.driver = webdriver.Chrome(executable_path = 'core\\chromedriver\\chromedriver.exe', chrome_options=options)   
            self.windowSize()
            
        except Exception as err:   
            Log(self._config['namelog'],rf"Erro: {err}")
            return None
                

    def click(self, type, value): 
        """
        Retorna o click em um elemento da pagina que pode ser do tipo [XPATH | NAME | ID | CLASS_NAME | TAG_NAME]
        
        :DRIVER: WebDriver
        :ELEMT: array
        
        RETURN bool|element
        """    
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,) 
        self.Log.log(self._config['namelog'],rf"Clicando em elemento {type}:{value}")  
        
        type = type.lower()     
        try:
        
            if(type == 'xpath'):       
                WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, value ))).click()
                
            elif(type == 'name'):
                WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.NAME, value ))).click()
                
            elif(type == 'id'):
                WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.ID, value ))).click()
                
            elif(type == 'clas_name'):
                WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.CLASS_NAME, value ))).click()
                
            elif(type == 'tag_name'):
                WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.TAG_NAME, value ))).click()
                
            else: 
                Log(self._config['namelog'],rf"Erro: Elemento Não encontrado: {type}:{value}")   
    
        except Exception as err:  
            Log(self._config['namelog'],rf"Erro: Elemento Não encontrado: {type}:{value}")         
      
    
        return self 

    
    def url(self, url):      
        """Acessa uma url"""
        self.Log.log(self._config['namelog'],rf"Acessando url: {url}")
        self.driver.get(url)
        return self
    
    
    def findElement(self, by, value): 
        """Procura um elemento na página"""   
        
        try:
            self.Log.log(self._config['namelog'],rf"Procurando elemento: {by}:{value}")
            if by == 'id':
                self.element_selected = self.driver.find_element_by_id(value)
            elif by == 'name':
                self.element_selected = self.driver.find_element_by_name(value)
            elif by == 'xpath':
                self.element_selected = self.driver.find_element_by_xpath(value)
            elif by == 'css':
                self.element_selected = self.driver.find_element_by_css_selector(value)     
           
        except Exception as err:  
            self.Log.log(self._config['namelog'], rf"Erro: Elemento Não encontrado: {by}:{value}") 
                       
        return self
        
        
    def key(self, value):
        """Insere um texto no elemento selecionado"""       
        
        if(self.element_selected != None):
            self.Log.log(self._config['namelog'],rf"Inserindo o texto: '{value}'")
            self.element_selected.send_keys(value)        
        else:
            self.Log.log(self._config['namelog'], rf"Erro: Não há elemento selecionado para inserir texto")  
            self.element_selected = None  
            
        return self
    
    
    def delay(self, timer):
        """Adiciona um delay em segundos"""
        self.Log.log(self._config['namelog'],rf"Aguardando {timer} segundos")
        time.sleep(timer)
        return self
    
    
    def enter(self):
        """Aciona o botão enter do teclado"""
        if(self.element_selected != None):
            self.Log.log(self._config['namelog'],rf"Acionando o ENTER")
            self.element_selected.send_keys(Keys.ENTER)
        else:
            self.Log.log(self._config['namelog'], rf"Erro: Não há elemento selecionado para pressionar enter")   
            self.element_selected = None  
            
        return self
    
    
    def toIframe(self):
        """Pula para um frame"""       
        if(self.element_selected != None):
            self.Log.log(self._config['namelog'],rf"Alterando para iframe selecionado")
            self.driver.switch_to.frame(self.element_selected)
        else:
            self.Log.log(self._config['namelog'], rf"Erro: Não há iframe selecionado") 
            self.element_selected = None  
            
        return self
    
    
    def backoDocument(self):
        """Retorna ao documento base"""
        self.Log.log(self._config['namelog'],rf"Retornando para documento base")
        self.driver.switch_to.default_content()   
        return self
    
    
    def getAttribute(self, name):
        """Recupera um atributo de um elemento selecionado"""
        if(self.element_selected != None):
            self.Log.log(self._config['namelog'],rf"Pegando atributo {name} de {self.element_selected}")
            self.element_selected.get_attribute(name)
        else:
            self.Log.log(self._config['namelog'], rf"Erro: Não há elemento selecionado para pegar o atributo")        
            self.element_selected = None    
                   
        return self
    
    
    def formSubmit(self):
        """Aciona o submit de um formulario selecionado"""
        if(self.element_selected != None):
            self.Log.log(self._config['namelog'],rf"Submit de formulário")
            self.element_selected.submit()
        else:
            self.Log.log(self._config['namelog'], rf"Erro: Não há formulario selecionado para dar o submit")        
            self.element_selected = None  
            
        return self
    
    
    def windowSize(self, size = 'maximize', x=None, y=None):
        """Ajusta a tela do navegador"""
        if size == 'maximize':
            self.driver.maximize_window()
        elif size == 'minimize':
            self.driver.minimize_window()
        elif size == 'set':
            self.driver.set_window_size(x,y)
            

    def waitDownload(self, file, timeOut=300):
        """Aguarda o download de um arquivo"""
        dirdown = Path(Storage().pathRpaDownloads())        
        
        timer = 0        
        stop = False
        while stop == False:
            filesInDown = dirdown.glob('*')  
            filesInDown = sorted(filesInDown) 
            
            for dnfile in filesInDown: 
                if file in os.path.basename(dnfile):
                    self.Log.log(self._config['namelog'], rf"Arquivo '{os.path.basename(dnfile)}' encontrado")  
                    self.fileToDownload = dnfile
                    stop = True
                    
            if(stop == False): 
                timer = timer+1
                time.sleep(1) 
                if(timer<=1):   
                    self.Log.log(self._config['namelog'], rf"Aguardando download do arquivo {file}") 
                 
            
            if(timer >= timeOut and stop == False):
                self.Log.log(self._config['namelog'], rf"Erro: Arquivo '{file}' demorou muito para baixar") 
                stop = True                
        
        return self
    
    
    def moveDownFileTo(self, toDir):
        """Move um arquivo baixado para outro diretorio, utilizado apos waitDownload()"""
        if os.path.isdir(toDir) == False:
            os.makedirs(toDir)
        self.Log.log(self._config['namelog'],rf'Movendo arquivo para {toDir}')       
        shutil.move(self.fileToDownload, toDir)
        return self