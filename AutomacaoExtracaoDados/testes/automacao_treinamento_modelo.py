from pprint import pprint

import gensim
from preprocessamento.pre_processamento import PreProcessamento
from treinamento.treinamento_modelo_lda import TreinamentoModelo


def main():
    local_arquivo_treino = 'C:\\PGC\\Projeto_PipeLine\\PGC-LDA\\AutomacaoExtracaoDados\\ArtefatosSaida\\treinamento_modelo_lda_v2'
    pre_processamento = PreProcessamento()
    treianemto_modelo = TreinamentoModelo()

    # CORPUS COMPLETO
    lista_artigos_geral = pre_processamento.obter_lista_geral_todos_artigos()
    lista_ngrams_geral = pre_processamento.unificar_artigos_com_n_gramas(lista_artigos_geral)

    # DICIONARIO
    dicionario_geral = pre_processamento.obter_dicionario(lista_ngrams_geral)
    corpus_geral = pre_processamento.obter_corpus(dicionario_geral, lista_ngrams_geral)

    # TESTE DA OBTENÇÃO DE UMA INSTANCIA DO MODELO
    meu_modelo = treianemto_modelo.obter_modelo_lda(corpus_geral, dicionario_geral, 20, 0.31)
    coer = treianemto_modelo.calcular_coerencia_modelo(meu_modelo, lista_ngrams_geral, dicionario_geral)
    assert coer <= 1
    assert type(meu_modelo) == gensim.models.ldamulticore.LdaMulticore
    print(coer)
    print(type(meu_modelo))
    pprint(meu_modelo.print_topics())

    # TESTE DA FUNCAO DE TREINAMENTO - OTIMIZACAO DA COERENCIA
    print("INICIANDO TESTE DO TREINAMENTO E OBTENCAO DA PLANILHA...\n\n")
    treianemto_modelo.gerar_planilha_treinamento_modelo(corpus_geral, dicionario_geral, lista_ngrams_geral, local_arquivo_treino)


if __name__ == '__main__':
    main()
