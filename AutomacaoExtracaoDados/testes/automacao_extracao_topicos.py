from pprint import pprint

import gensim
import pyLDAvis
import pyLDAvis.gensim
import time

from preprocessamento.pre_processamento import PreProcessamento
from treinamento.treinamento_modelo_lda import TreinamentoModelo


def main():
    local_arquivo_topicos = 'C:\\PGC\\Projeto_PipeLine\\PGC-LDA\\AutomacaoExtracaoDados\\ArtefatosSaida' \
                            '\\modelo_lda_v3'
    pre_processamento = PreProcessamento()
    treianemto_modelo = TreinamentoModelo()

    # CORPUS COMPLETO
    #lista_artigos_geral = pre_processamento.obter_lista_geral_todos_artigos()
    lista_artigos_geral = pre_processamento.pre_processamento_lista_artigos(2015)
    lista_ngrams_geral = pre_processamento.unificar_artigos_com_n_gramas(lista_artigos_geral)

    # DICIONARIO
    dicionario_geral = pre_processamento.obter_dicionario(lista_ngrams_geral)
    corpus_geral = pre_processamento.obter_corpus(dicionario_geral, lista_ngrams_geral)

    # OBTENDO OS TOPICOS APOS TREINAMENTO
    # HIPERPARAMETROS:
    # k = 50
    # Alpha = symmetric
    # Beta = 0.01

    #meu_modelo_geral = treianemto_modelo.obter_modelo_lda(corpus_geral, dicionario_geral, 50, "symmetric")
    meu_modelo_geral = treianemto_modelo.obter_modelo_lda(corpus_geral, dicionario_geral, 7, 0.61)
    coer = treianemto_modelo.calcular_coerencia_modelo(meu_modelo_geral, lista_ngrams_geral, dicionario_geral)
    assert coer <= 1
    assert type(meu_modelo_geral) == gensim.models.ldamulticore.LdaMulticore
    print("Coerencia do modelo de tópicos {}".format(coer))
    pprint(meu_modelo_geral.print_topics(10))
    #meu_modelo_geral.save(local_arquivo_topicos)

    pyLDAvis.enable_notebook(local=True)
    vis = pyLDAvis.gensim.prepare(meu_modelo_geral, corpus_geral, dicionario_geral)
    pyLDAvis.display(vis)

if __name__ == '__main__':
    main()
