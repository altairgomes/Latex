import numpy as np
import matplotlib.pyplot as plt

f = open('arquivo3', 'r')
lines = f.readlines()
f.close()

arr = np.array([], dtype={'names': ('ano', 'Ananke', 'Callirrhoe', 'Carme', 'Elara', 'Himalia', 'Leda', 'Lysithea', 'Pasiphae', 'Sinope', 'Phoebe', 'Siarnaq'),
'formats':('i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8')})

for i in np.arange(1998,2009):
    a = [(i, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)]
    b = np.asarray(a, dtype={'names': ('ano', 'Ananke', 'Callirrhoe', 'Carme', 'Elara', 'Himalia', 'Leda', 'Lysithea', 'Pasiphae', 'Sinope', 'Phoebe', 'Siarnaq'),
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

fig, ax = plt.subplots()
ind = np.arange(len(arr))
space = np.linspace(-0.5,0.5-1.0/len(arr.dtype.names[1:]),len(arr.dtype.names[1:]))
width = space[1]-space[0]
colormap = plt.cm.gist_ncar
cores = [colormap(i) for i in np.linspace(0, 0.95, len(arr.dtype.names[1:]))]
k = 0
for i in arr.dtype.names[1:]:
    ax.bar(arr['ano']+space[k], arr[i], width, color=cores[-k-1], label=i)
    k = k +1
#p2 = plt.bar(ind, a['IAG'][b], 0.9, color='grey', bottom=a['160'][b])
#p3 = plt.bar(ind, a['ZEI'][b], 0.9, color='white', bottom=a['160'][b]+ a['IAG'][b])

ax.set_ylabel('Number of Frames', fontsize=15)
ax.set_ylim(0,200)
ax.set_xlim(np.min(arr['ano'])-0.5,np.max(arr['ano'])+0.5)
ax.set_xticks(arr['ano'])
ax.set_xticklabels(arr['ano'], fontweight='bold')
fig.set_size_inches(16.0,4.0)
#handles, labels = ax.get_legend_handles_labels()
lgd = plt.legend(loc='upper left', bbox_to_anchor=(1, 1.03))
fig.savefig('framexobj_ano_ohp.eps',dpi=300, format='eps',  bbox_extra_artists=(lgd,), bbox_inches='tight')
