# -*- coding: utf-8 -*-
import re
from unicodedata import normalize

import nltk
from gensim import corpora
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

from utils.ArquivosUtils import ArquivosUtils


class PreProcessamento:

    def __init__(self):
        nltk.download('stopwords')
        nltk.download('rslp')
        nltk.download('gutenberg')
        nltk.download('punkt')

    def remover_stopwords(self, texto):
        stop_words = set(stopwords.words('portuguese'))
        stop_words_us = set(stopwords.words('english'))
        new_stopwords = ArquivosUtils.obter_lista_novas_stopwords('C:\\PGC\Projeto_PipeLine\\PGC-LDA\\AutomacaoExtracaoDados\\ArtefatosEntrada\\stopwords.txt')
        stop_words.update(new_stopwords)
        stop_words.update([stp.lower() for stp in new_stopwords])
        stop_words.update(stop_words_us)
        palavra = [i for i in texto.lower().split() if i not in stop_words]
        return ' '.join(palavra)

    def tokenizar_texto(self, texto):
        texto_tokenizado = word_tokenize(texto.lower())
        return texto_tokenizado

    def remover_acentos(self, texto):
        return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

    def converter_texto_para_minusculo(self, texto):
        return texto.lower()

    def remover_caracteres_especiais(self, texto):
        texto_sem_carac_esp = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕàÀìÌòÒïÏñÑÜüçÇ ]', "", texto)
        return texto_sem_carac_esp

    def remover_email(self, texto):
        padrao_email = r'[\w+\./{1}]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
        texto_sem_email = re.sub(padrao_email, "", texto)
        return texto_sem_email

    def remover_conjunto_emails(self, texto):
        padrao_email = r'\{[\w+\./{1}\,*]+\}@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
        texto_sem_email = re.sub(padrao_email, "", texto)
        return texto_sem_email

    def remover_enderecos_emails(self, texto):
        texto = self.remover_conjunto_emails(texto)
        texto = self.remover_email(texto)
        return texto

    def remover_url(self, texto):
        padrao_url = r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*'
        texto_sem_url = re.sub(padrao_url, "", texto)
        return texto_sem_url

    def converter_termos_geral(self, texto):
        texto = re.sub(" Universidade Federal de Minas Gerais", " UFMG ", texto)
        texto = re.sub(" Universidade Federal de Ouro Preto", " UFOP ", texto)
        texto = re.sub(" Universidade Federal de Pernambuco", " UFPE ", texto)
        texto = re.sub(" Universidade Federal de Santa Catarina", " UFSC ", texto)
        texto = re.sub(" Universidade Federal de São Carlos", " UFSCAR ", texto)
        texto = re.sub(" Universidade Federal de Sergipe", " UFS ", texto)
        texto = re.sub(" Universidade Federal de Viçosa", " UFV ", texto)
        texto = re.sub(" Universidade Federal do Ceará", " UFC ", texto)
        texto = re.sub(" Universidade Federal do Estado do Rio de Janeiro", " UNIRIO ", texto)
        texto = re.sub(" Universidade Federal do Maranhão", " UFMA ", texto)
        texto = re.sub(" Universidade Federal do Pará", " UFPA ", texto)
        texto = re.sub(" Universidade Federal do Paraná", " UFPR ", texto)
        texto = re.sub(" Universidade Federal do Rio de Janeiro", " UFRJ ", texto)
        texto = re.sub(" Universidade Federal do Rio Grande do Norte", " UFRN ", texto)
        texto = re.sub(" Universidade Federal do Rio Grande do Sul", " UFRGS ", texto)
        texto = re.sub(" Universidade Federal Fluminense", " UFF ", texto)
        texto = re.sub(" Universidade Federal Rural do Rio de Janeiro", " UFRRJ ", texto)
        texto = re.sub(" Pontifícia Universidade Católica", " PUC ", texto)
        texto = re.sub(" Universidade Federal de Goiás", " UFG ", texto)
        texto = re.sub(" Universidade de São Paulo", " USP ", texto)
        texto = re.sub(" Universidade Federal de Santa Maria", " UFSM ", texto)
        texto = re.sub(" Escola Regional de Computação Ceará Maranhão Piauí", " ERCEMAPI ", texto)
        texto = re.sub(" Universidade de Passo Fundo", " UPF ", texto)
        texto = re.sub(" Universidade Federal de Itajubá", " UNIFEI ", texto)
        texto = re.sub(" Escola Regional de Alto Desempenho", " ERAD ", texto)
        texto = re.sub(" Faculdade de Tecnologia e Ciências", " FTC ", texto)
        texto = re.sub(" Instituto Nacional de Pesquisas Espaciais", " INPE ", texto)
        texto = re.sub(" Instituto de Tecnologia de Pernambuco", " ITEP ", texto)
        texto = re.sub(" Pontifícia Universidade Católica do Paraná", " PUCRS ", texto)
        texto = re.sub(" Universidade Estadual de Campinas", " UNICAMP ", texto)
        texto = re.sub(" Fundação Getulio Vargas", " FGV ", texto)
        texto = re.sub(" Universidade Regional Integrada do Alto Uruguai e das Missões", " URI ", texto)
        texto = re.sub(" Colégio Agrícola de Frederico Westphalen", " CAFW ", texto)
        texto = re.sub(" Institute of Electrical and Electronic Engineers", " IEEE ", texto)
        texto = re.sub(" Instituto Federal de Educação Ciência e Tecnologia do Ceará", " IFCE ", texto)
        texto = re.sub(" Universidade Federal do Rio Grande do Sul", " UFRGS ", texto)
        texto = re.sub(" Associação Brasileira de Normas Técnicas", " ABNT ", texto)
        texto = re.sub(" Universidade Luterana do Brasil", " ULBRA ", texto)
        texto = re.sub(" Ministério da Educação", " MEC ", texto)
        texto = re.sub(" Universidade do Estado da Bahia", " UNEB ", texto)
        texto = re.sub(" Instituto Nacional de Estudos e Pesquisas Educacionais", " INEP ", texto)
        texto = re.sub(" Instituto Brasileiro de Geografia Estatística", " IBGE ", texto)
        texto = re.sub(" Universidade Federal do Pampa", " UNIPAMPA ", texto)
        texto = re.sub(" Instituto Federal de Educação Ciência e Tecnologia da Bahia", " IFBA ", texto)
        texto = re.sub(" Centro de Educação Superior Norte RS", " CESNORS ", texto)
        texto = re.sub(" Instituto Federal do Ceará", " IFCE ", texto)
        texto = re.sub(" Massachusetts Institute of Technology", " MIT ", texto)
        texto = re.sub(" Instituto Federal do Paraná", " IFPR ", texto)
        texto = re.sub(" Simpósio de Tecnologia da Informação da Região Noroeste do RS", " STIN ", texto)
        texto = re.sub(" Agência de Desenvolvimento do Médio Alto Uruguai", " ADMAU ", texto)
        texto = re.sub(" Universidade Federal Rural da Amazônia", " UFRA ", texto)
        texto = re.sub(" Sociedade Paranaense de Ensino e Informática", " SPEI ", texto)
        texto = re.sub(" Instituto Federal de Pernambuco", " IFPE ", texto)
        texto = re.sub(" Departamento Estadual de Informática Policial", " DINP ", texto)
        texto = re.sub(" Agência Nacional de Energia Elétrica", " ANEEL ", texto)
        texto = re.sub(" Inteligência Artificial e Tecnologia Educacional", " IATE ", texto)
        texto = re.sub(" Simpósio Brasileiro de Informática na Educação", " SBIE ", texto)
        texto = re.sub(" Universidade Federal da Fronteira Sul", " UFFS ", texto)
        texto = re.sub(" Exame Nacional do Ensino Médio", " ENEM ", texto)
        texto = re.sub("SGBD", " Sistema de Gerenciamento de Banco de Dados", texto)
        texto = re.sub("CNPq", " Conselho Nacional de Desenvolvimento Científico e Tecnológico", texto)
        return texto

    def converter_termos_2011(self, texto):
        texto = re.sub(" LE", " Lingua Estrangeira ", texto)
        texto = re.sub(" EAD", " Educação a Distância ", texto)
        texto = re.sub(" ZPD", " Zona de Desenvolvimento Proximal ", texto)
        texto = re.sub(" CCE", " Centro de Computação Eletrônica ", texto)
        texto = re.sub(" AVAs", " Ambientes Virtuais de Aprendizagem ", texto)
        texto = re.sub(" AVA", " Ambiente Virtual de Aprendizagem ", texto)
        texto = re.sub(" TI", " Tecnologia da Informação ", texto)
        texto = re.sub(" SIG", " Sistemas de Informações Geográficas ", texto)
        texto = re.sub("AIS", " avaliações integradas semestrais ", texto)
        return texto

    def converter_termos_2013(self, texto):
        texto = re.sub("ECM", " Gerenciamento de Conteúdo Corporativo ", texto)
        texto = re.sub("PEA", " Processo de Ensino e de Aprendizagem ", texto)
        texto = re.sub("ACs", " Autômatos Celulares ", texto)
        texto = re.sub("AC", " Autômato Celular ", texto)
        texto = re.sub("SOFTEX", " Programas de Excelência do Software Brasileiro ", texto)
        texto = re.sub("APF", " Administração Pública Federal ", texto)
        texto = re.sub(" TCU", " Tribunal de Contas da União ", texto)
        texto = re.sub(" SIG", " Sistemas de Informações Geográficas ", texto)
        texto = re.sub(" ICTs", " Information and Communication Technologies ", texto)
        texto = re.sub(" ICT", " Information and Communication Technology ", texto)
        texto = re.sub(" BD ", " Banco de Dados ", texto)
        texto = re.sub(" OCR", " Identificação Óptica de Caractere ", texto)
        texto = re.sub(" TACO", " Tabela Brasileira de Composição de Alimentos ", texto)
        texto = re.sub(" TI", " Tecnologia da Informação ", texto)
        texto = re.sub(" EAD", " Educação a Distância ", texto)
        texto = re.sub(" AR ", " Aprendizado por Reforço ", texto)
        texto = re.sub(" TIC", " Tecnologia da Informação e Comunicação ", texto)
        texto = re.sub(" RSSF ", " Redes de Sensores Sem Fio ", texto)
        texto = re.sub(" SGS ", " Sistema de Gestão de Segurança ", texto)
        texto = re.sub(" AE ", " Alinhamento Estratégico ", texto)
        texto = re.sub(" IA ", " Inteligência Artificial ", texto)
        texto = re.sub(" AVAs", " Ambientes Virtuais de Aprendizagem ", texto)
        texto = re.sub(" AVA", " Ambiente Virtual de Aprendizagem ", texto)
        texto = re.sub(" CAD ", " Desenho Assistido por Computador ", texto)
        texto = re.sub(" RBC ", " Raciocínio Baseado em Casos ", texto)
        texto = re.sub(" IES ", " Instituições de Ensino Superior ", texto)
        texto = re.sub(" TI", " Tecnologia da Informação ", texto)
        texto = re.sub(" SUS ", " Sistema Único de Saúde ", texto)
        texto = re.sub(" AVAE", " Ambiente Virtual de Aprendizagem e Ensino ", texto)
        return texto

    def converter_termos_2014(self, texto):
        texto = re.sub(" ABD ", " Aplicação de Banco de Dados ", texto)
        texto = re.sub(" BD ", " Banco de Dados ", texto)
        texto = re.sub(" IT ", " Information Technology ", texto)
        texto = re.sub(" GQA ", " Garantia da Qualidade ", texto)
        texto = re.sub("BDT", " Banco de Dados de Teste ", texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ", texto)
        texto = re.sub(" SND ", " Sistema Neural para Apoio ao Diagnóstico de Diabetes ", texto)
        texto = re.sub(" AG ", " Algoritmo Genético ", texto)
        texto = re.sub(" AGs ", " Algoritmos Genéticos ", texto)
        texto = re.sub(" BI ", " Business Intelligence ", texto)
        texto = re.sub(" FEES ", " Fórum de Educação em Engenharia de Software ", texto)
        texto = re.sub(" TCC ", " Trabalho de Conclusão de Curso ", texto)
        texto = re.sub(" ITIL ", " Information  Technology Infrastructure Library ", texto)
        texto = re.sub(" BDR ", " Banco de Dados de Referência ", texto)
        texto = re.sub(" SUS ", " Sistema Único de Saúde ", texto)
        texto = re.sub(" EAD ", " Educação a Distância ", texto)
        texto = re.sub(" TM ", " Teste de Mutação ", texto)
        texto = re.sub("RNAs", " Redes Neurais Artificiais ", texto)
        texto = re.sub(" RNA ", " Rede Neurail Artificial ", texto)
        texto = re.sub(" SESAU ", " Secretaria  Estadual de Saúde ", texto)
        texto = re.sub(" BDP ", " Banco de Dados de Produção ", texto)
        texto = re.sub(" RUP ", " Rational Unified  Process ", texto)
        texto = re.sub(" AGCA ", " Algoritmos Genéticos Canônicos ", texto)
        texto = re.sub(" TM ", " Recomendação Fuzzy de Objeto de Aprendizagem ", texto)
        texto = re.sub(" OA ", " Objeto de Aprendizagem ", texto)
        texto = re.sub(" OMS ", " Organização Mundial da Saúde ", texto)
        texto = re.sub(" UI ", " Interface do Usuário ", texto)
        texto = re.sub(" FV ", " Fotovoltaica ", texto)
        texto = re.sub(" OBAA ", " Aprendizagem Baseados em Agentes ", texto)
        texto = re.sub(" SI ", " Sistemas de Informação ", texto)
        return texto

    def converter_termos_2015(self, texto):
        texto = re.sub(" TIC", " Tecnologias da Comunicação e Informação ", texto)
        texto = re.sub(" IA", " Inteligência Artificial ", texto)
        texto = re.sub(" CAE ", " Coordenação de Assistência Estudantil ", texto)
        texto = re.sub(" CNES ", " Cadastro Nacional de Estabelecimentos de Saúde ", texto)
        texto = re.sub(" IA ", " Inteligência Artificial ", texto)
        texto = re.sub(" OMS ", " Organização Mundial de Saúde ", texto)
        texto = re.sub(" IPS", " Sistemas de Prevenção de Intrusão ", texto)
        texto = re.sub(" AR", " Aprendizagem por Reforço ", texto)
        texto = re.sub(" OA", " Objeto de Aprendizagem ", texto)
        return texto

    def converter_termos_2016(self, texto):
        texto = re.sub(" OA", " Objeto de Aprendizagem ", texto)
        texto = re.sub(" IA ", " Inteligência Artificial ", texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ", texto)
        texto = re.sub(" IT ", " Information Technology ", texto)
        texto = re.sub(" IPS ", " Sistema de Prevenção de Intrusão ", texto)
        texto = re.sub(" AE", " Algoritmo Evolucionário ", texto)
        texto = re.sub(" GD ", " Gradiente Descendente ", texto)
        texto = re.sub(" AVAs ", " Ambientes Virtuais de Aprendizagem ", texto)
        texto = re.sub(" BI ", " Business Intelligence ", texto)
        texto = re.sub(" VANTs", " Veículos Aéreos Não-Tripulados  ", texto)
        texto = re.sub(" APF", " Administração Pública Federal Brasileira ", texto)
        return texto

    def converter_termos_2017(self, texto):
        texto = re.sub(" VANTs", " Veículos Aéreos Não-Tripulados ", texto)
        texto = re.sub(" BI ", " Business Intelligence ", texto)
        texto = re.sub(" IDS ", " Sistema de Detecção de Intrusão ", texto)
        texto = re.sub(" RBD ", " Diagrama de Blocos de Confiabilidade ", texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ", texto)
        texto = re.sub(" IT ", " Information Technology ", texto)
        texto = re.sub(" IPS ", " Sistema de Prevenção de Intrusão ", texto)
        texto = re.sub(" AE", " Algoritmo Evolucionário ", texto)
        texto = re.sub(" GD ", " Gradiente Descendente ", texto)
        texto = re.sub(" AVAs ", " Ambientes Virtuais de Aprendizagem ", texto)
        texto = re.sub(" HDFS ", " Sistema de Arquivos istribuído Hadoop ", texto)
        texto = re.sub(" ACML ", " Acessibilidade Comunicativa por Meio da Libras ", texto)
        texto = re.sub(" OLAP ", " Online Analytical Processing ", texto)
        texto = re.sub(" SBC ", " Sociedade Brasileira de Computação ", texto)
        texto = re.sub(" APL ", " Arranjo Produtivo Local ", texto)
        texto = re.sub(" AIT ", " Auto de Infração de Trânsito ", texto)
        texto = re.sub(" AITs", " Auto de Infração de Trânsito ", texto)
        return texto

    def converter_termos_2018(self, texto):
        texto = re.sub("PAGMG", " Árvore Geradora Mínima Generalizado ", texto)
        texto = re.sub(" SIGAA ", " Sistema Integrado de Gestão  Acadêmica de Atividades ", texto)
        texto = re.sub(" IHC ", " Interface Humano Computador ", texto)
        texto = re.sub(" UBS ", " Unidade de Beneficiamento de Sementes ", texto)
        texto = re.sub(" TSI ", " Tecnologia em Sistemas para Internet ", texto)
        texto = re.sub(" CBQ ", " Enfileiramento Baseado em Classes ", texto)
        return texto

    def converter_termos_2019(self, texto):
        texto = re.sub(" SBRC ", " Simpósio Brasileiro de Redes de Computadores ", texto)
        texto = re.sub(" SIGAA ", " Sistema Integrado de Gestão Acadêmica de Atividades ", texto)
        texto = re.sub(" EAI ", " Integração de Aplicações Empresariais ", texto)
        texto = re.sub(" AVAs ", " Ambientes Virtuais de Aprendizagem ", texto)
        texto = re.sub(" AVA ", " Ambiente Virtual de Aprendizagem ", texto)
        texto = re.sub(" RFID ", " Identificação por Rádio Frequência ", texto)
        texto = re.sub(" OA", " Objeto de Aprendizagem ", texto)
        texto = re.sub(" CFD ", " Dinâmica de Fluídos Computacional ", texto)
        texto = re.sub(" PSNR ", " Relação Sinal Ruído de Pico ", texto)
        texto = re.sub(" PNL", " Processamento Natural de Linguagem ", texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ", texto)
        texto = re.sub(" ANOVA ", " Análise de Variância ", texto)
        texto = re.sub(" SETI ", " Secretaria Especial de Tecnologia da Informação ", texto)
        texto = re.sub(" MVP ", " Produto Mínimo Viável ", texto)
        return texto

    def remover_textos_layout(self, texto):
        texto = re.sub(
            "Anais do EATI - Encontro Anual de Tecnologia da Informação e Semana Acadêmica de Tecnologia da Informação",
            "", texto.lstrip())
        texto = re.sub("Anais do EATI Frederico Westphalen - RS", "".lower(), texto.lstrip())
        texto = re.sub("STIN – Simpósio de Tecnologia da Informação da Região Noroeste do RS", "", texto.lstrip())
        texto = re.sub("Anais do EATI", "", texto.lstrip())
        texto = re.sub("Encontro Anual de Tecnologia da Informação", "", texto.lstrip())
        texto = re.sub("Semana Acadêmica de Tecnologia da Informação", "", texto.lstrip())
        texto = re.sub("anais2018.pdf", "", texto.lstrip())
        texto = re.sub("                                             ", "", texto.lstrip())
        texto = re.sub("Microsoft Word", "", texto.lstrip())
        texto = re.sub("anais2019 sem pendentes", "", texto.lstrip())
        return texto.lstrip()

    def remover_numeros(self, texto):
        texto_sem_numeros = re.sub(r'\d', "", texto)
        return texto_sem_numeros

    def remover_caracteres_especiais(self, texto):
        texto_sem_carac_esp = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕàÀÜüçÇ ]', "", texto)
        return texto_sem_carac_esp

    def remover_sequencia_espaco_branco(self, texto):
        padrao = re.compile(r"(\s)\1{1,}")
        return padrao.sub(r"\1", texto)

    def remover_palavras_por_tamanho(self, texto, limite):
        lista_texto = self.tokenizar_texto(texto)
        lista_palavras_retorno = []
        separador = ' '
        for palavra in lista_texto:
            if len(palavra) > limite:
                lista_palavras_retorno.append(palavra)
        texto_pos_remocao = separador.join(lista_palavras_retorno)
        return texto_pos_remocao

    def remover_pronomes_obliquos(self, texto):
        texto = re.sub("-o", "", texto)
        texto = re.sub("-e", "", texto)
        texto = re.sub("-a", "", texto)
        texto = re.sub("-lo", "", texto)
        texto = re.sub("-la", "", texto)
        texto = re.sub("-los", "", texto)
        texto = re.sub("-las", "", texto)
        texto = re.sub("-no", "", texto)
        texto = re.sub("-na", "", texto)
        texto = re.sub("-nas", "", texto)
        texto = re.sub("-as", "", texto)
        texto = re.sub("-os", "", texto)
        texto = re.sub("-me", "", texto)
        texto = re.sub("-te", "", texto)
        texto = re.sub("-se", "", texto)
        texto = re.sub("-lhe", "", texto)
        texto = re.sub("-lhes", "", texto)
        texto = re.sub("-nos", "", texto)
        texto = re.sub("-vos", "", texto)
        texto = re.sub("e/ou", "e ou", texto)
        texto = re.sub("cliente/servidor", "cliente servidor", texto)
        texto = re.sub("pré-estabelecidos", "pré estabelecidos", texto)
        return texto

    def remover_estados(self, texto):
        texto = re.sub("/AC", "", texto)
        texto = re.sub("/AL", "", texto)
        texto = re.sub("/AP", "", texto)
        texto = re.sub("/AM", "", texto)
        texto = re.sub("/BA", "", texto)
        texto = re.sub("/CE", "", texto)
        texto = re.sub("/DF", "", texto)
        texto = re.sub("/ES", "", texto)
        texto = re.sub("/MA", "", texto)
        texto = re.sub("/MT", "", texto)
        texto = re.sub("/MS", "", texto)
        texto = re.sub("/MG", "", texto)
        texto = re.sub("/PA", "", texto)
        texto = re.sub("/PB", "", texto)
        texto = re.sub("/PR", "", texto)
        texto = re.sub("/PE", "", texto)
        texto = re.sub("/PI", "", texto)
        texto = re.sub("/RJ", "", texto)
        texto = re.sub("/RN", "", texto)
        texto = re.sub("/RS", "", texto)
        texto = re.sub("/RO", "", texto)
        texto = re.sub("/RR", "", texto)
        texto = re.sub("/SC", "", texto)
        texto = re.sub("/SP", "", texto)
        texto = re.sub("/SE", "", texto)
        texto = re.sub("/TO", "", texto)
        texto = re.sub("-AC", "", texto)
        texto = re.sub("-AL", "", texto)
        texto = re.sub("-AP", "", texto)
        texto = re.sub("-AM", "", texto)
        texto = re.sub("-BA", "", texto)
        texto = re.sub("-CE", "", texto)
        texto = re.sub("-DF", "", texto)
        texto = re.sub("-ES", "", texto)
        texto = re.sub("-MA", "", texto)
        texto = re.sub("-MT", "", texto)
        texto = re.sub("-MS", "", texto)
        texto = re.sub("-MG", "", texto)
        texto = re.sub("-PA", "", texto)
        texto = re.sub("-PB", "", texto)
        texto = re.sub("-PR", "", texto)
        texto = re.sub("-PE", "", texto)
        texto = re.sub("-PI", "", texto)
        texto = re.sub("-RJ", "", texto)
        texto = re.sub("-RN", "", texto)
        texto = re.sub("-RS", "", texto)
        texto = re.sub("-RO", "", texto)
        texto = re.sub("-RR", "", texto)
        texto = re.sub("-SC", "", texto)
        texto = re.sub("-SP", "", texto)
        texto = re.sub("-SE", "", texto)
        texto = re.sub("-TO", "", texto)
        return texto

    def pre_processamento_2011(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2011(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_2013(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2013(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_2014(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2014(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_2015(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2015(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_2016(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2016(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_2017(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2017(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_2018(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2018(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_2019(self, texto):
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.remover_textos_layout(texto)
        texto = self.remover_enderecos_emails(texto)
        texto = self.remover_url(texto)
        texto = self.remover_numeros(texto)
        texto = self.remover_pronomes_obliquos(texto)
        texto = self.remover_estados(texto)
        texto = self.remover_caracteres_especiais(texto)
        texto = self.remover_sequencia_espaco_branco(texto)
        texto = self.converter_termos_geral(texto)
        texto = self.converter_termos_2019(texto)
        texto = self.remover_stopwords(texto)
        texto = self.remover_palavras_por_tamanho(texto, 1)
        texto = self.remover_acentos(texto)
        return texto

    def pre_processamento_lista_artigos(self, edicao_artigo):
        ano_edicao = str(edicao_artigo)
        lista_de_listas = []
        if ano_edicao == "2011":
            nome_arquivo = "corpus_artigos_edicao_2011"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2011(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

        elif ano_edicao == "2013":
            nome_arquivo = "corpus_artigos_edicao_2013"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2013(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

        elif ano_edicao == "2014":
            nome_arquivo = "corpus_artigos_edicao_2014"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2014(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

        elif ano_edicao == "2015":
            nome_arquivo = "corpus_artigos_edicao_2015"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2015(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

        elif ano_edicao == "2016":
            nome_arquivo = "corpus_artigos_edicao_2016"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2016(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

        elif ano_edicao == "2017":
            nome_arquivo = "corpus_artigos_edicao_2017"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2017(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

        elif ano_edicao == "2018":
            nome_arquivo = "corpus_artigos_edicao_2018"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2018(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

        elif ano_edicao == "2019":
            nome_arquivo = "corpus_artigos_edicao_2019"
            lista_artigos_brutos = ArquivosUtils.extracao_artigos_listas(nome_arquivo)
            for linha in lista_artigos_brutos:
                txt_pre = self.pre_processamento_2019(linha)
                lista_txt_pre = txt_pre.split()
                lista_de_listas.append(lista_txt_pre)
            return lista_de_listas

    def unificar_artigos_com_n_gramas(self, lista_de_lista_de_artigos):
        artigo_tokens_unificados = []

        for artigo in lista_de_lista_de_artigos:
            xtexto = artigo
            unigramas = xtexto
            xbigramas = self.construir_bigramas(xtexto)
            xtrigramas = self.construir_trigramas(xtexto)
            xunigramas = unigramas + xbigramas + xtrigramas
            artigo_tokens_unificados.append(xunigramas)
        return artigo_tokens_unificados

    def construir_bigramas(self, artigo_tokenizado):
        bigrams = []
        for i in range(0, len(artigo_tokenizado)):
            if (i == len(artigo_tokenizado) - 1):
                break
            else:
                bigrama_obs = artigo_tokenizado[i] + '_' + artigo_tokenizado[i + 1]
                bigrams.append(bigrama_obs)
        # colocar analise por frequencia aqui
        bigrams = self.remover_ngram_por_frequencia(bigrams, 7)
        return bigrams

    def construir_trigramas(self, artigo_tokenizado):
        trigrams = []
        for i in range(0, len(artigo_tokenizado)):
            if (i == len(artigo_tokenizado) - 2):
                break
            else:
                trigrama_obs = artigo_tokenizado[i] + '_' + artigo_tokenizado[i + 1] + '_' + artigo_tokenizado[i + 2]
                trigrams.append(trigrama_obs)
        # colocar analise por frequencia aqui
        trigrams = self.remover_ngram_por_frequencia(trigrams, 7)
        return trigrams

    def remover_ngram_por_frequencia(self, lista_ngrams, frequencia_limiar):
        fdist = FreqDist(lista_ngrams)
        lista_ngrams_retorno = [w for w in lista_ngrams if fdist[w] >= frequencia_limiar]
        return lista_ngrams_retorno

    def obter_dicionario(self, lista_de_lista_artigos):
        dic_id_palavras = corpora.Dictionary(lista_de_lista_artigos)
        return dic_id_palavras

    def obter_corpus(self, dicionario_artigos, lista_de_lista_artigos):
        corpus_artigo = [dicionario_artigos.doc2bow(lista_artigo) for lista_artigo in lista_de_lista_artigos]
        return corpus_artigo

    def obter_lista_geral_todos_artigos(self):
        lista_artigos_2011 = self.pre_processamento_lista_artigos(2011)
        lista_artigos_2013 = self.pre_processamento_lista_artigos(2013)
        lista_artigos_2014 = self.pre_processamento_lista_artigos(2014)
        lista_artigos_2015 = self.pre_processamento_lista_artigos(2015)
        lista_artigos_2016 = self.pre_processamento_lista_artigos(2016)
        lista_artigos_2017 = self.pre_processamento_lista_artigos(2017)
        lista_artigos_2018 = self.pre_processamento_lista_artigos(2018)
        lista_artigos_2019 = self.pre_processamento_lista_artigos(2019)
        lista_completa = lista_artigos_2011 + lista_artigos_2013 + lista_artigos_2014 + lista_artigos_2015 + lista_artigos_2016 + lista_artigos_2017 + lista_artigos_2018 + lista_artigos_2019
        return lista_completa


