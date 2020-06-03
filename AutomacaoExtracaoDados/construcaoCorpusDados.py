import time


from Utils.ArquivosUtils import ArquivosUtils
from Utils.ExtracaoUtils import ExtracaoUtils

arquivos_ferramentas = ArquivosUtils()
caminho = "C:\PGC\BaseDeDados/1_2017_longo.pdf"

inicio = time.time()
#"C:\PGC\BaseDeDados/ é diretorio local, ainda nao esta apontando para os arquivos extraidos
arquivos_ferramentas.consolidar_base_arquivos("C:\PGC\BaseDeDados/", "ArtefatosSaida/", "corpus_artigos")
fim = time.time()
print("Automação Finalizada com sucesso.\nTempo de execução: {0} min.".format(round((fim - inicio) / 60)))


