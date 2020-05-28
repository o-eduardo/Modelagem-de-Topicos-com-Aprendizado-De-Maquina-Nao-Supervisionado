import logging as log
import time

import pandas as pd
# load webdriver function from selenium
from selenium import webdriver
import pprint

from Utils.ArquivosUtils import ArquivosUtils
from Utils.ExtracaoUtils import ExtracaoUtils

arquivos_ferramentas = ArquivosUtils()
caminho = "C:\PGC\BaseDeDados/1_2017_longo.pdf"

raw_text = arquivos_ferramentas.obter_texto_pdf(caminho)
print(raw_text)
