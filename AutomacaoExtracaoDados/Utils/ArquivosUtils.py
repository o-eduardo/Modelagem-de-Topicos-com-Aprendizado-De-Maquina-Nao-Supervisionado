# -*- coding: utf-8 -*-

import os
import io
import pandas as pd
import requests
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from tika import parser

from pygments.lexers.csound import newline


class ArquivosUtils:

    @staticmethod
    def verificar_diretorio(caminho):
        if not os.path.exists(caminho):
            print("Diretorio nao encontrado. Criando diretório...")
            os.makedirs(caminho)

    @staticmethod
    def validar_tamanho_artigos(caminho_destino):
        lista_arquivos = os.listdir(caminho_destino)
        for arq in lista_arquivos:
            arq_caminho = caminho_destino + arq
            arq_tamanho = os.path.getsize(arq_caminho)
            assert arq_tamanho > 2800, "Verificar arquivo " + arq_caminho

    @staticmethod
    def to_string(alist):
        seperator = ' '
        raw_text = seperator.join(alist)
        return raw_text

    def requisitar_arquivo(self, url_arquivo, caminho_destino, nome_arquivo, extencao_arquivo):
        try:
            self.verificar_diretorio(caminho_destino)
            novo_arquivo_nome = nome_arquivo + "." + extencao_arquivo
            novo_arquivo_caminho = caminho_destino + novo_arquivo_nome
            url_arquivo = url_arquivo.replace("view", "download")
            response_novo_arquivo = requests.get(url_arquivo, allow_redirects=True)
            open(novo_arquivo_caminho, 'wb').write(response_novo_arquivo.content)
            print("Request Artigo - OK")
        except:
            print("Erro na requisicao do arquivo {0}".format(url_arquivo))

    @staticmethod
    def nomear_artigo(lista_artigos_mapeados, ano_edicao, tipo_artigo):
        indice = str(len(lista_artigos_mapeados))
        return indice + "_" + str(ano_edicao) + "_" + tipo_artigo

    def criar_mapeamento_csv(self, lista_mapeamento_artigos, caminho_destino):
        try:
            self.verificar_diretorio(caminho_destino)
            mapa_artigos = pd.concat(lista_mapeamento_artigos, ignore_index=True)
            mapa_artigos.to_csv(caminho_destino + 'mapeamento_Corpus.csv', encoding='utf-8')
            print("Arquivo de mapeamento do corpus foi criado com sucesso.")
        except:
            print("Erro na criação do csv de mapeamento")

    @staticmethod
    def validar_arquivo(caminho_arquivo, formato_arq):
        try:
            assert (os.path.isfile(caminho_arquivo))
            assert (formato_arq in caminho_arquivo)
        except AssertionError:
            print("Arquivo não existe ou não esta no formato {0}.".format(formato_arq))
        except UnboundLocalError:
            print("Arquivo não existe!")
        except IOError:
            print("Arquivo com erro!")

    def obter_texto_pdf_pdfminer(self, caminho_arquivo):
        self.validar_arquivo(caminho_arquivo, ".pdf")
        pdf_resource_manager = PDFResourceManager()
        arq_auxiliar = io.StringIO()
        text_converter = TextConverter(pdf_resource_manager, arq_auxiliar)
        page_interpreter = PDFPageInterpreter(pdf_resource_manager, text_converter)
        try:
            count_page = 0
            with open(caminho_arquivo, 'rb') as fh:
                for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                    page_interpreter.process_page(page)
                    count_page = count_page + 1
                    # print("pagina {0} processada".format(count_page))

                texto_arquivo = arq_auxiliar.getvalue()
                self.validar_conteudo_artivo(texto_arquivo, caminho_arquivo)
        except:
            print("Falha na converção para Texto!\nVerificar: {0}".format(caminho_arquivo))
        finally:
            text_converter.close()
            arq_auxiliar.close()
        if texto_arquivo:
            return texto_arquivo

    def obter_texto_pdf_tika(self, caminho_arquivo):
        self.validar_arquivo(caminho_arquivo, ".pdf")
        try:
            raw = parser.from_file(caminho_arquivo)
            texto_arquivo = (raw['content'].replace("-\n", ""))
            texto_arquivo = (texto_arquivo.replace("\n", " "))
            self.validar_conteudo_artigo(texto_arquivo, caminho_arquivo)
        except:
            print("Falha na converção para Texto!\nVerificar: {0}".format(caminho_arquivo))
        finally:
            if texto_arquivo:
                return texto_arquivo

    def unificar_texto_pdfs(self, caminho_diretorio_pdfs):
        lista_conteudo_texto = []
        lista_arquivos_diretorio = os.listdir(caminho_diretorio_pdfs)
        print("\n*************************************************************************")
        print("Extraindo texto dos PDF's em {0}\n".format(caminho_diretorio_pdfs))
        for arq in lista_arquivos_diretorio:
            arq_caminho = caminho_diretorio_pdfs + arq
            raw_text = self.obter_texto_pdf_tika(arq_caminho)
            lista_conteudo_texto.append(raw_text)
        assert len(lista_arquivos_diretorio) == len(lista_conteudo_texto)
        print("\n*************************************************************************")
        print("\nDados de texto extraidos com sucesso!".format(caminho_diretorio_pdfs))
        return lista_conteudo_texto

    def gerar_arquivo_texto_unificado(self, lista_conteudo_texto, caminho_destino, nome_arquivo):
        print("\n*************************************************************************\n")
        print("Criando arquivo do corpus consolidado...\n")
        try:
            nome_arquivo_completo = caminho_destino + nome_arquivo + ".txt"
            arquivo = open(nome_arquivo_completo, "w", encoding='utf-8')
            for item_artigo in lista_conteudo_texto:
                arquivo.write(item_artigo + '\n')
        except :
            print("Erro na geração do arquivo Unificado de textos! \n")
        finally:
            arquivo.close()
            print("Arquivo do corpus consolidado Gerado com sucesso! \n")
            print("*************************************************************************\n")

    def consolidar_base_arquivos(self, caminho_diretorio_pdfs, caminho_destino_arquivo, nome_arquivo):
        lista_texto_arquivos = self.unificar_texto_pdfs(caminho_diretorio_pdfs)
        self.gerar_arquivo_texto_unificado(lista_texto_arquivos, caminho_destino_arquivo, nome_arquivo)

    def validar_conteudo_artigo(self, texto_arquivo, caminho_arq):
        try:
            #assert ("EATI" in texto_arquivo)
            assert "Resumo" in texto_arquivo
            assert "Refer" in texto_arquivo
        except AssertionError:
            print("*****Verificar conteudo arquivo {0}****".format(caminho_arq))