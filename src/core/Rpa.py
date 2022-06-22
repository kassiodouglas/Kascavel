from selenium import webdriver
from src.core.Storage import Storage
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class Rpa():
    
    def __init__(self, config = {"show":False}) -> None:
        
        """Instancia o RPA"""
        
        self.element_selected = ''
        
        try:  
            options = webdriver.ChromeOptions()
            options.add_experimental_option(
                "prefs", 
                {
                "download.default_directory": 'src\\core\\chromedriver\\downloads',
                "download.prompt_for_download":  False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
                }
            )
            options.add_experimental_option('excludeSwitches', ['enable-logging'])    
            
            if(config['show'] == False):   
                options.add_argument("--headless")      
            self.driver = webdriver.Chrome(executable_path = 'src\\core\\chromedriver\\chromedriver.exe', chrome_options=options)   
            self.driver.maximize_window()   
            
        except Exception as err:   
            print(rf"Erro: {err}", 'error')
            return None
                

    def click(self, type, value): 
        """
        Retorna o click em um elemento da pagina que pode ser do tipo [XPATH | NAME | ID | CLASS_NAME | TAG_NAME]
        
        :DRIVER: WebDriver
        :ELEMT: array
        
        RETURN bool|element
        """    
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)     

        time.sleep(1)
        try:
        
            if(type == 'xpath'):       
                return WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, value ))).click()
                
            elif(type == 'name'):
                return WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.NAME, value ))).click()
                
            elif(type == 'id'):
                return WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.ID, value ))).click()
                
            elif(type == 'clas_name'):
                return WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.CLASS_NAME, value ))).click()
                
            elif(type == 'tag_name'):
                return WebDriverWait(self.driver, 60,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.TAG_NAME, value ))).click()
                
            else:               
                return self 
    
        except Exception as err:  
            print(rf"Erro: Elemento Não encontrado: {type}:{value}")         
            return False

    
    def url(self, url):      
        """Acessa uma url"""
        self.driver.get(url)
        return self
    
    
    def findElement(self, by, value): 
        """Procura um elemento na página"""   
        if by == 'id':
            self.element_selected = self.driver.find_element_by_id(value)
        elif by == 'name':
            self.element_selected = self.driver.find_element_by_name(value)
        elif by == 'xpath':
            self.element_selected = self.driver.find_element_by_xpath(value)
        elif by == 'css':
            self.element_selected = self.driver.find_element_by_css_selector(value)           
            
        return self
        
        
    def key(self, value):
        """Insere um texto no elemento selecionado"""
        self.element_selected.send_keys(value)        
        return self
    
    
    def delay(self, timer):
        """Adiciona um delay em segundos"""
        time.sleep(timer)
        return self
    
    
    def enter(self):
        """Aciona o botão enter do teclado"""
        self.element_selected.send_keys(Keys.ENTER)
        return self
    
    
    def toIframe(self):
        """Pula para um frame"""
        self.driver.switch_to.frame(self.element_selected)
        return self
    
    
    def toDocument(self):
        """Retorna ao documento base"""
        self.driver.switch_to.default_content()   
        return self
    
    
    def getAttribute(self, name):
        """Recupera um atributo de um elemento selecionado"""
        self.element_selected.get_attribute(name)
        return self
    
    
    def formSubmit(self):
        """Aciona o submit de um formulario selecionado"""
        self.element_selected.submit()
        return self