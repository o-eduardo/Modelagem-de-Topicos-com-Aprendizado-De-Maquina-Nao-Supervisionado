from Base.BasePage import BasePage

class ListaArtigos(BasePage):

    def __init__(self, driver):
        self.driver = driver
            
    def obter_titulo_artigo(self, elemento):
        super().esperar(self.driver, elemento)
        return super().obter_texto(elemento)

    def obter_url_artigo(self, elemento):
        super().esperar(self.driver, elemento)
        return super().obter_url(elemento)