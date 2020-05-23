import pandas as pd
import os
from Pages.PageListaArtigos import PageListaArtigos
from Pages.PageAnais import PageAnais
from Steps.Anais import Anais
from Steps.ListaArtigos import ListaArtigos
from Utils.ArquivosUtils import ArquivosUtils


class ExtracaoUtils:

    def __init__(self, driver, caminho_extracao, log):
        self.caminho_destino_extracao = caminho_extracao
        self.driver = driver
        self.log = log
        log.basicConfig(filename='ArtefatosSaida/logAutomacao.log', level=log.INFO)


    def url_anais_ano(self, ano_edicao):
        # função que le o csv com dados de entrada (URL's) e recupera a URL pelo ano recebido
        try:
            dataEntrada = pd.read_csv('ArtefatosEntrada/URLsEventos.csv')
            linhaUrlAno = dataEntrada.loc[dataEntrada['Ano'] == ano_edicao]
            urlAno = linhaUrlAno['URL']
            # print(urlAno)
            return urlAno.values[0]
        except:
            print("Erro na busca do arquivo fonte das URL's. Verifique")
            return 0

    def mapear_info_listagem(self, elemento_artigo, lista_mapeamento, ano_artigo, tipo_artigo):
        try:
            lista_artigos = ListaArtigos(self.driver)
            titulo_artigo = lista_artigos.obter_titulo_artigo(elemento_artigo)
            url_artigo = lista_artigos.obter_url_artigo(elemento_artigo)
            temp = pd.DataFrame({'ID do Artigo': len(lista_mapeamento)+1, 'Titulo do Artigo': titulo_artigo,
                                 'URL': url_artigo, 'Ano': ano_artigo, 'Tipo de Artrigo': tipo_artigo}, index=[0])
            lista_mapeamento.append(temp)
            print(temp.values)
        except IndexError:
            print('Erro no mapeamento - elemento inválido')
        except:
            print("Erro no mapeamento")

    def extracao_padrao_1(self, ano_edicao, tipo_artigo, ele_ini, ele_fim, lista_artigos_mapeados,
                          caminho_destino_artigos, eh_pagina_anais_evento):
        url_artigo = self.url_anais_ano(ano_edicao)
        self.driver.get(url_artigo)
        page_lista_artigos = PageListaArtigos()
        lista_artigos = ListaArtigos(self.driver)
        arquivos_ferramentas = ArquivosUtils()

        if eh_pagina_anais_evento:
            page_anais = PageAnais()
            anais = Anais(self.driver)
            botao_anais = page_anais.chaveamento_botao_anais(self.driver, ano_edicao, tipo_artigo)
            anais.clicar_botao_anais(botao_anais)

        for indice in range(ele_ini, ele_fim + 1):
            try:
                indice = str(indice)
                artigos_pagina = page_lista_artigos.chaveamento_artigo(self.driver, ano_edicao, tipo_artigo, indice)
                url_artigo = lista_artigos.obter_url_artigo(artigos_pagina)
                self.mapear_info_listagem(artigos_pagina, lista_artigos_mapeados, ano_edicao, tipo_artigo)
                nome_arquivo = arquivos_ferramentas.nomear_artigo(lista_artigos_mapeados, ano_edicao, tipo_artigo)
                arquivos_ferramentas.requisitar_arquivo(url_artigo, caminho_destino_artigos, nome_arquivo, "pdf")
                self.log.info(nome_arquivo + " - Status: Finished")
            except:
                print('Erro no mapeamento {0}'.format(indice))
                self.log.info(ano_edicao + indice + " - Status: Fail")
                continue

    def extracao_padrao_2(self, ano_edicao, ele_ini_longo, ele_fim_longo, ele_ini_curto, ele_fim_curto,
                          lista_artigos_mapeados, caminho_destino_artigos):
        self.extracao_padrao_1(ano_edicao, "LONGO", ele_ini_longo, ele_fim_longo, lista_artigos_mapeados,
                               caminho_destino_artigos, False)
        self.extracao_padrao_1(ano_edicao, "CURTO", ele_ini_curto, ele_fim_curto, lista_artigos_mapeados,
                               caminho_destino_artigos, False)

    def extracao_padrao_3(self, ano_edicao, ele_ini_longo, ele_fim_longo, ele_ini_curto, ele_fim_curto,
                          lista_artigos_mapeados, caminho_destino_artigos):
        self.extracao_padrao_1(ano_edicao, "LONGO", ele_ini_longo, ele_fim_longo, lista_artigos_mapeados,
                               caminho_destino_artigos, True)
        self.extracao_padrao_1(ano_edicao, "CURTO", ele_ini_curto, ele_fim_curto, lista_artigos_mapeados,
                               caminho_destino_artigos, True)