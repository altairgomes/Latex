import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('arquivo2', dtype={'names':('name','IAG', '160','ZEI'), 'formats':('S20','f16', 'f16', 'f16')})

c = a['IAG']+ a['160'] + a['ZEI']

b = np.argsort(c)[::-1]

fig, ax = plt.subplots()
ind = np.arange(len(b))

p1 = plt.bar(ind, a['160'][b], 0.9, color='black')
p2 = plt.bar(ind, a['IAG'][b], 0.9, color='grey', bottom=a['160'][b])
p3 = plt.bar(ind, a['ZEI'][b], 0.9, color='white', bottom=a['160'][b]+ a['IAG'][b])

ax.set_ylabel('Number of Frames', fontsize=15)
ax.set_xticks(ind+1)
ax.set_xticklabels(a['name'][b], fontweight='bold', rotation=-45)
fig.set_size_inches(8.0,4.5)
plt.legend( (p1[0], p2[0], p3[0]), ('Perkin-Elmer', 'Boller & Chivens', 'Zeiss') )
fig.savefig('framexobj_opd.eps',dpi=300, format='eps', bbox_inches='tight')
