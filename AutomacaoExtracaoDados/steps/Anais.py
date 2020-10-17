from base.BasePage import BasePage

class Anais(BasePage):
    
    def __init__(self, driver):
        self.driver = driver
    
    def clicar_botao_anais(self, elemento):
        super().esperar(self.driver, elemento)
        return super().clicar(elemento)