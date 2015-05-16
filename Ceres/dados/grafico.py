import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.time import Time

################## Definicao de Parametros  #################################################

arquivo = 'data_ratio_poly_outCUT'			### arquivo de dados de entrada
arqsaida = 'saida.dat'				### arquivo de dados de saida
datainicio = '2013-10-25 00:00:00'		### data de referencia de contagem para o plot

#############################################################################################

Ceres = [
('Ted_Hampton', 'Hampton'),
('Ted_Topsfield', 'Topsfield'),
('ClayCenter', 'Brookline'),
('JBrooks', 'Winchester'),
('Greenbelt_Dunham', 'Greenbelt'),
('Maley', 'Alexandria'),
('CHAD', 'Owings'),
('Mechanicsville_Dunham', 'Mechanicville'),
('Varina_Dunham', 'Varina')
]

Ceres = Ceres[::-1]

axes=plt.gca()
plt.xlabel('Time (seconds after {inicio})'.format(inicio=datainicio))
plt.ylabel('Flux Ratio')

t = Time(datainicio, format='iso', scale='utc')
fator = 1.0
for i in np.arange(len(Ceres)):
    
    pasta = Ceres[i][0]
    x = np.loadtxt('{}/immersion/data_ratio_poly_out'.format(pasta), unpack=True)
    yi = np.loadtxt('{}/immersion/fort.20'.format(pasta), unpack=True)
    zi = np.loadtxt('{}/immersion/fort.21'.format(pasta), unpack=True)
    ti = np.loadtxt('{}/immersion/fort.22'.format(pasta), unpack=True)
    ui = np.loadtxt('{}/immersion/fort.23'.format(pasta), unpack=True)
    ye = np.loadtxt('{}/emersion/fort.20'.format(pasta), unpack=True)
    ze = np.loadtxt('{}/emersion/fort.21'.format(pasta), unpack=True)
    te = np.loadtxt('{}/emersion/fort.22'.format(pasta), unpack=True)
    ue = np.loadtxt('{}/emersion/fort.23'.format(pasta), unpack=True)
    y = np.append(yi, ye, axis=1)
    z = np.append(zi, ze, axis=1)
    t = np.append(ti, te, axis=1)
    u = np.append(ui, ue, axis=1)

    ini = Time(datainicio, format='iso', scale='utc')
    plt.plot(x[0], x[1] + fator*i, color='blue', label='dados')
#    plt.plot(x[0], x[1] + fator*i, 's', color='blue', label='dados')
    plt.plot(y[0], y[1] + fator*i, color='black', label='mod. geom.', lw=1.5)
    plt.plot(u[0], u[1] + fator*i, 'r', label='Sombra Int.')
    plt.text(34880,0.7 + fator*i, Ceres[i][1])


#axes.set_xlim([34833,34834])
#axes.set_ylim([34833,34834])


plt.savefig('Ceres_2013_fluxratio.png')
