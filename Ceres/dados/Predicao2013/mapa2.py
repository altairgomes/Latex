from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import os
import astropy.units as u
from astropy.time import Time, TimeDelta
from astropy.coordinates import SkyCoord, EarthLocation

######################################### lendo arquivo de dados da ocultacao e de observatorios ##############################

def lerdados():
    dados = np.loadtxt(arquivo, skiprows=41, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 21, 22, 25, 26, 28, 29), \
        dtype={'names': ('dia', 'mes', 'ano', 'hor', 'min', 'sec', 'afh', 'afm', 'afs', 'ded', 'dem', 'des', 'ca', 'pa', 'vel', 'delta', 'mR', 'mK', 'long', 'ora', 'ode'), 
        'formats': ('S30', 'S30', 'S30','S30', 'S30', 'f8','i4', 'i4', 'f8','i4', 'i4', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8', 'f8')})

################## lendo coordenadas #################

    alfa = np.core.defchararray.add(np.array(map(str, dados['afh'])), [' '])
    alfa = np.core.defchararray.add(alfa, np.array(map(str, dados['afm'])))
    alfa = np.core.defchararray.add(alfa, [' '])
    alfa = np.core.defchararray.add(alfa, np.array(map(str, dados['afs'])))
    delta = np.core.defchararray.add(np.array(map(str, dados['ded'])), [' '])
    delta = np.core.defchararray.add(delta, np.array(map(str, dados['dem'])))
    delta = np.core.defchararray.add(delta, [' '])
    delta = np.core.defchararray.add(delta, np.array(map(str, dados['des'])))
    coor = np.core.defchararray.add(alfa, [' '])
    coor = np.core.defchararray.add(coor, delta)
    stars = SkyCoord(coor, frame='icrs', unit=(u.hourangle, u.degree))

################### lendo tempo ########################

    tempo = np.core.defchararray.add(np.array(dados['ano']), ['-'])
    tempo = np.core.defchararray.add(tempo, np.array(dados['mes']))
    tempo = np.core.defchararray.add(tempo, ['-'])
    tempo = np.core.defchararray.add(tempo, np.array(dados['dia']))
    tempo = np.core.defchararray.add(tempo, [' '])
    tempo = np.core.defchararray.add(tempo, np.array(dados['hor']))
    tempo = np.core.defchararray.add(tempo, [':'])
    tempo = np.core.defchararray.add(tempo, np.array(dados['min']))
    tempo = np.core.defchararray.add(tempo, [':'])
    tempo = np.core.defchararray.add(tempo, np.array(map(str, dados['sec'])))
    datas = Time(tempo, format='iso', scale='utc')

############### definindo parametros #############
    ca = dados['ca']*u.arcsec
    pa = dados['pa']*u.deg
    vel = dados['vel']*(u.km/u.s)
    dist = dados['delta']*u.AU
    off_ra = dados['ora']*u.mas
    off_de = dados['ode']*u.mas
    return stars, datas, ca, pa, vel, dist, off_ra, off_de, dados['mR'], dados['mK'], dados['long']

################################### definido funcao que imprime o mapa #############################################

def geramapa():
    lon = stars.ra - datas.sidereal_time('mean', 'greenwich')
    fig = plt.figure(figsize=(mapsize[0].to(u.imperial.inch).value, mapsize[1].to(u.imperial.inch).value))
    m = Basemap(projection='ortho',lat_0=stars.dec.value,lon_0=lon.value,resolution=resolution, area_thresh=2000)
#    m = Basemap(projection='ortho',lat_0=stars.dec.value,lon_0=lon.value,resolution=resolution,llcrnrx=-800000.,llcrnry=-450000.,urcrnrx=1200000.,urcrnry=1050000., area_thresh=2000)
    axf = fig.add_axes([-0.001,-0.001,1.002,1.002])
    axf.set_rasterization_zorder(1)
#    m = Basemap(projection='ortho',lat_0=stars.dec.value,lon_0=lon.value,resolution=resolution, llcrnrx=-7000000,llcrnry=-7000000,urcrnrx=7000000,urcrnry=7000000)
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
#    m.drawstates(linewidth=0.5)
    m.drawmeridians(np.arange(0,360,30))
    m.drawparallels(np.arange(-90,90,30))
    m.drawmapboundary()
    ptcolor = 'red'
    lncolor = 'black'
    dscolor = 'black'
    if mapstyle == '2':
        m.drawmapboundary(fill_color='aqua')
        m.fillcontinents(color='coral',lake_color='aqua')
        ptcolor = 'red'
        lncolor = 'blue'
        dscolor = 'red'
    elif mapstyle == '3':
        m.shadedrelief()
        ptcolor = 'red'
        lncolor = 'blue'
        dscolor = 'red'
    elif mapstyle == '4':
        m.bluemarble()
        ptcolor = 'red'
        lncolor = 'red'
        dscolor = 'red'
    elif mapstyle == '5':
        m.etopo()
        ptcolor = 'red'
        lncolor = 'red'
        dscolor = 'red'
    if os.path.isfile(sitearq) == True:
        xpt,ypt = m(sites['lon'],sites['lat'])
        m.plot(xpt,ypt,'bo')
        for i in np.arange(len(xpt)):
            plt.text(xpt[i]+50000,ypt[i]-5000,sites['nome'][i])
    CS=m.nightshade(datas.datetime, alpha=0.2, zorder=0.5)
    a, b =m(lon.value, stars.dec.value)
    a = a*u.m
    b = b*u.m
    dista = (dist.to(u.km)*ca.to(u.rad)).value*u.km
    disterr = (dist.to(u.km)*erro.to(u.rad)).value*u.km
    vec = np.arange(0,7000,(np.absolute(vel)*(60*u.s)).value)*u.km + np.absolute(vel)*(60*u.s)
    vec = np.concatenate((vec.value,-vec.value), axis=0)*u.km
    ax = a + dista*np.sin(pa)
    ax2 = ax + vec*np.cos(pa)
    ax3 = ax2 - tamanho/2*np.sin(pa)
    ax4 = ax2 + tamanho/2*np.sin(pa)
    ax5 = a + (dista-disterr)*np.sin(pa) + vec*np.cos(pa)
    ax6 = a + (dista+disterr)*np.sin(pa) + vec*np.cos(pa)
    by = b + dista*np.cos(pa)
    by2 = by - vec*np.sin(pa)
    by3 = by2 - tamanho/2*np.cos(pa)
    by4 = by2 + tamanho/2*np.cos(pa)
    by5 = b + (dista-disterr)*np.cos(pa) - vec*np.sin(pa)
    by6 = b + (dista+disterr)*np.cos(pa) - vec*np.sin(pa)
    m.plot(ax,by, 'o', color=ptcolor, markersize=mapsize[0].value*20/46)
    m.plot(ax2.to(u.m),by2.to(u.m), 'o', color=ptcolor, markersize=mapsize[0].value*10/46)
    m.plot(ax3.to(u.m), by3.to(u.m), color=lncolor)
    m.plot(ax4.to(u.m), by4.to(u.m), color=lncolor)
    m.quiver(ax+800000*u.m,by-1000000*u.m, 10*np.cos(pa),-10*np.sin(pa), width=0.005)

#    ax2 = a + dista*np.sin(pa) + [(i - datas).sec for i in temposplot]*u.s*vel*np.cos(paplus)
#    by2 = b + dista*np.cos(pa) - [(i - datas).sec for i in temposplot]*u.s*vel*np.sin(paplus)

#    labels = [i.iso.split()[1][0:8] for i in temposplot]
#    m.plot(ax2, by2, 'ro')
    
#    for label, axpt, bypt in zip(labels, ax2.value, by2.value):
#        plt.text(axpt + 30000, bypt + 250000, label, rotation=60, weight='bold')

#    if os.path.isfile(sitearq) == True:
#        xpt,ypt = m(sites['lon'],sites['lat'])
#        m.plot(xpt,ypt,'bo')
#        for i in np.arange(len(xpt)):
#            plt.text(xpt[i]+50000,ypt[i]+15000,sites['nome'][i])

#    m.plot(ax5.to(u.m), by5.to(u.m), '--', color=dscolor, label='+-{} error'.format(erro))
#    m.plot(ax6.to(u.m), by6.to(u.m), '--', color=dscolor)
#    plt.legend(fontsize=mapsize[0].value*21/46)

    fig = plt.gcf()
    fig.set_size_inches(mapsize[0].to(u.imperial.inch).value, mapsize[1].to(u.imperial.inch).value)
#    plt.title('Objeto       Diam   dots <>  ra_off_obj_de  ra_of_star_de\n{:10s} {:4.0f} km  60 s <> {:+6.1f} {:+6.1f}  {:+6.1f} {:+6.1f} \n'
#        .format(obj, tamanho.value, ob_off_ra.value, ob_off_de.value, st_off_ra.value, st_off_de.value), fontsize=mapsize[0].value*25/46, fontproperties='FreeMono', weight='bold')
#    plt.xlabel('\n year-m-d    h:m:s UT     ra__dec__J2000__candidate    C/A    P/A    vel   Delta   R*   K*  long\n\
#{}  {:02d} {:02d} {:07.4f} {:+02d} {:02d} {:06.3f} {:6.3f} {:6.2f} {:6.2f}  {:5.2f} {:5.1f} {:4.1f}  {:3.0f}'
#        .format(datas.iso, int(stars.ra.hms.h), int(stars.ra.hms.m), stars.ra.hms.s, int(stars.dec.dms.d), np.absolute(int(stars.dec.dms.m)), np.absolute(stars.dec.dms.s),
#        ca.value, pa.value, vel.value, dist.value, magR, magK, longi), fontsize=mapsize[0].value*21/46, fontproperties='FreeMono', weight='bold')
#    plt.savefig('{}_{}.eps'.format(obj, datas.isot),dpi=300, format='eps')
    plt.savefig('{}_{}.eps'.format(obj, datas.isot), format='eps', dpi=300)
    print 'Gerado: {}_{}.eps'.format(obj, datas.isot)
    plt.clf()

###########################################################################################################################
###########################################################################################################################
######################################## lendo arquivo de entrada #########################################################

f = open('mapa_in.dat', 'r')

in_data = f.readlines()
option = in_data[0].rsplit()[0]
obj = in_data[18].rsplit()[0]
tamanho = int(in_data[19].rsplit()[0])*u.km
erro = float(in_data[20].rsplit()[0])*u.mas
sitearq = in_data[21].rsplit()[0]
resolution = in_data[22].rsplit()[0]
mapsize = map(float, in_data[23].rsplit()[0:2])*u.cm
mapstyle = in_data[24].rsplit()[0]
if option == '1':
    arquivo = in_data[2].rsplit()[0]
    stars, datas, ca, pa, vel, dist, ob_off_ra, ob_off_de, magR, magK, longi = lerdados()
    vals = np.arange(len(stars))
    st_off_ra = st_off_de = 0.0*u.mas
elif option == '2':
    stars = SkyCoord(in_data[4].rsplit('#')[0], frame='icrs', unit=(u.hourangle, u.degree))
    datas = Time(in_data[5].rsplit('#')[0], format='iso', scale='utc')
    ca = float(in_data[6].rsplit('#')[0].strip())*u.arcsec
    pa = float(in_data[7].rsplit('#')[0].strip())*u.deg
    dist = float(in_data[8].rsplit('#')[0].strip())*u.AU
    vel = float(in_data[9].rsplit('#')[0].strip())*(u.km/u.s)
    ob_off_ra = float(in_data[10].rsplit('#')[0].strip())*u.mas
    ob_off_de = float(in_data[11].rsplit('#')[0].strip())*u.mas
    st_off_ra = float(in_data[12].rsplit('#')[0].strip())*u.mas
    st_off_de = float(in_data[13].rsplit('#')[0].strip())*u.mas
    off_ra = ob_off_ra - st_off_ra
    off_de = ob_off_de - st_off_de
    magR = float(in_data[14].rsplit()[0].strip())
    magK = float(in_data[15].rsplit()[0].strip())
    longi = float(in_data[16].rsplit()[0].strip())
    dca = off_ra*np.sin(pa) - off_de*np.cos(pa)
    dt = int(((-off_ra*np.cos(pa) - off_de*np.sin(pa)).to(u.rad)*dist.to(u.km)/vel).value)*u.s
    ca = ca + dca
    datas = datas + dt
    vals = [0]

f.close()

paplus = ((pa > 180*u.deg) and pa - 180*u.deg) or pa
inttime = 5*u.min

deltas = float(datas.iso.rsplit(':')[2])*u.s
tempoint = datas - deltas
temposplot = [ tempoint - inttime + n*(60*u.s) for n in np.arange(2*6*(inttime.value)) ]

datas.delta_ut1_utc = 0

if os.path.isfile(sitearq) == True:
    sites = np.loadtxt(sitearq,  dtype={'names': ('lat', 'lon', 'alt', 'nome'), 'formats': ('f8', 'f8', 'f8', 'S30')})

###################### rodando o programa ######################

#map(geramapa, vals)
geramapa()

os.system('notify-send "Terminou de gerar os mapas" --icon=dialog-information')

