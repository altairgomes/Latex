import numpy as np
from astropy.coordinates import SkyCoord
from astropy.time import Time, TimeDelta
import astropy.units as u
import os

###############################################################

arquivo = ['search_results_ananke_OHP_final',
 'search_results_carme_OHP_final',
 'search_results_elara_OHP_final',
 'search_results_himalia_OHP_final',
 'search_results_leda_OHP_final',
 'search_results_lysithea_OHP_final',
 'search_results_pasiphae_OHP_final',
 'search_results_phoebe_OHP_final',
 'search_results_siarnaq_OHP_final',
 'search_results_sinope_OHP_final',
 'ucac4_Albiorix_eso_global_filtered_final',
 'ucac4_Ananke_160-1_filtered_final',
 'ucac4_Ananke_eso_global_filtered_final',
 'ucac4_Callirrhoe_160-1_filtered_final',
 'ucac4_Callirrhoe_eso_global_filtered_final',
 'ucac4_Carme_160_filtered_final',
 'ucac4_Carme_eso_global_filtered_final',
 'ucac4_Carme_IAG1_filtered_final',
 'ucac4_Elara_160_filtered_final',
 'ucac4_Elara_eso_global_filtered_final',
 'ucac4_Elara_IAG_filtered_final',
 'ucac4_Elara_zei1_filtered_final',
 'ucac4_Himalia_160_filtered_final',
 'ucac4_Himalia_eso_global_filtered_final',
 'ucac4_Himalia_IAG_filtered_final',
 'ucac4_Himalia_zei_filtered_final',
 'ucac4_Leda_160_filtered_final',
 'ucac4_Leda_eso_global_filtered_final',
 'ucac4_Lysithea_160-1_filtered_final',
 'ucac4_Lysithea_eso_global_filtered_final',
 'ucac4_Lysithea_IAG1_filtered_final',
 'ucac4_Megaclite_eso_global_filtered_final',
 'ucac4_Nereida_160_filtered_final',
 'ucac4_Nereida_eso_global_filtered_final',
 'ucac4_Nereida_IAG_filtered_final',
 'ucac4_Paaliaq_eso_global_filtered_final',
 'ucac4_Pasiphae_160_filtered_final',
 'ucac4_Pasiphae_eso_global_filtered_final',
 'ucac4_Pasiphae_IAG1_filtered_final',
 'ucac4_Pasiphae_zei1_filtered_final',
 'ucac4_Phoebe_160_filtered_final',
 'ucac4_Phoebe_eso_global_filtered_final',
 'ucac4_Phoebe_IAG_filtered_final',
 'ucac4_Phoebe_zei1_filtered_final',
 'ucac4_Praxidike_eso_global_filtered_final',
 'ucac4_Siarnaq_eso_global_filtered_final',
 'ucac4_Sinope_160_filtered_final',
 'ucac4_Sinope_eso_global_filtered_final',
 'ucac4_Sinope_IAG1_filtered_final',
 'ucac4_Sycorax_eso_global_filtered_final',
 'ucac4_Themisto_eso_global_filtered_final']

table = ['Ananke_ucac4_OHP.table_filtered',
 'Carme_ucac4_OHP.table_filtered',
 'Elara_ucac4_OHP.table_filtered',
 'Himalia_ucac4_OHP.table_filtered',
 'Leda_ucac4_OHP.table_filtered',
 'Lysithea_ucac4_OHP.table_filtered',
 'Pasiphae_ucac4_OHP.table_filtered',
 'Phoebe_ucac4_OHP.table_filtered',
 'Siarnaq_ucac4_OHP.table_filtered',
 'Sinope_ucac4_OHP.table_filtered',
 'Albiorix_ucac4_ESO.table_filtered',
 'Ananke_160-1.table_filtered',
 'Ananke_ucac4_ESO.table_filtered',
 'Callirrhoe_160-1.table_filtered',
 'Callirrhoe_ucac4_ESO.table_filtered',
 'Carme_160-total.table_filtered',
 'Carme_ucac4_ESO.table_filtered',
 'Carme_IAG1.table_filtered',
 'Elara_160-total.table_filtered',
 'Elara_ucac4_ESO.table_filtered',
 'Elara_IAG_total.table_filtered',
 'Elara_ZEI1.table_filtered',
 'Himalia_160-total.table_filtered',
 'Himalia_ucac4_ESO.table_filtered',
 'Himalia_IAG_total.table_filtered',
 'Himalia_ZEI_total.table_filtered',
 'Leda_160-total.table_filtered',
 'Leda_ucac4_ESO.table_filtered',
 'Lysithea_160-1.table_filtered',
 'Lysithea_ucac4_ESO.table_filtered',
 'Lysithea_IAG1.table_filtered',
 'Megaclite_ucac4_ESO.table_filtered',
 'Nereida_160-total.table_filtered',
 'Nereida_ucac4_ESO.table_filtered',
 'Nereida_IAG_total.table_filtered',
 'Paaliaq_ucac4_ESO.table_filtered',
 'Pasiphae_160-total.table_filtered',
 'Pasiphae_ucac4_ESO.table_filtered',
 'Pasiphae_IAG1.table_filtered',
 'Pasiphae_ZEI1.table_filtered',
 'Phoebe_160-total.table_filtered',
 'Phoebe_ucac4_ESO.table_filtered',
 'Phoebe_IAG_total.table_filtered',
 'Phoebe_ZEI1.table_filtered',
 'Praxidike_ucac4_ESO.table_filtered',
 'Siarnaq_ucac4_ESO.table_filtered',
 'Sinope_160-total.table_filtered',
 'Sinope_ucac4_ESO.table_filtered',
 'Sinope_IAG1.table_filtered',
 'Sycorax_ucac4_ESO.table_filtered',
 'Themisto_ucac4_ESO.table_filtered']

output = ['NSDC/NSDC_Ananke_OHP.txt',
'NSDC/NSDC_Carme_OHP.txt',
'NSDC/NSDC_Elara_OHP.txt',
'NSDC/NSDC_Himalia_OHP.txt',
'NSDC/NSDC_Leda_OHP.txt',
'NSDC/NSDC_Lysithea_OHP.txt',
'NSDC/NSDC_Pasiphae_OHP.txt',
'NSDC/NSDC_Phoebe_OHP.txt',
'NSDC/NSDC_Siarnaq_OHP.txt',
'NSDC/NSDC_Sinope_OHP.txt',
'NSDC/NSDC_Albiorix_ESO.txt',
'NSDC/NSDC_Ananke_160.txt',
'NSDC/NSDC_Ananke_ESO.txt',
'NSDC/NSDC_Callirrhoe_160.txt',
'NSDC/NSDC_Callirrhoe_ESO.txt',
'NSDC/NSDC_Carme_160.txt',
'NSDC/NSDC_Carme_ESO.txt',
'NSDC/NSDC_Carme_IAG.txt',
'NSDC/NSDC_Elara_160.txt',
'NSDC/NSDC_Elara_ESO.txt',
'NSDC/NSDC_Elara_IAG.txt',
'NSDC/NSDC_Elara_ZEI.txt',
'NSDC/NSDC_Himalia_160.txt',
'NSDC/NSDC_Himalia_ESO.txt',
'NSDC/NSDC_Himalia_IAG.txt',
'NSDC/NSDC_Himalia_ZEI.txt',
'NSDC/NSDC_Leda_160.txt',
'NSDC/NSDC_Leda_ESO.txt',
'NSDC/NSDC_Lysithea_160.txt',
'NSDC/NSDC_Lysithea_ESO.txt',
'NSDC/NSDC_Lysithea_IAG.txt',
'NSDC/NSDC_Megaclite_ESO.txt',
'NSDC/NSDC_Nereid_160.txt',
'NSDC/NSDC_Nereid_ESO.txt',
'NSDC/NSDC_Nereid_IAG.txt',
'NSDC/NSDC_Paaliaq_ESO.txt',
'NSDC/NSDC_Pasiphae_160.txt',
'NSDC/NSDC_Pasiphae_ESO.txt',
'NSDC/NSDC_Pasiphae_IAG.txt',
'NSDC/NSDC_Pasiphae_ZEI.txt',
'NSDC/NSDC_Phoebe_160.txt',
'NSDC/NSDC_Phoebe_ESO.txt',
'NSDC/NSDC_Phoebe_IAG.txt',
'NSDC/NSDC_Phoebe_ZEI.txt',
'NSDC/NSDC_Praxidike_ESO.txt',
'NSDC/NSDC_Siarnaq_ESO.txt',
'NSDC/NSDC_Sinope_160.txt',
'NSDC/NSDC_Sinope_ESO.txt',
'NSDC/NSDC_Sinope_IAG.txt',
'NSDC/NSDC_Sycorax_ESO.txt',
'NSDC/NSDC_Themisto_ESO.txt']

code = ['OH',
'OH',
'OH',
'OH',
'OH',
'OH',
'OH',
'OH',
'OH',
'OH',
'E',
'PE',
'E',
'PE',
'E',
'PE',
'E',
'BC',
'PE',
'E',
'BC',
'Z',
'PE',
'E',
'BC',
'Z',
'PE',
'E',
'PE',
'E',
'BC',
'E',
'PE',
'E',
'BC',
'E',
'PE',
'E',
'BC',
'Z',
'PE',
'E',
'BC',
'Z',
'E',
'E',
'PE',
'E',
'BC',
'E',
'E',]

iau_code = [511,
511,
511,
511,
511,
511,
511,
511,
511,
511,
809,
874,
809,
874,
809,
874,
809,
874,
874,
809,
874,
874,
874,
809,
874,
874,
874,
809,
874,
809,
874,
809,
874,
809,
874,
809,
874,
809,
874,
874,
874,
809,
874,
874,
809,
809,
874,
809,
874,
809,
809,]

list_filt = {
'r cousins': 'R',
'v cousins': 'V',
'': 'un',
'filtro desconhecido': 'un',
'i gunn': 'I',
'clear': 'C',
'no filter': 'C',
'cl': 'C',
'i': 'I',
'r': 'R',
'u': 'U',
'c': 'C',
'v': 'V',
'cuso4': 'un',
'b': 'B',
'dark': 'un',
"'r       '": 'R',
're': 'RE'
}

###############################################################
dif = TimeDelta(60*60*6, format='sec')

ra_formatter = lambda x: "%07.4f" %x
dec_formatter = lambda x: "%06.3f" %x
alt_formatter = lambda x: "%.1f" %x
int_formatter = lambda x: "%02d" %x
int2_formatter = lambda x: "%+03d" %x

def coord_pack(coord):
    if type(coord) == SkyCoord:
        if not coord.isscalar:
            return coord
        return SkyCoord([coord.ra], [coord.dec], frame=coord.frame)
    a, b = [], []
    for i in coord:
        a.append(i.ra)
        b.append(i.dec)
    coord = SkyCoord(a,b, frame='fk5')
    return coord
    
def text_coord(coord):
    coord = coord_pack(coord)
    ra = np.char.array([int_formatter(j) for j in coord.ra.hms.h]) + ' ' + np.char.array([int_formatter(j) for j in coord.ra.hms.m]) + ' ' + np.char.array([ra_formatter(j) for j in coord.ra.hms.s])
    sign = np.char.array(np.sign(coord.dec)).replace('-1.0', '-').replace('1.0', '+').replace('0.0', '+')
    dec = sign + np.char.array([int_formatter(j) for j in np.absolute(coord.dec.dms.d)]) + ' ' + np.char.array([int_formatter(j) for j in np.absolute(coord.dec.dms.m)]) + ' ' + np.char.array([dec_formatter(j) for j in np.absolute(coord.dec.dms.s)])
    return ra, dec
    
for idy, value in enumerate(arquivo):

    print 'Arquivo: {}\nTable: {}\nGera: {}\nCode: {}\nIAU Code: {}\n'.format(arquivo[idy], table[idy], output[idy], code[idy], iau_code[idy])
    
    f = open(arquivo[idy], 'r')
    dados = f.readlines()
    f.close()

    erros = np.loadtxt(table[idy], usecols=(2, 3, 25), ndmin=1, dtype={'names': ('ra', 'dec', 'time'), 'formats': ('f8', 'f8', 'f16')})
    datasgeral = Time(erros['time'], format='jd', scale='utc')

    g = open(output[idy], 'w')

    for i in dados:
        coord = SkyCoord(i[252:280], frame='icrs', unit=(u.hourangle,u.deg))
        time = np.float(i[303:320].strip())
        epoch = Time(time, scale='utc', format='jd')
        mag = np.float(i[79:86].strip())
        filtro = i[326:348].strip().lower()
        if filtro not in list_filt.keys():
           list_filt[filtro] = 'NAN'
        filt = list_filt[filtro]
        time_dif = datasgeral - epoch
        idx = [i for i in np.arange(len(time_dif)) if np.absolute(time_dif[i]) < dif]
        raerr = erros['ra'][idx]
        deerr = erros['dec'][idx]
        ra, dec = text_coord(coord)
        g.write(' {} {} {} {} {} {}  {} {} {:4.0f} {:4.0f} {:4.1f} {:2s} {:2s} {:3d}\n'\
.format(epoch.iso.split(' ')[0].split('-')[0], epoch.iso.split(' ')[0].split('-')[1], epoch.iso.split(' ')[0].split('-')[2], epoch.iso.split(' ')[1].split(':')[0],
epoch.iso.split(' ')[1].split(':')[1], epoch.iso.split(' ')[1].split(':')[2][0:4], ra[0], dec[0], raerr[0], deerr[0], mag, filt, code[idy], iau_code[idy]))

    g.close()
    


