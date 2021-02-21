import time


from utils.ArquivosUtils import ArquivosUtils


def main():
    arquivos_ferramentas = ArquivosUtils()
    inicio = time.time()
    arquivos_ferramentas.consolidar_base_arquivos("ArtefatosSaida\BaseArtigosExtraidos/", "ArtefatosSaida/",
                                                  "corpus_artigos")
    arquivos_ferramentas.consolidar_base_arquivos_ano_edicao("ArtefatosSaida\BaseArtigosExtraidos/", "ArtefatosSaida/",
                                                             "corpus_artigos_edicao")
    fim = time.time()
    print("Consolidação do Corpus Finalizada com sucesso.\nTempo de execução: {0} min.".format(
        round((fim - inicio) / 60)))

if __name__ == '__main__':
    main()