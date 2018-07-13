# -*- coding: utf-8 -*-
# http://dados.gov.br/
# https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries
# NOTA IMPORTANTE NA LINHA 314

import sys, time, re, shelve
from INFOGOV_04_PRODUTO_IPCA import *
from unicodedata import normalize

#1 - base original; 2 - ANO_MES na forma 2000XX
baseVINCULOS = open(sys.argv[1],'r')
ANO_MES = sys.argv[2]
basePESSOAS = open('INFOGOV_BASE_PESSOA_'+ANO_MES+'.txt','w',0)
baseCPF = shelve.open('INFOGOV_03_CPF_ANONIMO.db')

dict_ESC = {}
dict_JOR = {}
dict_UF = {}
dict_ORG = {}
vet_comi = []
vet_func = []
vet_tran = []
vet_ced = []
vet_req = []
vet_FPE = []

def INIC_SIAPE():
    global dict_ESC, dict_JOR, dict_UF, dict_ORG, vet_func, vet_ced, vet_req, vet_comi, vet_tran, vet_FPE
    
    dict_ESC['MESTRADO'] = 'MESTRADO'
    dict_ESC['LICENCIATURA(T)'] = 'SUPERIOR'
    dict_ESC['MESTRADO(T)'] = 'MESTRADO'
    dict_ESC['ENSINO_FUNDAMENTAL(T)'] = 'FUNDAMENTAL'
    dict_ESC['LICENCIATURA_PLENA(T)'] = 'SUPERIOR'
    dict_ESC['GRAD_O+RSC-I(LEI12772/12(T)'] = 'SUPERIOR'
    dict_ESC['ANALFABETO'] = 'FUNDAMENTAL'
    dict_ESC['DOUTORADO'] = 'DOUTORADO'
    dict_ESC['SUP_COMPL_OU_HAB_LEGAL_EQV'] = 'SUPERIOR'
    dict_ESC['BACHAREL(T)'] = 'SUPERIOR'
    dict_ESC['APERFEICOAMENTO_NIV_MED(T)'] = 'ENSINO MÉDIO'
    dict_ESC['AUXILIAR_DE_ENFERMAGEM(T)'] = 'ENSINO MÉDIO'
    dict_ESC['2O_GR_INCOMPLETO'] = 'FUNDAMENTAL'
    dict_ESC['POS-GRAD_O+RSC-II_L12772/12'] = 'POS GRADUACAO'
    dict_ESC['CURSO_QUAL_PROF_MIN_360H(T)'] = 'SUPERIOR'
    dict_ESC['ALFABETIZ_S/_CURSOS_REGUL'] = 'FUNDAMENTAL'
    dict_ESC['DOUTORADO(T)'] = 'DOUTORADO'
    dict_ESC['APERFEICOAMENTO_NIV_SUP(T)'] = 'SUPERIOR'
    dict_ESC['CURSO_QUAL_PROF_MIN_180H(T)'] = 'SUPERIOR'
    dict_ESC['1O_GR_INC_-_4A_SERIE_COMPL'] = 'FUNDAMENTAL'
    dict_ESC['POS-GRADUACAO(T)'] = 'POS GRADUACAO'
    dict_ESC['2O_GR_COMPL_OU_TEC_PROFISS'] = 'ENSINO MÉDIO'
    dict_ESC['1O_GR_INC_-_5A_A_8A_SER_INC'] = 'FUNDAMENTAL'
    dict_ESC['CURSO_CAP/QUAL_P_MIN180H(T)'] = 'SUPERIOR'
    dict_ESC['ESPECIALIZACAO_NIV_MED(T)'] = 'ENSINO MÉDIO'
    dict_ESC['POS-DOUTORADO(T)'] = 'DOUTORADO'
    dict_ESC['POS-DOUTORADO'] = 'DOUTORADO'
    dict_ESC['1O_GR_INC_-_1A_A_4A_SER_INC'] = 'FUNDAMENTAL'
    dict_ESC['TECNICO_NIV_MED_COMPLETO(T)'] = 'ENSINO MÉDIO'
    dict_ESC['SUPERIOR_INCOMPLETO'] = 'ENSINO MÉDIO'
    dict_ESC['1O_GR_COMPL_-_8A_SER_COMPL'] = 'FUNDAMENTAL'
    dict_ESC['ESPECIALIZACAO_NIV_SUP(T)'] = 'POS GRADUACAO'
    dict_ESC['NIVEL_MÉDIO(T)'] = 'ENSINO MÉDIO'
    dict_ESC['ESPECIALIZACAO_-_NA(T)'] = 'ENSINO MÉDIO'
    dict_ESC['MESTRE+RSC-III_LEI_12772/12'] = 'DOUTORADO'
    dict_ESC['GRADUACAO_NIV_SUP_COMPLE(T)'] = 'SUPERIOR'
    dict_ESC['CURSO_QUAL_PROF_MIN_250H(T)'] = 'SUPERIOR'
    dict_ESC['ESPECIALIZACAO'] = 'POS GRADUACAO'
    dict_ESC['CURSOS_EQUIP-GQ-360HORAS(T)'] = 'SUPERIOR'
    dict_ESC['APERFEICOAMENTO_-_NA(T)'] = 'SUPERIOR'
    dict_ESC['CURSOS_EQUIP-GQ-360HORAS(T)'] = 'SUPERIOR'
    dict_ESC['LIVRE_DOCENCIA'] = 'SUPERIOR'
    dict_ESC['APERFEICOAMENTO'] = 'SUPERIOR'
    dict_ESC['APERFEICOAMENTO_(RMI)_(T)'] = 'SUPERIOR'
    dict_ESC['FORMACAO_(RMI)_(T)'] = 'SUPERIOR'
    dict_ESC['NIVEL_MÉDIO'] = 'ENSINO MÉDIO'
    dict_ESC['NIVEL_MÉDIO(T)'] = 'ENSINO MÉDIO'
    dict_ESC['NIVEL_M\xc3\xa9DIO(T)'] = 'ENSINO MÉDIO'
    dict_ESC[''] = 'SEM_INFO'    

    dict_JOR['12 h sem'] = '12'
    dict_JOR['18 h sem'] = '18'
    dict_JOR['20 h sem'] = '20'
    dict_JOR['22 h sem'] = '22'
    dict_JOR['24 h sem'] = '24'
    dict_JOR['25 h sem'] = '25'
    dict_JOR['30 h sem'] = '30'
    dict_JOR['32,5 h sem'] = '32.5'
    dict_JOR['36 h sem'] = '36'
    dict_JOR['40 h sem'] = '40'
    dict_JOR['44 h sem'] = '44'
    dict_JOR['60 h sem'] = '60'
    dict_JOR['66 h sem'] = '66'
    dict_JOR['Dedc exclus'] = '99'
    dict_JOR[''] = '00'
    
    dict_UF['Acre'] = 'AC'
    dict_UF['Alagoas'] = 'AL'
    dict_UF['Amapá'] = 'AP'
    dict_UF['Amazonas'] = 'AM'
    dict_UF['Bahia'] = 'BA'
    dict_UF['Ceará'] = 'CE'
    dict_UF['Distrito Federal'] = 'DF'
    dict_UF['Espírito Santo'] = 'ES'
    dict_UF['Goiás'] = 'GO'
    dict_UF['Maranhão'] = 'MA'
    dict_UF['Mato Grosso'] = 'MT'
    dict_UF['Mato Grosso do Sul'] = 'MS'
    dict_UF['Minas Gerais'] = 'MG'
    dict_UF['Pará'] = 'PA'
    dict_UF['Paraíba'] = 'PB'
    dict_UF['Paraná'] = 'PR'
    dict_UF['Pernambuco'] = 'PE'
    dict_UF['Piauí'] = 'PI'
    dict_UF['Rio de Janeiro'] = 'RJ'
    dict_UF['Rio Grande do Norte'] = 'RN'
    dict_UF['Rio Grande do Sul'] = 'RS'
    dict_UF['Rondônia'] = 'RO'
    dict_UF['Roraima'] = 'RR'
    dict_UF['Santa Catarina'] = 'SC'
    dict_UF['São Paulo'] = 'SP'
    dict_UF['Sergipe'] = 'SE'
    dict_UF['Tocantins'] = 'TO'
    dict_UF[''] = 'XX'
    
    baseSIORG = open('INFOGOV_02_BASE_SIORG.txt','r')
    temp = baseSIORG.readline()
    for line in baseSIORG:
        campos = line.replace('\n','').split('\t')
        dict_ORG[campos[0]] = (campos[1],campos[2],campos[3])
    baseSIORG.close()
    
    #FUNCOES QUE LIGAM A FLAG DUMMY_DAS
    vet_func = ['DAS', 'NES', 'FPE', 'FCI', 'FCD', 'FPR', 'FDI', 'FCT', 'FG', 'FGE', 'FGR', 'FIN', 'FND']
    vet_FPE = ['FCI', 'FDI', 'FCD', 'FPR', 'FPE']
    #FUNCOES QUE LIGAM O PAR CEDIDO/REQUISITADO
    vet_ced = ['CEDIDO ART93 8112', 'CEDIDO', 'CEDIDO SUS/LEI 8270', 'CLT ANS JUD. CEDIDO']
    vet_req = ['REQ. MILITAR', 'REQ.DE OUTROS ORGAOS', 'REQUISITADO', 'ATIVO PERMANENTE', 'REQUISITADO MILITAR', 'CLT ANS -DEC 6657/08','CLT ANS DEC JUDICIAL',]
    #FUNÇÕES QUE INDICAM QUE A PESSOA É COMISSIONADA
    vet_comi = ['NOM.COMIS.CARG. 8112/90,A.9,II','NOMEACAO P/CARGO EM COMISSAO']
    #CARREIRAS TRANSVERSAIS
    vet_tran = ['ANALISTA DE COMERCIO EXTERIOR', 'ANALISTA DE PLANEJAMENTO E ORC', 'TECNICO DE PLANEJAMENTO', 'TECNICO DE PLANEJAMENTO E ORCA', 'TECNICO DE PLANEJAMENTO E PESQ', 'ESP POL PUBL GESTAO GOVERNAMEN', 'ANALISTA DE FINANCAS E CONTROL', 'TECNICO DE FINANCAS E CONTROLE', 'AUDITOR FEDERAL DE FINANCAS E']    

def NORM(nome):
    nome=nome.lower()
    nome=normalize('NFKD', nome.decode('utf-8')).encode('ASCII','ignore')
    nome=re.sub('ã|Ã|â|Â|á|Á|à|À','A',nome)
    nome=re.sub('ê|Ê|é|É|è|È','E',nome)
    nome=re.sub('î|Î|í|Í|ì|Ì|ï|Ï','I',nome)
    nome=re.sub('õ|Õ|ô|Ô|ó|Ó|ò|Ò','O',nome)
    nome=re.sub('û|Û|ú|Ú|ù|Ù|ü|Ü','U',nome)
    nome=re.sub('ç|Ç','C',nome)
    nome=re.sub('ñ|Ñ','N',nome)
    nome=re.sub("'",' ',nome)
    nome=nome.upper()
    return str(nome)
    
def SIAPE_PESSOA(bloco):
    vinculos=[]
    campos=[]
    vinc_req = -1 #posicao do vinculo requisitado
    vinc_ced = -1 #posicao do vinculo cedido
    vinc_qtd = str(len(bloco)) #qtd vinculos no cpf
    flag_abono = 0 #flag se a pessoa esta abonada
    flag_infogov = '0' #flag se a pessoa teve vinculos unificados
    
    for line in bloco:
        campos = line.replace('\r\n','').split('\t')
        
        #LOCAL PARA RECODIFICAR VARIÁVEIS
        for campo in cab:
            if campos[cab.index(campo)][:2] == 'S/':
                campos[cab.index(campo)] = ''
        
        if campos[cab.index('ÓRGÃO SUPERIOR')][0:4] == 'IFET' : campos[cab.index('ÓRGÃO SUPERIOR')] = 'MEC'            
        if campos[cab.index('ÓRGÃO SUPERIOR')][0:2] == 'C.' : campos[cab.index('ÓRGÃO SUPERIOR')] = 'MD'
        if campos[cab.index('ÓRGÃO SUPERIOR')] == 'ANCINE' : campos[cab.index('ÓRGÃO SUPERIOR')] = 'MINC'
        if campos[cab.index('ÓRGÃO SUPERIOR')] == 'SAE' : campos[cab.index('ÓRGÃO SUPERIOR')] = 'PR'
        if campos[cab.index('ÓRGÃO SUPERIOR')] == 'E/M/EMPRES' : campos[cab.index('ÓRGÃO SUPERIOR')] = 'CEDIDO'        
        if campos[cab.index('ÓRGÃO SUP DESTINO')] == 'ANCINE' : campos[cab.index('ÓRGÃO SUP DESTINO')] = 'MINC'
        if campos[cab.index('ÓRGÃO SUP DESTINO')] == 'SAE' : campos[cab.index('ÓRGÃO SUP DESTINO')] = 'PR'
        if campos[cab.index('ÓRGÃO SUP DESTINO')] == 'E/M/EMPRES' : campos[cab.index('ÓRGÃO SUP DESTINO')] = 'CEDIDO'
        if campos[cab.index('ANO PREVISÃO APOSENTADORIA')] == 'ABONO' : flag_abono = 1
        if campos[cab.index('SITUAÇÃO VÍNCULO')] == 'EXERC.÷7º ART93 8112' : campos[cab.index('SITUAÇÃO VÍNCULO')] = 'CEDIDO ART93 8112'        

        campos[cab.index('UF RESID')] = dict_UF[campos[cab.index('UF RESID')]]
        campos[cab.index('JORNADA CARGO')] = dict_JOR[campos[cab.index('JORNADA CARGO')]]
        campos[cab.index('JORNADA TRABALHO')] = dict_JOR[campos[cab.index('JORNADA TRABALHO')]]    
        campos[cab.index('ESCOLARIDADE')] = dict_ESC[campos[cab.index('ESCOLARIDADE')].replace(' ','_').upper()]
        campos[cab.index('REMUN')] = campos[cab.index('REMUN')].replace('.','').replace(',','.')
        campos[cab.index('RENDIM')] = campos[cab.index('RENDIM')].replace('.','').replace(',','.')
        campos[cab.index('DESCONTO')] = campos[cab.index('DESCONTO')].replace('.','').replace(',','.')            
        #FIM LOCAL PARA RECODIFICAR VARIÁVEIS
        
        vinculos.append(campos)
        
        if campos[cab.index('SITUAÇÃO VÍNCULO')] in vet_ced:
            vinc_ced = len(vinculos) - 1
        if campos[cab.index('SITUAÇÃO VÍNCULO')] in vet_req:
            vinc_req = len(vinculos) - 1
                
        if campos[cab.index('FUNÇÃO')] == '':
            campos[cab.index('FUNÇÃO')] = campos[cab.index('FUNÇÃO DESTINO')]
        if campos[cab.index('NÍVEL FUNÇÃO')] == '':
            campos[cab.index('NÍVEL FUNÇÃO')] = campos[cab.index('NÍVEL FUNÇÃO DESTINO')]
        
    #INICIO REGRAS DE UNIFICAÇÃO DE REGISTROS
    if (vinc_ced != -1) and (vinc_req != -1):
        vinc_unificado = vinculos[vinc_req]
        flag_infogov = '1'
        if flag_abono == 1:
            vinc_unificado[cab.index('ANO PREVISÃO APOSENTADORIA')] = 'ABONO'
            
        vinc_unificado[cab.index('ANO MES OPÇÃO FUNPRESP')] = vinculos[vinc_ced][cab.index('ANO MES OPÇÃO FUNPRESP')]
        vinc_unificado[cab.index('TEMPO SERV APOS')] = vinculos[vinc_ced][cab.index('TEMPO SERV APOS')]
        vinc_unificado[cab.index('INGRESSO')] = vinculos[vinc_ced][cab.index('INGRESSO')]
        vinc_unificado[cab.index('CARGO')] = vinculos[vinc_ced][cab.index('CARGO')]
        vinc_unificado[cab.index('COD CARGO')] = vinculos[vinc_ced][cab.index('COD CARGO')]
        vinc_unificado[cab.index('ESC CARGO')] = vinculos[vinc_ced][cab.index('ESC CARGO')]
        vinc_unificado[cab.index('NÍVEL CARGO')] = vinculos[vinc_ced][cab.index('NÍVEL CARGO')]
        vinc_unificado[cab.index('GRUPO CARGO')] = vinculos[vinc_ced][cab.index('GRUPO CARGO')]
        vinc_unificado[cab.index('DATA INGRESSO CARGO')] = vinculos[vinc_ced][cab.index('DATA INGRESSO CARGO')]
                
        vinc_unificado[cab.index('REMUN')] = str(float(vinculos[vinc_req][cab.index('REMUN')]) + float(vinculos[vinc_ced][cab.index('REMUN')]))
        vinc_unificado[cab.index('RENDIM')] = str(float(vinculos[vinc_req][cab.index('RENDIM')]) + float(vinculos[vinc_ced][cab.index('RENDIM')]))
        vinc_unificado[cab.index('DESCONTO')] = str(float(vinculos[vinc_req][cab.index('DESCONTO')]) + float(vinculos[vinc_ced][cab.index('DESCONTO')]))
        
        vinculos.append(vinc_unificado)
        
        temp1 = vinculos[vinc_ced]
        temp2 = vinculos[vinc_req]
        vinculos.remove(temp1)
        vinculos.remove(temp2)
    #FIM REGRAS DE UNIFICAÇÃO DE REGISTROS
    
    for vinc in vinculos:
    
        if len(vinculos) == 1: 
            if (vinc[cab.index('CARGO')] in vet_tran) and (vinc[cab.index('ÓRGÃO DESTINO')] != ''):
                #EXECUTE TRANSFORMACAO DE CARGO E CARGO SUP AQUI
                vinc[cab.index('ÓRGÃO')] = vinc[cab.index('ÓRGÃO DESTINO')]
                vinc[cab.index('ÓRGÃO SUPERIOR')] = vinc[cab.index('ÓRGÃO SUP DESTINO')]
        
        vinc[cab.index('MÊS')] = ANO_MES
        REMUN_IPCA = str(round(float(vinc[cab.index('REMUN')])*IPCA_fator,3))
        if vinc[cab.index('CPF SERVIDOR')] in baseCPF:
            CPF_ANON = baseCPF[vinc[cab.index('CPF SERVIDOR')]]
        else:
            id_anon = str(len(baseCPF)).zfill(11)
            baseCPF[vinc[cab.index('CPF SERVIDOR')]] = id_anon
            CPF_ANON = id_anon
        
        NOVO_COD = dict_ORG[vinc[cab.index('ÓRGÃO')].strip()][0]
        NOVO_ORG = dict_ORG[vinc[cab.index('ÓRGÃO')].strip()][1]
        NOVO_NATJUR = dict_ORG[vinc[cab.index('ÓRGÃO')].strip()][2]
        vinc.extend([REMUN_IPCA,NOVO_ORG,NOVO_COD,NOVO_NATJUR])
        
        '''
        FLAG FUNCAO:
        0 - SEM FUNCAO / FUNÇÃO DESCONSIDERADA
        1 - DAS/FPE 
        2 - OUTRAS FUNC DE IMPORTANCIA
        '''
        flag_func = '0'
        if vinc[cab.index('FUNÇÃO')] in vet_func:
            if vinc[cab.index('FUNÇÃO')] == 'DAS' or vinc[cab.index('FUNÇÃO')] in vet_FPE:
                flag_func = '1'
            else:
                flag_func = '2'
        '''
        FLAG COMISSIONADO:
        0 - COM VINCULO
        1 - SEM VINCULO
        '''
        flag_comis = '0'
        if vinc[cab.index('INGRESSO')].upper() in vet_comi and vinc[cab.index('CARGO')] == '':
            flag_comis = '1'
    
        vinc.insert(01,CPF_ANON)
        vinc.insert(17,str(vinc_qtd))
        vinc.insert(18,flag_infogov)              
        vinc.insert(53,flag_func)
        vinc.insert(54,flag_comis)
  
        basePESSOAS.write('\t'.join(NORM(c) for c in vinc)+'\n')
        
print "INICIO",time.ctime()
cab = baseVINCULOS.readline().replace('\r\n','').split('\t')

if cab[12] == '':
    cab[12] = 'NOME DEFICIENCIA'
else:
    print 'PROBLEMA COM VAR[12] NOME DEFICIENCIA'
    exit()
    
cab_cp = [] #HARD COPY NO CAB_CP POR QUE CAB_CP = CAB CRIA UM LINK SIMBÓLICO
for x in cab:
    if x == 'DIA NOMEAÇÃO': 
        x = 'DIA NOMEAÇÃO FUNÇÃO'
    cab_cp.append(NORM(x))

cab_cp.insert(01,'ID_ANON')
cab_cp.insert(17,'QTD VINCULOS')
cab_cp.insert(18,'VINCULO INFOGOV')
cab_cp.insert(53,'FLAG FUNCAO')    
cab_cp.insert(54,'FLAG COMISSIONADO')    
cab_cp.extend(['REMUN IPCA','ORG SIORG','COD SIORG NOVO','NATJUR SIORG'])
basePESSOAS.write('\t'.join(str(c) for c in cab_cp)+'\n')
    
INIC_SIAPE()
#ATUALIZAR SEMPRE COM O VALOR ANOMES DA BASE MAIS RECENTE NO CONJUNTO
IPCA_fator = IPCA(int(ANO_MES),201803)
len_baseCPF = 0

#NÚCLEO DO PROCESSO DE ANALISE DE BLOCO, NÃO MEXER EM HIPÓTESE NENHUMA
bloco = []
pes_atual=''
pes_tmp=''
inicio = True

for id,line in enumerate(baseVINCULOS):
    campos = []
    campos = (line.replace('"','').replace('\r\n','')).split('\t')
    pes_atual = campos[cab.index('CPF SERVIDOR')]
    
    #PRIMEIRA LINHA DO BLOCO
    if ((pes_atual == pes_tmp) or (inicio == True)):
        bloco.append(line)
    else:
        #SE A LINHA FOR DIFERENTE
        SIAPE_PESSOA(bloco)
        bloco = []
        bloco.append(line)
        pes_tmp = pes_atual
     
    while True:
        try:
            tmp = str(baseVINCULOS.next())
        except StopIteration:
            break

        campos = tmp.split('\t')
        if (campos[cab.index('CPF SERVIDOR')] == pes_atual):
            bloco.append(tmp)
        else:
            SIAPE_PESSOA(bloco)
            bloco = []
            bloco.append(tmp)
            pes_tmp = campos[cab.index('CPF SERVIDOR')]
            inicio = False
            break
            
if (len(bloco) != 0):
    SIAPE_PESSOA(bloco)
#FIM DO NÚCLEO
    
baseVINCULOS.close()
basePESSOAS.close()
baseCPF.close()

print "FIM", time.ctime()
