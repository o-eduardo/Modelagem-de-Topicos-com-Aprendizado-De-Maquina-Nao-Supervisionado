# -*- coding: utf-8 -*-

import logging as log
import time

import pandas as pd
# load webdriver function from selenium
from selenium import webdriver

from utils.ArquivosUtils import ArquivosUtils
from utils.ExtracaoUtils import ExtracaoUtils


def acionar_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\\Users\\SA31\\Downloads\\dt\\Win_337026_chrome-win32\\chrome-win32\\chrome.exe"
    driver = webdriver.Chrome("C:\ChromeDriver\chromedriver")
    return driver


def extracao_2011(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_1(2011, "LONGO", 1, 12, lista_artigos_mapa, caminho_destino, False)


def extracao_2013(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_2(2013, 1, 29, 1, 22, lista_artigos_mapa, caminho_destino)


def extracao_2014(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_2(2014, 1, 30, 1, 33, lista_artigos_mapa, caminho_destino)


def extracao_2015(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_3(2015, 3, 32, 3, 17, lista_artigos_mapa, caminho_destino)


def extracao_2016(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_3(2016, 1, 24, 1, 20, lista_artigos_mapa, caminho_destino)


def extracao_2017(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_3(2017, 1, 17, 1, 19, lista_artigos_mapa, caminho_destino)


def extracao_2018(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_3(2018, 1, 15, 1, 15, lista_artigos_mapa, caminho_destino)


def extracao_2019(driver, lista_artigos_mapa, caminho_destino):
    extract = ExtracaoUtils(driver, caminho_destino, log)
    extract.extracao_padrao_2(2019, 1, 16, 1, 11, lista_artigos_mapa, caminho_destino)

def main():

    inicio = time.time()
    caminho_artigos = "ArtefatosSaida\BaseArtigosExtraidos/"
    caminho = 'ArtefatosSaida/'
    driver = acionar_driver()
    artigos_mapeamento = []
    extracao_2011(driver, artigos_mapeamento, caminho_artigos)
    extracao_2013(driver, artigos_mapeamento, caminho_artigos)
    extracao_2014(driver, artigos_mapeamento, caminho_artigos)
    extracao_2015(driver, artigos_mapeamento, caminho_artigos)
    extracao_2016(driver, artigos_mapeamento, caminho_artigos)
    extracao_2017(driver, artigos_mapeamento, caminho_artigos)
    extracao_2018(driver, artigos_mapeamento, caminho_artigos)
    extracao_2019(driver, artigos_mapeamento, caminho_artigos)

    arquivos_ferramentas = ArquivosUtils()
    arquivos_ferramentas.criar_mapeamento_csv(artigos_mapeamento, caminho)
    driver.close()
    dataSaida = pd.read_csv('../ArtefatosSaida/mapeamento_Corpus.csv')
    ids_artigos = list(dataSaida["ID do Artigo"])
    assert len(artigos_mapeamento) == 308
    assert len(ids_artigos) == len(set(ids_artigos))
    arquivos_ferramentas.validar_tamanho_artigos(caminho_artigos)
    fim = time.time()
    print("Automação Finalizada com sucesso. \n\nTempo de execução: {0} min.".format(round((fim-inicio)/60)))

if __name__ == '__main__':
    main()

