# -*- coding: utf-8 -*-
import time, sys

def hist():
    #eixo_y = ['MAS','FEM']
    #eixo_y = ['DAS-1','DAS-2','DAS-3','DAS-4','DAS-5','DAS-6','FPE-1011','FPE-1012','FPE-1013','FPE-1014','FPE-1021','FPE-1022','FPE-1023','FPE-1024']
    #eixo_y = ['DAS-1','DAS-2','DAS-3','DAS-4','DAS-5','DAS-6']
    #eixo_y = ['ATE_FUNDAMENTAL', 'FUNDAMENTAL', 'ENSINO_MEDIO', 'SUPERIOR', 'POS_GRAD', 'MESTRADO', 'DOUTORADO','SEM_INFO']        
    #eixo_z = ['DAS-1','DAS-2','DAS-3','DAS-4','DAS-5','DAS-6','FPE-1011','FPE-1012','FPE-1013','FPE-1014','FPE-1021','FPE-1022','FPE-1023','FPE-1024']
    #eixo_z = ['ATE_FUNDAMENTAL', 'FUNDAMENTAL', 'ENSINO_MEDIO', 'SUPERIOR', 'POS_GRAD', 'MESTRADO', 'DOUTORADO']
    #eixo_z = ['CGU','GDF','MAPA','MCID','MCTI','MD','MDH','MDIC','MDSA','ME','MEC','MF','MIN','MINC','MJ','MMA','MME','MP','MRE','MS','MT','MTB','MTUR','PR']
    #eixo_x = ['AMARELA', 'BRANCA', 'INDIGENA', 'NEGRA']
    None

dict_cubo = {}
eixo_x = []
eixo_y = []
eixo_z = []
for i in xrange(2000,2019):
    eixo_z.append(str(i))

for ano in eixo_z:
    dict_cubo[ano] = {}
    for esc in eixo_y:
        dict_cubo[ano][esc] = {}
        for raca in eixo_x:
            dict_cubo[ano][esc][raca] = 0

print 'CONTANDO...', time.ctime()            
baseINFO = open(sys.argv[1],'r')
cab = baseINFO.readline().replace('\n','').split('\t')

for id,line in enumerate(baseINFO):
    line = line.replace('\n','').split('\t')
    if line[cab.index('GRUPO SITUAÇÃO VÍNCULO')] == 'ATIVO':
    
        #AREA DE FILTROS, FAVOR ANOTAR A PORRA DO FILTRO INSERIDO E SALVAR O SCRIPT COM NOME DIFERENTE, PREFERENCIALMENTE COM DATA
    
            if line[cab.index('COR ORIGEM ETNICA')] == 'PARDA' or line[cab.index('COR ORIGEM ETNICA')] == 'PRETA':
                line[cab.index('COR ORIGEM ETNICA')] = 'NEGRA'
            
            x = line[cab.index('')]
            y = line[cab.index('')]
            z = line[cab.index('MÊS')][:4]
            
            try:
                dict_cubo[z][y][x] += 1
            except:
                print 'z:',z,'y:',y,'x:',x
                exit()
            
    if id%1000000 == 0:
        print str(id)
baseINFO.close()

with open('result_'+str(time.ctime()).replace(':','.')+'.txt','w',0) as resultado:
    for z in eixo_z:
        for y in eixo_y:
            for x in eixo_x:
                 resultado.write(z+';'+y+';'+x+';'+str(dict_cubo[z][y][x])+'\n')
    resultado.close()                 

print 'FIM.', time.ctime()