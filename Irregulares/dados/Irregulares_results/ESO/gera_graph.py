import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('arquivo', dtype={'names':('number','name'), 'formats':('i8','S20')})

b = np.sort(a)[::-1]

fig, ax = plt.subplots()
ind = np.arange(len(b))
rects = ax.bar(ind, b['number'], 0.9, color='grey')

ax.set_ylabel('Number of Frames', fontsize=15)
ax.set_xticks(ind+1)
ax.set_xticklabels(b['name'], fontweight='bold', rotation=-45)
fig.set_size_inches(8.0,4.5)
fig.savefig('framexobj_eso.eps',dpi=300, format='eps', bbox_inches='tight')
