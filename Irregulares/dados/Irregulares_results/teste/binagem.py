import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.time import Time
from multiprocessing import Pool

################## Definicao de Parametros  #################################################



arquivo = 'photometry.dat'			### arquivo de dados de entrada
binagem = [1, 3, 5, 15]				### lista de binagens a plotar
coltime = [2]                                   ### coluna do tempo
coltarg = [4, 7, 10, 13, 16]                    ### colunas das estrelas alvo
targcom = ['6px', '8px', '10px', '12px', '14px']			### nomes das colunas da estrela alvo - plot issue
calib = 'No'					### caso haja estrela de calibracao => calib = 'Yes'
colcalb = [19]					### coluna da estrela de calibracao
calbcom = ['Calib-10px']			### abertura da estrela de calibracao - plot issue
proc = 4					### numero maximo de processos paralelos
#  #  #  ### plot config ###  #  #  #
nomelocal = 'JBrooks'				### Nome do sitio de observacao
timelimuser = 'No'				### usar limites do eixo x fornecido pelo usuario => Yes ou No
timeminlim = -5					### tempo minimo do plot; segundos a partir do tempo inicial
timemaxlim = 100				### tempo maximo do plot; segundos a partir do tempo inicial
datainicio = '2013-10-25 09:40:00'		### data de referencia de contagem para o plot
fluxlimuser = 'Yes'				### usar limites de fluxo do usuario => Yes ou No
fluxminlim = 100000				### fluxo minimo do plot
fluxmaxlim = 900000				### fluxo maximo do plot
fluxlimcalib = 'No'				### usar limites de fluxo do usuario => Yes ou No
fluxmincalib = 0				### fluxo minimo do plot
fluxmaxcalib = 10000				### fluxo maximo do plot
fluxlimrelat = 'No'				### usar limites de fluxo do usuario => Yes ou No
fluxminrelat = 0.5				### fluxo minimo do plot
fluxmaxrelat = 1.5				### fluxo maximo do plot



#############################################################################################

colunas = np.hstack((coltime, coltarg))
coments = ['Time (jd)']
coments = np.hstack((coments, targcom))
if calib == 'Yes':
    colunas = np.hstack((colunas, colcalb))
    coments = np.hstack((coments, calbcom))
x = np.loadtxt(arquivo, usecols=(colunas), unpack=True)
t = Time(datainicio, format='iso', scale='utc')
te = t.iso.split(' ')
data = te[0]
inicio = te[1]

###################### Funcoes ########################################################


###### ve a mediana de um array ####
def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

#### faz a binagem ####
def bina(array, tam, binagem):
    return (sum(array[tam + i] for i in np.arange(binagem))) / binagem

#### salva figura ####
def salvafigura(array, coment, binagem, tempo, labely, ylimuser, yminlim, ymaxlim):
    axes=plt.gca()
    plt.title('{}, Data: {data}; {coment} ; binagem = {binagem} pts'.format(nomelocal, data=data, coment=coment, binagem=binagem))
    plt.ylabel(labely)
    plt.xlabel('Tempo a partir de {inicio} (s)'.format(inicio=inicio))
    if timelimuser == 'Yes':
        axes.set_xlim([timeminlim,timemaxlim])
    if ylimuser == 'Yes':
        axes.set_ylim([yminlim,ymaxlim])
    plt.plot(tempo, array)
    plt.savefig('{}_{coment}_bin{binagem}.png'.format(nomelocal, coment=coment, binagem=binagem))
    plt.clf()


############################ Corpo principal #######################################################

#def plotar(binagem, tam):
def callfunc(binagem):
    global coments
    elim = binagem - 1
    tam = np.arange(x[0].size - elim)

####  target  ##################

    saida = np.vstack((bina(i, tam, binagem)  for i in x))
    tempo = (saida[0] - t.jd)*86400

### Calibracao   ###############

    if calib == 'Yes':
        h = x[len(coltime):len(coltime) + len(coltarg)] / x[len(coltime) + len(coltarg)]
        relat = np.vstack((bina(i, tam, binagem)  for i in h))
        relatm = np.vstack((i / median(i) for i in relat))
        for k in np.arange(len(relatm)):
            texto = 'Relat_flux_{text}'.format(text=targcom[k])
            coments = np.hstack((coments,texto))
        saida = np.vstack((saida, relatm))

### Plots ##########################

    for k in np.arange(len(coltime), len(coltime) + len(coltarg)):
        salvafigura(saida[k], coments[k], binagem, tempo, 'Flux', fluxlimuser, fluxminlim, fluxmaxlim) 

    if calib == 'Yes':
        for k in np.arange(len(coltime) + len(coltarg), len(coltime) + len(coltarg) + len(colcalb)):
            salvafigura(saida[k], coments[k], binagem, tempo, 'Flux', fluxlimcalib, fluxmincalib, fluxmaxcalib) 
        for k in np.arange(len(coltime) + len(coltarg) + len(colcalb), len(saida)):
            salvafigura(saida[k], coments[k], binagem, tempo, 'Relative Flux', fluxlimrelat, fluxminrelat, fluxmaxrelat) 

### Save file  ###################

    strs = ["%16.8f"]
    b = ["%13.5f" for k in range(len(saida) - 1)]
    for j in b:
        strs.append(j)
    np.savetxt('photometry_{}_bin{binagem}.dat'.format(nomelocal, binagem=binagem), np.c_[saida.T], fmt=strs)

    f1=open('./photometry_{}_bin{binagem}.label'.format(nomelocal, binagem=binagem), 'w+')
    for k in np.arange(len(coments)):
        print >>f1, 'Coluna {i} = {texto}'.format(i=k+1,texto=coments[k])

#############################################################################################
######################   CHAMADA DA FUNCAO DIVIDO POR PROCESSOS   ###########################
#############################################################################################

pool = Pool(processes=proc)
pool.map(callfunc, binagem)


