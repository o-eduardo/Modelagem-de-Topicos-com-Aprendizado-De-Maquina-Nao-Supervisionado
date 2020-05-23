# -*- coding: utf-8 -*-

class PageListaArtigos:
    
    def artigo_longo_2011(self, driver, id_artigo):
        return driver.find_element_by_xpath("//*[@id='miolo']/div/div[2]/p/a["+id_artigo+"]")

    def artigo_longo_2013(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[4]/div/table/tbody/tr["+id_artigo+"]/td/a")
    
    def artigo_curto_2013(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[6]/div/table/tbody/tr["+id_artigo+"]/td/a")
    
    def artigo_longo_2014(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/div/table/tbody/tr["+id_artigo+"]/td/a")
    
    def artigo_curto_2014(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[4]/div/table/tbody/tr["+id_artigo +"]/td/a")
    
    def artigo_longo_2015(self, driver, id_artigo):
        return driver.find_element_by_xpath("//*[@id='centro']/p["+id_artigo+"]/a")
    
    def artigo_curto_2015(self, driver, id_artigo):
        return driver.find_element_by_xpath("//*[@id='centro']/p["+id_artigo+"]/a")
    
    def artigo_longo_2016(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div/table/tbody/tr["+id_artigo+"]/td[1]/a")
    
    def artigo_curto_2016(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div/table/tbody/tr["+id_artigo+"]/td[1]/a")

    def artigo_longo_2017(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div/table/tbody/tr["+id_artigo+"]/td[1]/a")
    
    def artigo_curto_2017(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div/table/tbody/tr["+id_artigo+"]/td[1]/a")   

    def artigo_longo_2018(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div/table/tbody/tr["+id_artigo+"]/td[1]/a")
    
    def artigo_curto_2018(self, driver, id_artigo):
        return driver.find_element_by_xpath("/html/body/div/table/tbody/tr["+id_artigo+"]/td[1]/a")     
    
    def artigo_longo_2019(self, driver, id_artigo):
        return driver.find_element_by_xpath("//*[@id='pkp_content_main']/div/div/div[2]/div[2]/div[2]/ul/li["+id_artigo+"]/div/ul/li/a")
    
    def artigo_curto_2019(self, driver, id_artigo):
        return driver.find_element_by_xpath("//*[@id='pkp_content_main']/div/div/div[2]/div[2]/div[3]/ul/li["+id_artigo+"]/div/ul/li/a") 
    
    def chaveamento_artigo(self, driver, ano_edicao, tipo_artigo, id):
        if ano_edicao == 2011:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2011(driver, id)

        elif ano_edicao == 2013:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2013(driver, id)
            elif tipo_artigo.lower() == "curto":
                return self.artigo_curto_2013(driver, id)

        elif ano_edicao == 2014:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2014(driver, id)
            elif tipo_artigo.lower() == "curto":
                return self.artigo_curto_2014(driver, id)

        elif ano_edicao == 2015:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2015(driver, id)
            elif tipo_artigo.lower() == "curto":
                return self.artigo_curto_2015(driver, id)

        elif ano_edicao == 2016:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2016(driver, id)
            elif tipo_artigo.lower() == "curto":
                return self.artigo_curto_2016(driver, id)

        elif ano_edicao == 2017:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2017(driver, id)
            elif tipo_artigo.lower() == "curto":
                return self.artigo_curto_2017(driver, id)

        elif ano_edicao == 2018:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2018(driver, id)
            elif tipo_artigo.lower() == "curto":
                return self.artigo_curto_2018(driver, id)

        elif ano_edicao == 2019:
            if tipo_artigo.lower() == "longo":
                return self.artigo_longo_2019(driver, id)
            elif tipo_artigo.lower() == "curto":
                return self.artigo_curto_2019(driver, id)
    
    
    
    
    
    
    
    
    
    
    