import numpy as np
from astropy.coordinates import SkyCoord
from astropy.time import Time
import astropy.units as u
from astropy.table import Table, Column, vstack
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv

f = open('lista_tables', 'r')
lista = f.readlines()
f.close()

tabela = Table(names=('object', 'instantes', 'RA (ICRS) DEC', 'C/A', 'P/A', 'vel', 'distance', 'magR', 'magK', 'long', 'caminho'),\
    dtype=(np.str, np.str, np.str, np.float, np.float, np.float, np.float, np.float, np.float, np.float, np.str))

c = csv.writer(open("agenda.csv", "wb"))
c.writerow(["Subject","Start Date","Start Time","End Date","End Time","All Day Event","Description","Private"])
    
def mostrar(i):
    imagem = tabela[np.where(tabela['numero'] == i)]
    imagem.pprint(max_width=-1)
    img = mpimg.imread(imagem['caminho'][0])
    plt.imshow(img)
    plt.show()

for i in lista:
    arquivo = i.strip()
    print i.strip()
    dados = np.loadtxt(arquivo, skiprows=41, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 21, 22, 25, 26, 28, 29), \
        dtype={'names': ('dia', 'mes', 'ano', 'hor', 'min', 'sec', 'afh', 'afm', 'afs', 'ded', 'dem', 'des', 'ca', 'pa', 'vel', 'delta', 'mR', 'mK', 'long', 'ora', 'ode'), \
       'formats': ('S30', 'S30', 'S30','S30', 'S30', 'S30','S20', 'S20', 'S20','S20', 'S20', 'S20', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8')}, ndmin=1)
################## lendo coordenadas #################
    coor = dados['afh']
    for i in ['afm', 'afs', 'ded', 'dem', 'des']:
        coor = np.core.defchararray.add(coor, ' ')
        coor = np.core.defchararray.add(coor, dados[i])
    stars = SkyCoord(coor, frame='fk5', unit=(u.hourangle, u.degree))
    star_coord = Column(stars.to_string('hmsdms', precision=4, sep=' '), name='RA (ICRS) DEC')
################### lendo tempo ########################
    tim=dados['ano']
    len_iso = ['-', '-', ' ', ':',':']
    arr = ['mes', 'dia', 'hor', 'min', 'sec']
    for i in np.arange(len(arr)):
        tim = np.core.defchararray.add(tim, len_iso[i]) 
        tim = np.core.defchararray.add(tim, dados[arr[i]])
    tim = np.char.array(tim) + '000'
    datas = Time(tim, format='iso', scale='utc')
    occ_data = Column(datas.iso, name='Instantes')
############### definindo parametros #############
    ca = Column(dados['ca']*u.arcsec, name='C/A', format='5.3f')
    pa = Column(dados['pa']*u.deg, name='P/A', format='6.1f')
    vel = Column(dados['vel']*(u.km/u.s), name='vel', format='+5.1f')
    dist = Column(dados['delta']*u.AU, name='distance', format='4.2f')
    magR = Column(dados['mR'], name='MagR', format='4.1f')
    magK = Column(dados['mK'], name='MagK', format='4.1f')
    longi = Column(dados['long'], name='long', format='+3.0f')
    name = Column([arquivo[15:-11].capitalize()]*len(ca), name='object')
    caminho = '/home/altair/Documentos/Maps/Todos/' + np.char.array(datas.iso).rpartition(' ')[:,0].rpartition('-')[:,0].rpartition('-')[:,0] + arquivo[15:-11].capitalize() + arquivo[15:-11].capitalize() + '_' + np.char.array(datas.isot) + '.png'
    t = Table([name, occ_data, star_coord, ca, pa, vel, dist, magR, magK, longi, caminho], names=('object', 'instantes', 'RA (ICRS) DEC', 'C/A', 'P/A', 'vel', 'distance', 'magR', 'magK', 'long', 'caminho'))
    tabela = vstack([tabela, t])

    for i in np.arange(len(stars)):
        subj = 'Ocultation by {}'.format(arquivo[15:-11].capitalize())
        stdate = '{}/{}/{}'.format(datas.iso[i][5:7], datas.iso[i][8:10], datas.iso[i][0:4])
        sttime = datas.iso[i][11:16]
        desc = 'Coord Star: {}\nC/A: {} arcsec\nP/A {} deg\nVelocity: {} km/s\nDistance: {} AU\nMagR: {}\n'.format(star_coord[i], ca[i], pa[i], vel[i], dist[i], magR[i])
        c.writerow([subj,stdate,sttime,stdate,sttime,"False",desc,"False"])
    
tabela.sort('instantes')
aa = Column(np.arange(len(tabela)), name='numero')
tabela.add_column(aa, index=0)
