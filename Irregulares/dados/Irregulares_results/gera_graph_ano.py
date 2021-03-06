import numpy as np
import matplotlib.pyplot as plt

f = open('arquivo', 'r')
lines = f.readlines()
f.close()

arr = np.array([], dtype={'names': ('ano', 'Ananke', 'Callirrhoe', 'Carme', 'Elara', 'Himalia', 'Leda', 'Lysithea', 'Pasiphae', 'Sinope', 'Phoebe', 'Nereid'),
'formats':('i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8')})

for i in np.arange(1992,2015):
    a = [(i, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)]
    b = np.asarray(a, dtype={'names': ('ano', 'Ananke', 'Callirrhoe', 'Carme', 'Elara', 'Himalia', 'Leda', 'Lysithea', 'Pasiphae', 'Sinope', 'Phoebe', 'Nereid'),
'formats':('i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8')})
    arr = np.append(arr,b)

for i in lines:
    g = i.strip().split('/')[1]
    a= np.loadtxt(i.strip(), usecols=[40], dtype={'names':['ano'],'formats':['i8']}, unpack=True, ndmin=1)
    for k in arr['ano']:
        l = np.where(a['ano'] == k)[0]
        if len(l) > 0:
            tam = len(l)
            arr[g][np.where(arr['ano']==k)] = arr[g][np.where(arr['ano']==k)] + tam

fig, ax = plt.subplots(2, sharey=True)
ind = np.arange(len(arr))
space = np.linspace(-0.5,0.5-1.0/len(arr.dtype.names[1:]),len(arr.dtype.names[1:]))
width = space[1]-space[0]
colormap = plt.cm.gist_ncar
cores = [colormap(i) for i in np.linspace(0, 0.95, len(arr.dtype.names[1:]))]
k = 0
a = np.where(arr['ano'] < 2004)
b = np.where(arr['ano'] >= 2004)
for i in arr.dtype.names[1:]:
    ax[0].bar(arr['ano'][a]+space[k], arr[i][a], width, color=cores[-k-1], label=i)
    ax[1].bar(arr['ano'][b]+space[k], arr[i][b], width, color=cores[-k-1], label=i)
    k = k +1
#p2 = plt.bar(ind, a['IAG'][b], 0.9, color='grey', bottom=a['160'][b])
#p3 = plt.bar(ind, a['ZEI'][b], 0.9, color='white', bottom=a['160'][b]+ a['IAG'][b])

ax[0].set_ylabel('Number of Frames', fontsize=15)
ax[0].set_ylim(0,300)
ax[0].set_xlim(np.min(arr['ano'][a])-0.5,np.max(arr['ano'][a])+0.5)
ax[0].set_xticks(arr['ano'][a])
ax[0].set_xticklabels(arr['ano'][a], fontweight='bold')
ax[1].set_ylabel('Number of Frames', fontsize=15)
ax[1].set_xlim(np.min(arr['ano'][b])-0.5,np.max(arr['ano'][b])+0.5)
ax[1].set_xticks(arr['ano'][b])
ax[1].set_xticklabels(arr['ano'][b], fontweight='bold')
fig.set_size_inches(16.0,8.0)
#handles, labels = ax.get_legend_handles_labels()
lgd = plt.legend(loc='upper left', bbox_to_anchor=(1, 1.5))
fig.savefig('framexobj_ano_opd.eps',dpi=300, format='eps',  bbox_extra_artists=(lgd,), bbox_inches='tight')
