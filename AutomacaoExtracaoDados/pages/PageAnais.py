# -*- coding: utf-8 -*-


class PageAnais:

    def botao_artigos_curtos_2015(self, driver):
        return driver.find_element_by_xpath("//*[@id='centro-id']/a[5]/span")
    
    def botao_artigos_longos_2015(self, driver):
        return driver.find_element_by_xpath("//*[@id='centro-id']/a[4]/span")
    
    def botao_artigos_curtos_2016(self, driver):
        return driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div/div/p[2]/a")

    def botao_artigos_longos_2016(self, driver):
        return driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/p[2]/a")

    def botao_artigos_curtos_2017(self, driver):
        return driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div/div/p[2]/a")
    
    def botao_artigos_longos_2017(self, driver):
        return driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/p[2]/a")
    
    def botao_artigos_curtos_2018(self, driver):
        return driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div/div/p[2]/a")
    
    def botao_artigos_longos_2018(self ,driver):
        return driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/p[2]/a")

    def chaveamento_botao_anais(self, driver, ano_edicao, tipo_artigo):

        if ano_edicao == 2015:
            if tipo_artigo.lower() == "longo":
                return self.botao_artigos_longos_2015(driver)
            elif tipo_artigo.lower() == "curto":
                return self.botao_artigos_curtos_2015(driver)

        elif ano_edicao == 2016:
            if tipo_artigo.lower() == "longo":
                return self.botao_artigos_longos_2016(driver)
            elif tipo_artigo.lower() == "curto":
                return self.botao_artigos_curtos_2016(driver)

        elif ano_edicao == 2017:
            if tipo_artigo.lower() == "longo":
                return self.botao_artigos_longos_2017(driver)
            elif tipo_artigo.lower() == "curto":
                return self.botao_artigos_curtos_2017(driver)

        elif ano_edicao == 2018:
            if tipo_artigo.lower() == "longo":
                return self.botao_artigos_longos_2018(driver)
            elif tipo_artigo.lower() == "curto":
                return self.botao_artigos_curtos_2018(driver)