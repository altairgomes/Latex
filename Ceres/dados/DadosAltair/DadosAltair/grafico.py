import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.time import Time
import os

################## Definicao de Parametros  #################################################

arquivo = 'data_ratio_poly_outCUT'			### arquivo de dados de entrada
arqsaida = 'saida.dat'				### arquivo de dados de saida
datainicio = '2010-08-17 00:00:00'		### data de referencia de contagem para o plot

#############################################################################################

Ceres = [
('BH', 'CEAMIG'),
('OPD', 'LNA'),
('INPE', 'INPE'),
('UEPG', 'UEPG')
]

Ceres = Ceres[::-1]

axes=plt.gca()
plt.xlabel('Time (seconds after {inicio}, UTC)'.format(inicio=datainicio))
plt.ylabel('Flux Ratio')

t = Time(datainicio, format='iso', scale='utc')
fator = 0.2
for i in np.arange(len(Ceres)):
    
    pasta = Ceres[i][0]
    x = np.loadtxt('{}/data_ratio_poly_out'.format(pasta), unpack=True)
    y, z, t, u = [], [], [], []
    if os.path.isdir('{}/im'.format(pasta)):
        y = np.loadtxt('{}/im/fort.20'.format(pasta), unpack=True)
        z = np.loadtxt('{}/im/fort.21'.format(pasta), unpack=True)
        t = np.loadtxt('{}/im/fort.22'.format(pasta), unpack=True)
        u = np.loadtxt('{}/im/fort.23'.format(pasta), unpack=True)
    if os.path.isdir('{}/em'.format(pasta)):
        ye = np.loadtxt('{}/em/fort.20'.format(pasta), unpack=True)
        ze = np.loadtxt('{}/em/fort.21'.format(pasta), unpack=True)
        te = np.loadtxt('{}/em/fort.22'.format(pasta), unpack=True)
        ue = np.loadtxt('{}/em/fort.23'.format(pasta), unpack=True)
        if y == []:
            y = ye
        else:
            y = np.append(y, ye, axis=1)
        if z == []:
            z = ze
        else:
            z = np.append(z, ze, axis=1)
        if t == []:
            t = te
        else:
            t = np.append(t, te, axis=1)
        if u == []:
            u = ue
        else:
            u = np.append(u, ue, axis=1)

    ini = Time(datainicio, format='iso', scale='utc')
    plt.plot(x[0], x[1] + fator*i, color='blue', label='dados')
    if Ceres[i][0] == 'BH' or Ceres[i][0] == 'UEPG':
        plt.scatter(x[0], x[1] + fator*i, facecolors='none', color='blue')
    plt.plot(y[0], y[1] + fator*i, color='black', label='mod. geom.', lw=1.5)
    plt.plot(u[0], u[1] + fator*i, 'r', label='Sombra Int.')
    plt.text(81330,0.95 + fator*i, Ceres[i][1])


axes.set_xlim([81300,81900])
#axes.set_ylim([34833,34834])

fig = plt.gcf()
fig.set_size_inches(6, 7.5)
ax = plt.gca()
ax.ticklabel_format(useOffset=False)
#ax.get_yaxis().set_ticks(np.arange(10))
plt.savefig('Ceres_2010_fluxratio.eps', format='eps', dpi=300)
