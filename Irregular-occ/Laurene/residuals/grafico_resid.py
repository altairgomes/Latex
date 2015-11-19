import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time, TimeDelta
import astropy.units as u
import os

######################################################################3

plt.rcParams['text.latex.preamble']=[r"\usepackage{txfonts}"]

params = {'text.usetex' : True,
          'font.size' : 22,
          'font.family' : 'txfonts',
          'text.latex.unicode': True,
          }
          
plt.rcParams.update(params)

obj = ['Ananke','Carme','Elara','Himalia','Leda','Lysithea','Pasiphae','Sinope']
nobj= ['omc012.dat', 'omc011.dat', 'omc007.dat', 'omc006.dat', 'omc013.dat', 'omc010.dat', 'omc008.dat', 'omc009.dat']

sizel = 17

r = []
for i in np.arange(1995,2016,2):
    r.append(Time('{}-01-01 00:00:00'.format(i), format='iso').jd - 2451544.5)
r = np.array(r)

for t in np.arange(len(obj)):
    dados = np.loadtxt(nobj[t], usecols=[0,1,2], unpack=True)
    time = Time(dados[0], format='jd')
    alfa = dados[1]*u.rad
    dec = dados[2]*u.rad
    plt.plot(time.jd - 2451544.5,alfa.to(u.mas), '+', markersize=5, label='RA')
    plt.plot(time.jd - 2451544.5,dec.to(u.mas), 'x', markersize=5, label='Dec')
    plt.title('{}'.format(obj[t]), fontsize=sizel)
    plt.xlim(Time('1995-01-01 00:00:00', format='iso').jd - 2451544.5,Time('2016-01-01 00:00:00', format='iso').jd - 2451544.5)
    plt.ylim(-400,400)
    plt.xlabel('Time', fontsize=sizel)
    plt.xticks(r, ['{}'.format(i) for i in np.arange(1995,2016,2)])
    plt.ylabel('Residuals (mas)', fontsize=sizel)
    plt.legend(numpoints=1, labelspacing=0.25, borderpad=0.5, handlelength=0.1, prop={'size':sizel})
    plt.axhline(0, color='black')
    fig =plt.gcf()
    fig.set_size_inches(6.93,3.9)
    plt.tick_params(axis='both', which='major', labelsize=sizel)
    fig.savefig('{}_resid.eps'.format(obj[t]),dpi=300, format='eps', bbox_inches='tight')
    plt.clf()


os.system('notify-send "Terminou os graficos"')
