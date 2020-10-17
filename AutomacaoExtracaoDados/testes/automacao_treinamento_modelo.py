from pprint import pprint
import numpy as np
import tqdm
import pandas
from preprocessamento.pre_processamento import PreProcessamento
from treinamento.treinamento_modelo_lda import TreinamentoModelo


def main():
    pre_processamento = PreProcessamento()
    treianemto_modelo = TreinamentoModelo()


    # CORPUS COMPLETO
    lista_artigos_geral = pre_processamento.obter_lista_geral_todos_artigos()
    lista_ngrams_geral = pre_processamento.unificar_artigos_com_n_gramas(lista_artigos_geral)

    # DICIONARIO
    dicionario_geral = pre_processamento.obter_dicionario(lista_ngrams_geral)
    corpus_geral = pre_processamento.obter_corpus(dicionario_geral, lista_ngrams_geral)

    meu_modelo = treianemto_modelo.obter_modelo_lda(corpus_geral, dicionario_geral, 20, 0.31)
    coer = treianemto_modelo.calcular_coerencia_modelo(meu_modelo, lista_ngrams_geral, dicionario_geral)
    print(coer)
    pprint(meu_modelo.print_topics())

if __name__ == '__main__':
    main()
