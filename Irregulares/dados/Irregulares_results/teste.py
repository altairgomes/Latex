import numpy as np
from astropy.time import Time
from astropy import units
from astropy.coordinates import SkyCoord

arquivo1 = 'ucac4_Himalia_IAG_filtered_final'
arquivo2 = 'Himalia_IAG_total.table_filtered'
local = 'IAG'

x = np.loadtxt(arquivo1, usecols=(10, 35, 36, 43), unpack=True)
filt = np.genfromtxt(arquivo1, usecols=45, dtype='str')
y = np.loadtxt(arquivo2, usecols=(2, 3, 25), unpack=True)

t = Time(x[3], format='jd', scale='utc')
u = Time(y[2], format='jd', scale='utc')

k = t
k.precision = 0
l = u
l.precision = 0

b = [local for k in range(len(x[0]))]

n = []
o = []
for i in t:
    m = u - i
    for index, item in enumerate(m.jd):
        if -1.0 < item < 1.0:
            valor = index
    n.append(y[0][valor])
    o.append(y[1][valor])

r = SkyCoord(ra=[x[1]]*units.hours, dec=[x[2]]*units.degree, frame='icrs')
print r.ra

#print len(x[1]), len(x[2]), len(n), len(o), len(t.jd), len(x[0]), filt, local

z = np.array(zip(x[1], x[2], n, o, t.jd, x[0], filt, b), dtype=[('x[1]', float), ('x[2]', float), ('n', float), ('o', float), ('t.jd', float), ('x[0]', float), ('filt', 'S8'), ('b', 'S8')])

#np.savetxt('output.txt', data, fmt=["%.3f",]*3 + ["%s"])
#np.savetxt('saida.dat', z, fmt=["%10.6f",]*2 + ["%5.1f",]*2 + ["%15.8f",] + ["%6.1f",] + ["%8s",]*2)
#np.savetxt('saida2.dat', z, delimiter=' & ', fmt=["%10.6f",]*2 + ["%5.1f",]*2 + ["%15.8f",] + ["%6.1f",] + ["%8s",]*2)
