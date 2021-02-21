# -*- coding: utf-8 -*-
import time
import tqdm
import pandas
from gensim.models import CoherenceModel
import gensim


class TreinamentoModelo:

    @staticmethod
    def obter_modelo_lda(corpus_artigos, dicionario_artigo, numero_de_topicos, hiper_param_alfa):
        inicio = time.time()

        lda_model = gensim.models.LdaMulticore(corpus=corpus_artigos,
                                               id2word=dicionario_artigo,
                                               num_topics=numero_de_topicos,
                                               random_state=100,
                                               # update_every=1,
                                               chunksize=100,
                                               passes=50,
                                               alpha=hiper_param_alfa,
                                               eta=0.1,
                                               per_word_topics=True)
        fim = time.time()
        tempo_execucao = round((fim - inicio) / 60)
        if tempo_execucao < 1:
            tempo_execucao = 1
        #print("Execução estimada da obtenção de um objeto de modelo LDA: Até {0} Min(s)".format(tempo_execucao))

        return lda_model

    def calcular_coerencia_modelo(self, modelo_lda, lista_de_lista_artigos, dicionario):
        #print("Iniciando o Calculo da coerencia de um objeto de modelo LDA")

        modelo_coerencia_lda = CoherenceModel(model=modelo_lda, texts=lista_de_lista_artigos,
                                              dictionary=dicionario, coherence='c_v')
        valor_coerencia_lda = modelo_coerencia_lda.get_coherence()
        #print("Coerencia calculada com sucesso!\n")
        print("\nCoerencia C_v: {0}".format(valor_coerencia_lda))

        return round(valor_coerencia_lda, 4)

    def gerar_planilha_treinamento_modelo(self, corpus_de_dados, dicionario, lista_unificada, nome_arquivo):
        grid = {'Validation_Set': {}}

        topics_range = [5, 15, 25, 35, 45, 50, 55, 65, 75]
        # Alpha parameter
        # {0.01, 0.31, 0.61, 0909, symmetric, asymmetric}

        alpha = [0.01, 0.31, 0.61, 0.909, 'symmetric', 'asymmetric']

        beta = [0.01]

        # Validation sets
        num_of_docs = len(corpus_de_dados)
        corpus_sets = [#gensim.utils.ClippedCorpus(corpus_de_dados, num_of_docs*0.25),
                       #gensim.utils.ClippedCorpus(corpus_de_dados, num_of_docs*0.5),
                       #gensim.utils.ClippedCorpus(corpus_de_dados, num_of_docs*0.75),
                       corpus_de_dados]

        #corpus_title = ['75% Corpus', '100% Corpus']
        corpus_title = ['100% Corpus']

        model_results = {'Conjunto_De_Validacao': [],
                         'Topicos': [],
                         'Alpha': [],
                         'Beta': [],
                         'Coerencia_Cv': []
                         }

        barra_load = len(topics_range) * len(alpha) * len(corpus_sets) * len(beta)

        print("\n\nPREVISAO DE TERMINO: {} MIN\n\n".format((barra_load * 1)))
        if 1 == 1:
            pbar = tqdm.tqdm(total=barra_load)

            # iterate through validation corpuses
            for i in range(len(corpus_sets)):
                # iterate through number of topics
                for k in topics_range:
                    # iterate through alpha values
                    for a in alpha:
                        # iterare through beta values
                        for b in beta:
                            # get the coherence score for the given parameters
                            meu_modelo = TreinamentoModelo.obter_modelo_lda(corpus_sets[i], dicionario, k, a)

                            cv = self.calcular_coerencia_modelo(meu_modelo, lista_unificada, dicionario)
                            # Save the model results
                            #print(" {}".format(cv))
                            pbar.update(1)
                            model_results['Conjunto_De_Validacao'].append(corpus_title[i])
                            model_results['Topicos'].append(str(k))
                            model_results['Alpha'].append(str(a))
                            model_results['Beta'].append(str(b))
                            model_results['Coerencia_Cv'].append(cv)

                            # pbar.update(1)
            pandas.DataFrame(model_results).to_csv(nome_arquivo + '.csv', index=False)
            pbar.close()
