# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def obter_texto(self, elemento):
         return elemento.text
         
    def obter_url(self, elemento):
         return elemento.get_attribute('href')
    
    def clicar(self, elemento):
        elemento.click()
        
    def esperar(self, driver, elemento):
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of(elemento))
        except:
            print("Elemento não encontrado a tempo!")
         

