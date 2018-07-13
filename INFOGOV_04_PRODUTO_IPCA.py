# -*- coding: utf-8 -*-

def IPCA(data_ini, data_fim):
    #CALCULADORA IPCA BANCO CENTRAL EXPORTACAO https://dadosabertos.bcb.gov.br/organization/depec?q=ipca&sort=score+desc%2C+metadata_modified+desc
    #UTILIZO OS DADOS OBTIDOS DO SISTEMA http://www.calculador.com.br/calculo/correcao-valor-por-indice#
    #BASE OFICIAL https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

    if data_ini > data_fim:
        return -1    
    
    #ATUALIZAR SEMPRE TAMANHO DE VET
    vet=[x for x in xrange(0,228)]
    
    vet[0] = [200001 , 0.0062]
    vet[1] = [200002 , 0.0013]
    vet[2] = [200003 , 0.0022]
    vet[3] = [200004 , 0.0042]
    vet[4] = [200005 , 0.0001]
    vet[5] = [200006 , 0.0023]
    vet[6] = [200007 , 0.0161]
    vet[7] = [200008 , 0.0131]
    vet[8] = [200009 , 0.0023]
    vet[9] = [200010 , 0.0014]
    vet[10] = [200011 , 0.0032]
    vet[11] = [200012 , 0.0059]
    vet[12] = [200101 , 0.0057]
    vet[13] = [200102 , 0.0046]
    vet[14] = [200103 , 0.0038]
    vet[15] = [200104 , 0.0058]
    vet[16] = [200105 , 0.0041]
    vet[17] = [200106 , 0.0052]
    vet[18] = [200107 , 0.0133]
    vet[19] = [200108 , 0.007]
    vet[20] = [200109 , 0.0028]
    vet[21] = [200110 , 0.0083]
    vet[22] = [200111 , 0.0071]
    vet[23] = [200112 , 0.0065]
    vet[24] = [200201 , 0.0052]
    vet[25] = [200202 , 0.0036]
    vet[26] = [200203 , 0.006]
    vet[27] = [200204 , 0.008]
    vet[28] = [200205 , 0.0021]
    vet[29] = [200206 , 0.0042]
    vet[30] = [200207 , 0.0119]
    vet[31] = [200208 , 0.0065]
    vet[32] = [200209 , 0.0072]
    vet[33] = [200210 , 0.0131]
    vet[34] = [200211 , 0.0302]
    vet[35] = [200212 , 0.021]
    vet[36] = [200301 , 0.0225]
    vet[37] = [200302 , 0.0157]
    vet[38] = [200303 , 0.0123]
    vet[39] = [200304 , 0.0097]
    vet[40] = [200305 , 0.0061]
    vet[41] = [200306 , -0.0015]
    vet[42] = [200307 , 0.002]
    vet[43] = [200308 , 0.0034]
    vet[44] = [200309 , 0.0078]
    vet[45] = [200310 , 0.0029]
    vet[46] = [200311 , 0.0034]
    vet[47] = [200312 , 0.0052]
    vet[48] = [200401 , 0.0076]
    vet[49] = [200402 , 0.0061]
    vet[50] = [200403 , 0.0047]
    vet[51] = [200404 , 0.0037]
    vet[52] = [200405 , 0.0051]
    vet[53] = [200406 , 0.0071]
    vet[54] = [200407 , 0.0091]
    vet[55] = [200408 , 0.0069]
    vet[56] = [200409 , 0.0033]
    vet[57] = [200410 , 0.0044]
    vet[58] = [200411 , 0.0069]
    vet[59] = [200412 , 0.0086]
    vet[60] = [200501 , 0.0058]
    vet[61] = [200502 , 0.0059]
    vet[62] = [200503 , 0.0061]
    vet[63] = [200504 , 0.0087]
    vet[64] = [200505 , 0.0049]
    vet[65] = [200506 , -0.0002]
    vet[66] = [200507 , 0.0025]
    vet[67] = [200508 , 0.0017]
    vet[68] = [200509 , 0.0035]
    vet[69] = [200510 , 0.0075]
    vet[70] = [200511 , 0.0055]
    vet[71] = [200512 , 0.0036]
    vet[72] = [200601 , 0.0059]
    vet[73] = [200602 , 0.0041]
    vet[74] = [200603 , 0.0043]
    vet[75] = [200604 , 0.0021]
    vet[76] = [200605 , 0.001]
    vet[77] = [200606 , -0.0021]
    vet[78] = [200607 , 0.0019]
    vet[79] = [200608 , 0.0005]
    vet[80] = [200609 , 0.0021]
    vet[81] = [200610 , 0.0033]
    vet[82] = [200611 , 0.0031]
    vet[83] = [200612 , 0.0048]
    vet[84] = [200701 , 0.0044]
    vet[85] = [200702 , 0.0044]
    vet[86] = [200703 , 0.0037]
    vet[87] = [200704 , 0.0025]
    vet[88] = [200705 , 0.0028]
    vet[89] = [200706 , 0.0028]
    vet[90] = [200707 , 0.0024]
    vet[91] = [200708 , 0.0047]
    vet[92] = [200709 , 0.0018]
    vet[93] = [200710 , 0.003]
    vet[94] = [200711 , 0.0038]
    vet[95] = [200712 , 0.0074]
    vet[96] = [200801 , 0.0054]
    vet[97] = [200802 , 0.0049]
    vet[98] = [200803 , 0.0048]
    vet[99] = [200804 , 0.0055]
    vet[100] = [200805 , 0.0079]
    vet[101] = [200806 , 0.0074]
    vet[102] = [200807 , 0.0053]
    vet[103] = [200808 , 0.0028]
    vet[104] = [200809 , 0.0026]
    vet[105] = [200810 , 0.0045]
    vet[106] = [200811 , 0.0036]
    vet[107] = [200812 , 0.0028]
    vet[108] = [200901 , 0.0048]
    vet[109] = [200902 , 0.0055]
    vet[110] = [200903 , 0.002]
    vet[111] = [200904 , 0.0048]
    vet[112] = [200905 , 0.0047]
    vet[113] = [200906 , 0.0036]
    vet[114] = [200907 , 0.0024]
    vet[115] = [200908 , 0.0015]
    vet[116] = [200909 , 0.0024]
    vet[117] = [200910 , 0.0028]
    vet[118] = [200911 , 0.0041]
    vet[119] = [200912 , 0.0037]
    vet[120] = [201001 , 0.0075]
    vet[121] = [201002 , 0.0078]
    vet[122] = [201003 , 0.0052]
    vet[123] = [201004 , 0.0057]
    vet[124] = [201005 , 0.0043]
    vet[125] = [201006 , 0]
    vet[126] = [201007 , 0.0001]
    vet[127] = [201008 , 0.0004]
    vet[128] = [201009 , 0.0045]
    vet[129] = [201010 , 0.0075]
    vet[130] = [201011 , 0.0083]
    vet[131] = [201012 , 0.0063]
    vet[132] = [201101 , 0.0083]
    vet[133] = [201102 , 0.008]
    vet[134] = [201103 , 0.0079]
    vet[135] = [201104 , 0.0077]
    vet[136] = [201105 , 0.0047]
    vet[137] = [201106 , 0.0015]
    vet[138] = [201107 , 0.0016]
    vet[139] = [201108 , 0.0037]
    vet[140] = [201109 , 0.0053]
    vet[141] = [201110 , 0.0043]
    vet[142] = [201111 , 0.0052]
    vet[143] = [201112 , 0.005]
    vet[144] = [201201 , 0.0056]
    vet[145] = [201202 , 0.0045]
    vet[146] = [201203 , 0.0021]
    vet[147] = [201204 , 0.0064]
    vet[148] = [201205 , 0.0036]
    vet[149] = [201206 , 0.0008]
    vet[150] = [201207 , 0.0043]
    vet[151] = [201208 , 0.0041]
    vet[152] = [201209 , 0.0057]
    vet[153] = [201210 , 0.0059]
    vet[154] = [201211 , 0.006]
    vet[155] = [201212 , 0.0079]
    vet[156] = [201301 , 0.0086]
    vet[157] = [201302 , 0.006]
    vet[158] = [201303 , 0.0047]
    vet[159] = [201304 , 0.0055]
    vet[160] = [201305 , 0.0037]
    vet[161] = [201306 , 0.0026]
    vet[162] = [201307 , 0.0003]
    vet[163] = [201308 , 0.0024]
    vet[164] = [201309 , 0.0035]
    vet[165] = [201310 , 0.0057]
    vet[166] = [201311 , 0.0054]
    vet[167] = [201312 , 0.0092]
    vet[168] = [201401 , 0.0055]
    vet[169] = [201402 , 0.0069]
    vet[170] = [201403 , 0.0092]
    vet[171] = [201404 , 0.0067]
    vet[172] = [201405 , 0.0046]
    vet[173] = [201406 , 0.004]
    vet[174] = [201407 , 0.0001]
    vet[175] = [201408 , 0.0025]
    vet[176] = [201409 , 0.0057]
    vet[177] = [201410 , 0.0042]
    vet[178] = [201411 , 0.0051]
    vet[179] = [201412 , 0.0078]
    vet[180] = [201501 , 0.0124]
    vet[181] = [201502 , 0.0122]
    vet[182] = [201503 , 0.0132]
    vet[183] = [201504 , 0.0071]
    vet[184] = [201505 , 0.0074]
    vet[185] = [201506 , 0.0079]
    vet[186] = [201507 , 0.0062]
    vet[187] = [201508 , 0.0022]
    vet[188] = [201509 , 0.0054]
    vet[189] = [201510 , 0.0082]
    vet[190] = [201511 , 0.0101]
    vet[191] = [201512 , 0.0096]
    vet[192] = [201601 , 0.0127]
    vet[193] = [201602 , 0.009]
    vet[194] = [201603 , 0.0043]
    vet[195] = [201604 , 0.0061]
    vet[196] = [201605 , 0.0078]
    vet[197] = [201606 , 0.0035]
    vet[198] = [201607 , 0.0052]
    vet[199] = [201608 , 0.0044]
    vet[200] = [201609 , 0.0008]
    vet[201] = [201610 , 0.0026]
    vet[202] = [201611 , 0.0018]
    vet[203] = [201612 , 0.003]
    vet[204] = [201701 , 0.0038]
    vet[205] = [201702 , 0.0033]
    vet[206] = [201703 , 0.0025]
    vet[207] = [201704 , 0.0014]
    vet[208] = [201705 , 0.0031]
    vet[209] = [201706 , -0.0023]
    vet[210] = [201707 , 0.0024]
    vet[211] = [201708 , 0.0019]
    vet[212] = [201709 , 0.0016]
    vet[213] = [201710 , 0.0042]
    vet[214] = [201711 , 0.0028]
    vet[215] = [201712 , 0.0044]
    vet[216] = [201801 , 0.0029]
    vet[217] = [201802 , 0.0032]
    vet[218] = [201803 , 0.0009]
    vet[219] = [201804 , 0.0022]
    vet[220] = [201805 , 0.0040]
    vet[221] = [201806 , 0.0126]
    vet[222] = [201807 , 0]
    vet[223] = [201808 , 0]
    vet[224] = [201809 , 0]
    vet[215] = [201810 , 0]
    vet[226] = [201811 , 0]
    vet[227] = [201812 , 0]    
    

    pos_ini = 0
    pos_fim = 0

    for ipca in vet:
        if ipca[0] == data_ini:
            pos_ini = vet.index(ipca)
        if ipca[0] == data_fim:
            pos_fim = vet.index(ipca)
            break
            
    if pos_fim == 0:
        return -1
        
    fator = 1    
    for i in xrange(pos_ini,pos_fim+1):
        fator = fator*(1+vet[i][1])

    return fator
    
def Atualiza_INFOGOV(data_fim):
    vet_mes = ['03','06','09','12']
    vet_ano = []
    for i in xrange(2000,2019):
        for mes in vet_mes:
            vet_ano.append(str(i)+mes)

    for mes in vet_ano:
        if int(mes) <= int(data_fim):   
            fator = IPCA(int(mes), int(data_fim))
            print mes, data_fim, str(fator)