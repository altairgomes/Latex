import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time, TimeDelta
import os

######################################################################3

plt.rcParams['text.latex.preamble']=[r"\usepackage{txfonts}"]

params = {'text.usetex' : True,
          'font.size' : 22,
          'font.family' : 'txfonts',
          'text.latex.unicode': True,
          }
          
plt.rcParams.update(params)

obj = ['Ananke','Carme','Elara','Himalia','Leda','Lysithea','Nereid','Pasiphae','Phoebe','Sinope']
nobj= [512, 511, 507, 506, 513, 510, 802, 508, 609, 509]
pee = ['160-1', '160-total', '160-total', '160-total', '160-total', '160-1', '160-total', '160-total', '160-total', '160-total']
iage = ['IAG_total', 'IAG1', 'IAG_total', 'IAG_total', 'IAG_total', 'IAG1', 'IAG_total', 'IAG1', 'IAG_total', 'IAG1']
zeie = ['ZEI1', 'ZEI1', 'ZEI1', 'ZEI_total', 'ZEI1', 'ZEI1', 'ZEI1', 'ZEI1', 'ZEI1', 'ZEI1']
locald = [2, 3, 1, 1, 1, 1, 1, 2, 1, 1]
localr = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

sizel = 18
sizek = 14

def julian(idx):
    f = open('julian_date_{}'.format(obj[idx]), 'w')
    datas = []
    if os.path.isfile(arq160) == True:
        datas = np.hstack((datas, dado160[4]))
    if os.path.isfile(arqiag) == True:
        datas = np.hstack((datas, dadoiag[4]))
    if os.path.isfile(arqzei) == True:
        datas = np.hstack((datas, dadozei[4]))
    if os.path.isfile(arqohp) == True:
        datas = np.hstack((datas, dadoohp[4]))
    if os.path.isfile(arqeso) == True:
        datas = np.hstack((datas, dadoeso[4]))
    for i in datas:
        f.write('{:.10f} JD\n'.format(i))
    f.close()
    g = open('entry_naif_{}'.format(obj[idx]), 'w')
    g.write('874\n')
    g.write('{}\n'.format(nobj[idx]))
    g.write('de421\n')
    g.write('/home/altair/Documentos/Irregulares/dados/Irregulares_results/julian_date_{}'.format(obj[idx]))
    g.close()
    h = open('rodanaif.sh', 'w')
    h.write('cd /homeA/NAIF64/toolkit/work/\n')
    h.write('./ephem_hv5 < /home/altair/Documentos/Irregulares/dados/Irregulares_results/entry_naif_{} > /home/altair/Documentos/Irregulares/dados/Irregulares_results/{}_ephem.dat\n'.format(obj[idx], obj[idx]))
    h.write('cd /home/altair/Documentos/Irregulares/dados/Irregulares_results/\n')
    h.close()
    os.system('bash rodanaif.sh')

def getav(idx):
    ephemer = np.loadtxt(arqeph, skiprows=3, usecols=(2, 37), unpack=True)
    ephemav = Time(ephemer[0], format='jd', scale= 'utc')
    av160, aviag, avzei, avohp, aveso = [], [], [], [], []
    delt = TimeDelta(1, format='sec')
    if os.path.isfile(arq160) == True:
        for idx, value in enumerate(dado160[4]):
            a = Time(value, format='jd', scale='utc')
            k = [j for (i,j) in zip(ephemav,ephemer[1]) if np.absolute(i - a) <= delt]
            av160.append(k[0])
    if os.path.isfile(arqiag) == True:
        for idx, value in enumerate(dadoiag[4]):
            a = Time(value, format='jd', scale='utc')
            k = [j for (i,j) in zip(ephemav,ephemer[1]) if np.absolute(i - a) <= delt ]
            aviag.append(k[0])
    if os.path.isfile(arqzei) == True:
        for idx, value in enumerate(dadozei[4]):
            a = Time(value, format='jd', scale='utc')
            k = [j for (i,j) in zip(ephemav,ephemer[1]) if np.absolute(i - a) <= delt ]
            avzei.append(k[0])
    if os.path.isfile(arqohp) == True:
        for idx, value in enumerate(dadoohp[4]):
            a = Time(value, format='jd', scale='utc')
            k = [j for (i,j) in zip(ephemav,ephemer[1]) if np.absolute(i - a) <= delt ]
            avohp.append(k[0])
    if os.path.isfile(arqeso) == True:
        for idx, value in enumerate(dadoeso[4]):
            a = Time(value, format='jd', scale='utc')
            k = [j for (i,j) in zip(ephemav,ephemer[1]) if np.absolute(i - a) <= delt ]
            aveso.append(k[0])
    return av160, aviag, avzei, avohp, aveso    

def plot(idx):
    if os.path.isfile(arq160) == True:
        plt.errorbar(av160, dado160[1], yerr=dado160[3], fmt='s', label='PE', color='red')
    if os.path.isfile(arqiag) == True:
        plt.errorbar(aviag, dadoiag[1], yerr=dadoiag[3], fmt='o', label='B&C', color='blue')
    if os.path.isfile(arqohp) == True:
        plt.errorbar(avohp, dadoohp[1], yerr=dadoohp[3], fmt='^', label='OHP', color='black')
    if os.path.isfile(arqeso) == True:
        plt.errorbar(aveso, dadoeso[1], yerr=dadoeso[3], fmt='*', label='ESO', color='green')
    if os.path.isfile(arqzei) == True:
        plt.errorbar(avzei, dadozei[1], yerr=dadozei[3], fmt='v', label='Zeiss', color='magenta')
    plt.title('{}: Declination'.format(obj[idx]), fontsize=sizel)
    plt.xlim(0,360)
    plt.ylim(-600,600)
    plt.xlabel('True Anomaly', fontsize=sizel)
    plt.xticks(np.arange(0,361,45))
    plt.ylabel('Offset (mas)', fontsize=sizel)
    plt.legend(loc=locald[idx], numpoints=1, prop={'size':sizek})
    plt.axhline(0, color='black')
    fig =plt.gcf()
    fig.set_size_inches(7.2,4.05)
    plt.tick_params(axis='both', which='major', labelsize=sizel)
    fig.savefig('{}_DEC.png'.format(obj[idx]),dpi=300, format='png', bbox_inches='tight')
    plt.clf()

    if os.path.isfile(arq160) == True:
        plt.errorbar(av160, dado160[0], yerr=dado160[2], fmt='s', label='PE', color='red')
    if os.path.isfile(arqiag) == True:
        plt.errorbar(aviag, dadoiag[0], yerr=dadoiag[2], fmt='o', label='B&C', color='blue')
    if os.path.isfile(arqohp) == True:
        plt.errorbar(avohp, dadoohp[0], yerr=dadoohp[2], fmt='^', label='OHP', color='black')
    if os.path.isfile(arqeso) == True:
        plt.errorbar(aveso, dadoeso[0], yerr=dadoeso[2], fmt='*', label='ESO', color='green')
    if os.path.isfile(arqzei) == True:
        plt.errorbar(avzei, dadozei[0], yerr=dadozei[2], fmt='v', label='Zeiss', color='magenta')
    plt.title('{}: Right Ascension'.format(obj[idx]), fontsize=sizel)
    plt.xlim(0,360)
    plt.ylim(-600,600)
    plt.xlabel('True Anomaly', fontsize=sizel)
    plt.xticks(np.arange(0,361,45))
    plt.ylabel('Offset (mas)', fontsize=sizel)
    plt.legend(loc=localr[idx], numpoints=1, prop={'size':sizek})
    plt.axhline(0, color='black')
    fig = plt.gcf()
    fig.set_size_inches(7.2,4.05)
    plt.tick_params(axis='both', which='major', labelsize=sizel)
    fig.savefig('{}_RA.png'.format(obj[idx]),dpi=300, format='png', bbox_inches='tight')
    plt.clf()

for idx, value in enumerate(obj):
    arq160 = 'OPD-PE/{}/{}_{}.table_filtered'.format(obj[idx], obj[idx], pee[idx])  ## 160-1 = Ananke, Callirrhoe, Lysithea,  Resto = 160-total
    arqiag = 'OPD-BC/{}/{}_{}.table_filtered'.format(obj[idx], obj[idx], iage[idx])  ## IAG1 = Carme, Lysithea, Pasiphae, Sinope, Resto = IAG_total
    arqzei = 'OPD-ZEI/{}/{}_{}.table_filtered'.format(obj[idx], obj[idx], zeie[idx])  ## ZEI_total = Himalia, resto ZEI1
    arqohp = 'OHP/{}/{}_ucac4_OHP.table_filtered'.format(obj[idx], obj[idx])
    arqeso = 'ESO/{}/{}_ucac4_ESO.table_filtered'.format(obj[idx], obj[idx])
    arqeph = '{}_ephem.dat'.format(obj[idx])
    print value
    if os.path.isfile(arq160) == True:
        f = open(arq160, 'r')
        nl = len(f.readlines())
        f.close()
        if nl == 1:
            dado160 = np.loadtxt(arq160, usecols=(0, 1, 2, 3, 25), unpack=True).reshape((-1,1))
        else:
            dado160 = np.loadtxt(arq160, usecols=(0, 1, 2, 3, 25), unpack=True)
    if os.path.isfile(arqiag) == True:
        f = open(arqiag, 'r')
        nl = len(f.readlines())
        f.close()
        if nl == 1:
            dadoiag = np.loadtxt(arqiag, usecols=(0, 1, 2, 3, 25), unpack=True).reshape((-1,1))
        else:
            dadoiag = np.loadtxt(arqiag, usecols=(0, 1, 2, 3, 25), unpack=True)
    if os.path.isfile(arqzei) == True:
        f = open(arqzei, 'r')
        nl = len(f.readlines())
        f.close()
        if nl == 1:
            dadozei = np.loadtxt(arqzei, usecols=(0, 1, 2, 3, 25), unpack=True).reshape((-1,1))
        else:
            dadozei = np.loadtxt(arqzei, usecols=(0, 1, 2, 3, 25), unpack=True)
    if os.path.isfile(arqohp) == True:
        f = open(arqohp, 'r')
        nl = len(f.readlines())
        f.close()
        if nl == 1:
            dadoohp = np.loadtxt(arqohp, usecols=(0, 1, 2, 3, 25), unpack=True).reshape((-1,1))
        else:
            dadoohp = np.loadtxt(arqohp, usecols=(0, 1, 2, 3, 25), unpack=True)
    if os.path.isfile(arqeso) == True:
        f = open(arqeso, 'r')
        nl = len(f.readlines())
        f.close()
        if nl == 1:
            dadoeso = np.loadtxt(arqeso, usecols=(0, 1, 2, 3, 25), unpack=True).reshape((-1,1))
        else:
            dadoeso = np.loadtxt(arqeso, usecols=(0, 1, 2, 3, 25), unpack=True)
#    julian(idx)
    av160, aviag, avzei, avohp, aveso = getav(idx)
    plot(idx)

os.system('notify-send "Terminou os graficos"')
