import os
import io
import pandas as pd
import requests
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


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

    def obter_texto_pdf(self, caminho_arquivo):
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
                    print("pagina {0} processada".format(count_page))

                texto_arquivo = arq_auxiliar.getvalue()
        except:
            print("Falha na converção para Texto!\nVerificar: {0}".format(caminho_arquivo))
        finally:
            text_converter.close()
            arq_auxiliar.close()
            assert ("EATI" in texto_arquivo)
            if texto_arquivo:
                return texto_arquivo
