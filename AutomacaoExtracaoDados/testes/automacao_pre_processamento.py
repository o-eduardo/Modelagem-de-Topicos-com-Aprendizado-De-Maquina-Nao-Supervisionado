from functools import reduce

from preprocessamento.pre_processamento import PreProcessamento
from utils.ArquivosUtils import ArquivosUtils


def main():
    pre_processamento = PreProcessamento()

    # CORPUS COMPLETO
    lista_artigos_geral = pre_processamento.obter_lista_geral_todos_artigos()
    assert type(lista_artigos_geral) == list
    assert len(lista_artigos_geral) == 308

    print("Lista de Lista Todos os Artigos Para Testes : {0}".format(len(lista_artigos_geral)))

    lista_ngrams_geral = pre_processamento.unificar_artigos_com_n_gramas(lista_artigos_geral)
    assert type(lista_ngrams_geral) == list

    print("Lista de Lista Ngrams Geral Para Testes : {0}".format(len(lista_ngrams_geral)))

    # DICIONARIO

    dicionario_geral = pre_processamento.obter_dicionario(lista_ngrams_geral)
    corpus_geral = pre_processamento.obter_corpus(dicionario_geral, lista_ngrams_geral)
    print("Lista de Lista Bag Of Word Para Testes : {0}".format(len(corpus_geral)))
    lista_tamanho = []

    for art in lista_ngrams_geral:
        lista_tamanho.append((len(art)))
    print(len(lista_tamanho))
    import operator
    soma_tam = reduce(operator.add, lista_tamanho)
    media = soma_tam/len(lista_tamanho)
    print("Tamanho médio dos artigos: {}".format(media))

if __name__ == '__main__':
    main()
