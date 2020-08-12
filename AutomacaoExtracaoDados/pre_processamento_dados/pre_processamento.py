# -*- coding: utf-8 -*-
import nltk

from utils.ArquivosUtils import ArquivosUtils

nltk.download('stopwords')
nltk.download('rslp')
nltk.download('gutenberg')
nltk.download('punkt')

from unicodedata import normalize
from nltk.probability import FreqDist

import re
from nltk import word_tokenize
from nltk.corpus import stopwords

class PreProcessamento:

    @staticmethod
    def remover_stopwords(texto):
        stop_words = set(stopwords.words('portuguese'))
        stop_words_us = set(stopwords.words('english'))
        new_stopwords = ArquivosUtils.obter_lista_novas_stopwords('ArtefatosEntrada/stopwords.txt')
        stop_words.update(new_stopwords)
        stop_words.update(stop_words_us)
        palavra = [i for i in texto.lower().split() if i not in stop_words]
        return ' '.join(palavra)

    @staticmethod
    def tokenizar_texto(texto):
        texto_tokenizado = word_tokenize(texto.lower())
        return texto_tokenizado

    @staticmethod
    def remover_acentos(texto):
        return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

    @staticmethod
    def converter_texto_para_minusculo(texto):
      return texto.lower()

    @staticmethod
    def remover_caracteres_especiais_e_numericos(texto):
        texto_sem_carac_num = re.sub(r'[^a-zA-Z \n]', "", texto)
        return texto_sem_carac_num

    @staticmethod
    def remover_email(texto):
        padrao_email = r'[\w+\./{1}]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
        texto_sem_email = re.sub(padrao_email, "", texto)
        return texto_sem_email

    @staticmethod
    def remover_conjunto_emails(texto):
        padrao_email = r'\{[\w+\./{1}\,*]+\}@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
        texto_sem_email = re.sub(padrao_email, "", texto)
        return texto_sem_email

    @staticmethod
    def remover_enderecos_emails(texto):
        texto = PreProcessamento.remover_conjunto_emails(texto)
        texto = PreProcessamento.remover_email(texto)
        return texto

    @staticmethod
    def remover_url(texto):
        padrao_url = r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*'
        texto_sem_url = re.sub(padrao_url, "", texto)
        return texto_sem_url

    @staticmethod
    def converter_termos_geral(texto):
        texto = re.sub(" universidade federal de minas gerais ", " ufmg ", texto.lower())
        texto = re.sub(" universidade federal de ouro preto ", " ufop ", texto.lower())
        texto = re.sub(" universidade federal de pernambuco ", " ufpe ", texto.lower())
        texto = re.sub(" universidade federal de santa caratina ", " ufsc ", texto.lower())
        texto = re.sub(" universidade federal de são carlos ", " ufscar ", texto.lower())
        texto = re.sub(" universidade federal de sergipe ", " ufs ", texto.lower())
        texto = re.sub(" universidade federal de viçosa ", " ufv ", texto.lower())
        texto = re.sub(" universidade federal do ceará ", " ufc ", texto.lower())
        texto = re.sub(" universidade federal do estado do rio de janeiro ", " unirio ", texto.lower())
        texto = re.sub(" universidade federal do maranhão ", " ufma ", texto.lower())
        texto = re.sub(" universidade federal do pará ", " ufpa ", texto.lower())
        texto = re.sub(" universidade federal do paraná ", " ufpr ", texto.lower())
        texto = re.sub(" universidade federal do rio de janeiro ", " ufrj ", texto.lower())
        texto = re.sub(" universidade federal do rio grande do norte ", " ufrn ", texto.lower())
        texto = re.sub(" universidade federal do rio grande do sul  ", " ufrgs ", texto.lower())
        texto = re.sub(" universidade federal fluminense ", " uff ", texto.lower())
        texto = re.sub(" universidade federal rural do rio de janeiro ", " ufrrj ", texto.lower())
        texto = re.sub(" pontifícia universidade católica ", " puc ", texto.lower())
        texto = re.sub(" universidade federal de goiás ", " ufg ", texto.lower())
        texto = re.sub(" universidade de são paulo ", " usp ", texto.lower())
        texto = re.sub(" universidade federal de santa maria ", " ufsm ", texto.lower())
        texto = re.sub(" escola regional de computação ceará maranhão piauí ", " ERCEMAPI ", texto.lower())
        texto = re.sub(" Universidade de Passo Fundo ".lower(), " UPF ".lower(), texto.lower())
        texto = re.sub(" Universidade Federal de Itajubá ".lower(), " UNIFEI ".lower(), texto.lower())
        texto = re.sub(" Escola Regional de Alto Desempenho ".lower(), " ERAD ".lower(), texto.lower())
        texto = re.sub(" Faculdade de tecnologia e ciências ".lower(), " FTC ".lower(), texto.lower())
        texto = re.sub(" Instituto Nacional de Pesquisas Espaciais ".lower(), " INPE ".lower(), texto.lower())
        texto = re.sub(" Instituto de Tecnologia de Pernambuco ".lower(), " ITEP ".lower(), texto.lower())
        texto = re.sub(" Pontifícia Universidade Católica do Paraná ".lower(), " PUCRS ".lower(), texto.lower())
        texto = re.sub(" Universidade Estadual de Campinas ".lower(), " UNICAMP ".lower(), texto.lower())
        texto = re.sub(" Fundação Getulio Vargas ".lower(), " FGV ".lower(), texto.lower())
        texto = re.sub(" Universidade Regional Integrada do Alto Uruguai e das Missões ".lower(), " URI ".lower(),
                       texto.lower())
        texto = re.sub(" Colégio Agrícola de Frederico Westphalen ".lower(), " CAFW ".lower(), texto.lower())
        texto = re.sub(" Institute of Electrical and Electronic Engineers ".lower(), " IEEE ".lower(), texto.lower())
        texto = re.sub(" Instituto Federal de Educação Ciência e Tecnologia do Ceará ".lower(), " IFCE ".lower(),
                       texto.lower())
        texto = re.sub(" Universidade Federal do Rio Grande do Sul ".lower(), " UFRGS ".lower(), texto.lower())
        texto = re.sub(" Associação Brasileira de Normas Técnicas ".lower(), " ABNT ".lower(), texto.lower())
        texto = re.sub(" Universidade Luterana do Brasil ".lower(), " ULBRA ".lower(), texto.lower())
        texto = re.sub(" Ministério da Educação ".lower(), " MEC ".lower(), texto.lower())
        texto = re.sub(" Universidade do Estado da Bahia ".lower(), " UNEB ".lower(), texto.lower())
        texto = re.sub(" Instituto Nacional de Estudos e Pesquisas Educacionais ".lower(), " INEP ".lower(),
                       texto.lower())
        texto = re.sub(" Instituto Brasileiro de Geografia Estatística ".lower(), " IBGE ".lower(), texto.lower())
        texto = re.sub(" Universidade Federal do Pampa ".lower(), " UNIPAMPA ".lower(), texto.lower())
        texto = re.sub(" Instituto Federal de Educação Ciência e Tecnologia da Bahia ".lower(), " IFBA ".lower(),
                       texto.lower())
        texto = re.sub(" Centro de Educação Superior Norte RS ".lower(), " CESNORS ".lower(), texto.lower())
        texto = re.sub(" Instituto Federal do Ceará ".lower(), " IFCE ".lower(), texto.lower())
        texto = re.sub(" Massachusetts Institute of Technology ".lower(), " MIT ".lower(), texto.lower())
        texto = re.sub(" Instituto Federal do Paraná ".lower(), " IFPR ".lower(), texto.lower())
        texto = re.sub(" Simpósio de tecnologia da Informação da Região Noroeste do RS ".lower(), " STIN ".lower(),
                       texto.lower())
        texto = re.sub(" Agência de Desenvolvimento do Médio Alto Uruguai ".lower(), " ADMAU ".lower(), texto.lower())
        texto = re.sub(" Universidade Federal Rural da Amazônia ".lower(), " UFRA ".lower(), texto.lower())
        texto = re.sub(" Universidade Federal Rural da Amazônia ".lower(), " UFRA ".lower(), texto.lower())
        texto = re.sub(" Sociedade Paranaense de Ensino e Informática ".lower(), " SPEI ".lower(), texto.lower())
        texto = re.sub(" Instituto Federal de Pernambuco ".lower(), " IFPE ".lower(), texto.lower())
        texto = re.sub(" Departamento Estadual de Informática Policial ".lower(), " DINP ".lower(), texto.lower())
        texto = re.sub(" Agência Nacional de Energia Elétrica ".lower(), " ANEEL ".lower(), texto.lower())
        texto = re.sub(" Inteligência Artificial e Tecnologia Educacional ".lower(), " IATE ".lower(), texto.lower())
        texto = re.sub(" Simpósio Brasileiro de Informática na Educação ".lower(), " SBIE ".lower(), texto.lower())
        texto = re.sub(" Universidade Federal da Fronteira Sul ".lower(), " UFFS ".lower(), texto.lower())
        texto = re.sub(" Exame Nacional do Ensino Médio ".lower(), " ENEM ".lower(), texto.lower())
        texto = re.sub(" SGBD ".lower(), " Sistema de Gerenciamento de Banco de Dados ".lower(), texto.lower())
        texto = re.sub(" CNPq ".lower(), " Conselho Nacional de Desenvolvimento Científico e Tecnológico ".lower(),
                       texto.lower())
        texto = re.sub("-se", "", texto.lower())
        texto = re.sub(" se ", "", texto.lower())
        texto = re.sub("-lo ", "", texto.lower())
        texto = re.sub("-la ", "", texto.lower())
        texto = re.sub(" lo ", "", texto.lower())
        texto = re.sub(" la ", "", texto.lower())
        return texto

    @staticmethod
    def converter_termos_2011(texto):
        texto = re.sub(" LE", " lingua estrangeira ".lower(), texto)
        texto = re.sub(" EAD", " Educação a Distância ".lower(), texto)
        texto = re.sub(" ZPD", " Zona de Desenvolvimento Proximal ".lower(), texto)
        texto = re.sub(" CCE", " Centro de Computação Eletrônica ".lower(), texto)
        texto = re.sub(" AVALWEB",
                       " Sistema interativo para gerência de questões e aplicação de avaliação na Web ".lower(), texto)
        texto = re.sub(" AVAs", " Ambientes Virtuais de Aprendizagem ".lower(), texto)
        texto = re.sub(" AVA", " Ambiente Virtual de Aprendizagem ".lower(), texto)
        texto = re.sub(" TI", " Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" SIG", " Sistemas de Informações  Geográficas ".lower(), texto)
        texto = re.sub("AIS", " Sistemas de Informações  Geográficas ".lower(), texto)
        return texto

    @staticmethod
    def converter_termos_2013(texto):
        texto = re.sub(" ECM", " Gerenciamento de Conteúdo Corporativo ".lower(), texto)
        texto = re.sub("PEA", " Processo de Ensino e de Aprendizagem ".lower(), texto)
        texto = re.sub("ACs", " autômatos celulares ".lower(), texto)
        texto = re.sub("AC", " autômato celular ".lower(), texto)
        texto = re.sub("AC", " autômato celular ".lower(), texto)
        texto = re.sub("SOFTEX", " Programas de Excelência do Software Brasileiro ".lower(), texto)
        texto = re.sub("APF", " Administração Pública Federal ".lower(), texto)
        texto = re.sub(" TCU", " Tribunal de Contas da União ".lower(), texto)
        texto = re.sub(" SIG", " Sistemas de Informações Geográficas ".lower(), texto)
        texto = re.sub(" ICTs", " Information and Communication Technologies ".lower(), texto)
        texto = re.sub(" ICT", " Information and Communication Technology ".lower(), texto)
        texto = re.sub(" BD ", " banco de dados ".lower(), texto)
        texto = re.sub(" OCR", " Identificação Óptica de Caractere ".lower(), texto)
        texto = re.sub(" TACO", " Tabela Brasileira de Composição de Alimentos ".lower(), texto)
        texto = re.sub(" TI", " Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" EAD", " Educação a Distância ".lower(), texto)
        texto = re.sub(" AR ", " Aprendizado por Reforço ".lower(), texto)
        texto = re.sub(" TIC", " Tecnologia da Informação e Comunicação ".lower(), texto)
        texto = re.sub(" RSSF ", " Redes de Sensores Sem Fio ".lower(), texto)
        texto = re.sub(" SGS ", " Sistema de Gestão de Segurança ".lower(), texto)
        texto = re.sub(" AE ", " alinhamento estratégico ".lower(), texto)
        texto = re.sub(" IA ", " Inteligência Artificial ".lower(), texto)
        texto = re.sub(" AVAs", " Ambientes Virtuais de Aprendizagem ".lower(), texto)
        texto = re.sub(" AVA", " Ambiente Virtual de Aprendizagem ".lower(), texto)
        texto = re.sub(" CAD ", " Desenho Assistido por Computador ".lower(), texto)
        texto = re.sub(" RBC ", " Raciocínio Baseado em Casos ".lower(), texto)
        texto = re.sub(" IES ", " Instituições de Ensino Superior ".lower(), texto)
        texto = re.sub(" TI", " Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" SUS ", " Sistema Único de Saúde ".lower(), texto)
        texto = re.sub(" AVAE", " ambiente virtual de aprendizagem e ensino ".lower(), texto)
        texto = re.sub("  ", "  ".lower(), texto)
        return texto

    @staticmethod
    def converter_termos_2014(texto):
        texto = re.sub(" ABD ", " Aplicação de Banco de Dados ".lower(), texto)
        texto = re.sub(" BD ", " Banco de Dados ".lower(), texto)
        texto = re.sub(" IT ", " Information Technology ".lower(), texto)
        texto = re.sub(" GQA ", " Garantia da Qualidade ".lower(), texto)
        texto = re.sub("BDT", " banco de dados de teste ".lower(), texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" SND ", " Sistema Neural para Apoio ao Diagnóstico de Diabetes ".lower(), texto)
        texto = re.sub(" AG ", " Algoritmo Genético ".lower(), texto)
        texto = re.sub(" AGs ", " Algoritmos Genéticos ".lower(), texto)
        texto = re.sub(" BI ", " Business Intelligence ".lower(), texto)
        texto = re.sub(" FEES ", " Fórum de Educação em Engenharia de Software ".lower(), texto)
        texto = re.sub(" TCC ", " Trabalho de Conclusão de Curso ".lower(), texto)
        texto = re.sub(" ITIL ", " Information  Technology Infrastructure Library ".lower(), texto)
        texto = re.sub(" BDR ", " Banco de Dados de Referência ".lower(), texto)
        texto = re.sub(" SUS ", " Sistema Único de Saúde ".lower(), texto)
        texto = re.sub(" EAD ", " Educação a Distância ".lower(), texto)
        texto = re.sub(" TM ", " Teste de Mutação ".lower(), texto)
        texto = re.sub("RNAs", " Redes Neurais Artificiais ".lower(), texto)
        texto = re.sub(" RNA ", " Rede Neurail Artificial ".lower(), texto)
        texto = re.sub(" SESAU ", " Secretaria  Estadual de Saúde ".lower(), texto)
        texto = re.sub(" BDP ", " Banco de Dados de Produção ".lower(), texto)
        texto = re.sub(" RUP ", " Rational Unified  Process ".lower(), texto)
        texto = re.sub(" AGCA ", " Algoritmos Genéticos Canônicos ".lower(), texto)
        texto = re.sub(" TM ", " Recomendação Fuzzy de Objeto de Aprendizagem ".lower(), texto)
        texto = re.sub(" OA ", " Objeto de Aprendizagem ".lower(), texto)
        texto = re.sub(" OMS ", " Organização Mundial da Saúde ".lower(), texto)
        texto = re.sub(" UI ", " interface do usuário ".lower(), texto)
        texto = re.sub(" FV ", " fotovoltaica ".lower(), texto)
        texto = re.sub(" OBAA ", " Aprendizagem Baseados em Agentes ".lower(), texto)
        texto = re.sub(" SI ", " Sistemas de Informação ".lower(), texto)
        return texto

    @staticmethod
    def converter_termos_2015(texto):
        texto = re.sub(" TIC", " tecnologias da  comunicação e informação ".lower(), texto)
        texto = re.sub(" IA", " Inteligência Artificial ".lower(), texto)
        texto = re.sub(" CAE ", " Coordenação de Assistência Estudantil ".lower(), texto)
        texto = re.sub(" CNES ", " Cadastro Nacional de Estabelecimentos de Saúde ".lower(), texto)
        texto = re.sub(" IA ", " Inteligência Artificial ".lower(), texto)
        texto = re.sub(" OMS ", " organização mundial de saúde ".lower(), texto)
        texto = re.sub(" IPS", " sistemas de prevenção de intrusão ".lower(), texto)
        texto = re.sub(" AR", " aprendizagem por reforço ".lower(), texto)
        texto = re.sub(" OA", " Objeto de Aprendizagem ".lower(), texto)
        return texto

    @staticmethod
    def converter_termos_2016(texto):
        texto = re.sub(" OA", " Objeto de Aprendizagem ".lower(), texto)
        texto = re.sub(" IA ", " Inteligência Artificial ".lower(), texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" IT ", " Information Technology ".lower(), texto)
        texto = re.sub(" IPS ", " Sistema de Prevenção de Intrusão ".lower(), texto)
        texto = re.sub(" AE", " algoritmo evolucionário ".lower(), texto)
        texto = re.sub(" GD ", " gradiente descendente ".lower(), texto)
        texto = re.sub(" AVAs ", " ambientes virtuais de aprendizagem ".lower(), texto)
        texto = re.sub(" BI ", " Business Intelligence ".lower(), texto)
        texto = re.sub(" VANTs", " Veículos Aéreos Não-Tripulados  ".lower(), texto)
        texto = re.sub(" APF", " Administração Pública Federal Brasileira ".lower(), texto)
        return texto

    @staticmethod
    def converter_termos_2017(texto):
        texto = re.sub(" VANTs", " Veículos Aéreos Não-Tripulados  ".lower(), texto)
        texto = re.sub(" BI ", " Business Intelligence ".lower(), texto)
        texto = re.sub(" IDS ", " Sistema de Detecção de Intrusão ".lower(), texto)
        texto = re.sub(" RBD ", " Diagrama de Blocos de Confiabilidade ".lower(), texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" IT ", " Information Technology ".lower(), texto)
        texto = re.sub(" IPS ", " Sistema de Prevenção de Intrusão ".lower(), texto)
        texto = re.sub(" AE", " algoritmo evolucionário ".lower(), texto)
        texto = re.sub(" GD ", " gradiente descendente ".lower(), texto)
        texto = re.sub(" AVAs ", " ambientes virtuais de aprendizagem ".lower(), texto)
        texto = re.sub(" HDFS ", " Sistema de arquivos distribuído Hadoop ".lower(), texto)
        texto = re.sub(" ACML ", " Acessibilidade Comunicativa por Meio da Libras ".lower(), texto)
        texto = re.sub(" OLAP ", " Online Analytical Processing ".lower(), texto)
        texto = re.sub(" SBC ", " Sociedade Brasileira de Computação ".lower(), texto)
        texto = re.sub(" APL ", " Arranjo Produtivo Local ".lower(), texto)
        texto = re.sub(" AIT ", " Auto de Infração de Trânsito ".lower(), texto)
        texto = re.sub(" AITs", " Auto de Infração de Trânsito ".lower(), texto)
        return texto

    @staticmethod
    def converter_termos_2018(texto):
        texto = re.sub("PAGMG", " Árvore Geradora Mínima Generalizado ".lower(), texto)
        texto = re.sub(" SIGAA ", " Sistema Integrado de Gestão  Acadêmica de Atividades ".lower(), texto)
        texto = re.sub(" IHC ", " interface humano computador ".lower(), texto)
        texto = re.sub(" UBS ", " Unidade de Beneficiamento de Sementes ".lower(), texto)
        texto = re.sub(" TSI ", " Tecnologia em Sistemas para Internet ".lower(), texto)
        texto = re.sub(" CBQ ", " Enfileiramento Baseado em Classes ".lower(), texto)
        return texto

    @staticmethod
    def converter_termos_2019(texto):
        texto = re.sub(" SBRC ", " Simpósio  Brasileiro de Redes de Computadores ".lower(), texto)
        texto = re.sub(" SIGAA ", " Sistema Integrado de Gestão  Acadêmica de Atividades ".lower(), texto)
        texto = re.sub(" EAI ", " Integração de Aplicações Empresariais ".lower(), texto)
        texto = re.sub(" AVAs ", " ambientes virtuais de aprendizagem ".lower(), texto)
        texto = re.sub(" AVA ", " Ambientes Virtuais de Aprendizagem ".lower(), texto)
        texto = re.sub(" RFID ", " Identificação por Rádio Frequência ".lower(), texto)
        texto = re.sub(" OA", " Objeto de Aprendizagem ".lower(), texto)
        texto = re.sub(" CFD ", " Dinâmica de fluídos computacional ".lower(), texto)
        texto = re.sub(" PSNR ", " Relação sinal ruído de pico ".lower(), texto)
        texto = re.sub(" PNL ", " Processamento Natural de Linguagem ".lower(), texto)
        texto = re.sub(" TI ", " Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" ANOVA ", " Análise de Variância ".lower(), texto)
        texto = re.sub(" SETI ", " Secretaria Especial de Tecnologia da Informação ".lower(), texto)
        texto = re.sub(" MVP ", " Produto Mínimo Viável ".lower(), texto)
        return texto

    @staticmethod
    def remover_textos_layout(texto):
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
        return texto.lstrip()