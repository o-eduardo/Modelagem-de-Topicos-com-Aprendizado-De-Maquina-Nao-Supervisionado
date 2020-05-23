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

    # chavear ano/tipo artigo para retornar elemento referencia do indice i - jeito de reaproveitar o laço -
    # este chaveamento recebe ano, tipo, indice - fica dentro do laço
    # e assim, talvez de pra fazer padrao 1, padrao 2 e 3