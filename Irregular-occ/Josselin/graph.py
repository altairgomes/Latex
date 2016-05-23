import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u


#####################################################################

plt.rcParams['text.latex.preamble']=[r"\usepackage{txfonts}"]

params = {'text.usetex' : True,
          'font.size' : 22,
          'font.family' : 'txfonts',
          'text.latex.unicode': True,
          }
          
plt.rcParams.update(params)

sizel = 17

#####################################################################

a = np.loadtxt('precision_all1898-2012.txt', unpack=True)
b = np.loadtxt('precision_all1898-2014.txt', unpack=True)
c = np.loadtxt('precision_gomesjunior2015.txt', unpack=True)

plt.plot(b[0], b[3]*1000, label='all')
plt.plot(a[0], a[3]*1000, label='all-GJ15')
plt.plot(c[0], c[3]*1000, label='GJ15')
plt.xlim(2016,2021)
plt.ylim(0,20)
plt.xlabel('Time (years)', fontsize=sizel)
plt.ylabel('Error RA (mas)', fontsize=sizel)
plt.tick_params(axis='both', which='major', labelsize=sizel)
xt = np.arange(2016,2022,1)
plt.xticks(xt, xt)
plt.legend(labelspacing=0.25, borderpad=0.5, handlelength=1.7, prop={'size':sizel})
fig =plt.gcf()
fig.set_size_inches((17.6*u.cm).to(u.imperial.inch).value,(9.9*u.cm).to(u.imperial.inch).value)
fig.savefig('PH15_err_RA.eps',dpi=300, format='eps', bbox_inches='tight')

plt.clf()

plt.plot(b[0], b[4]*1000, label='all')
plt.plot(a[0], a[4]*1000, label='all-GJ15')
plt.plot(c[0], c[4]*1000, label='GJ15')
plt.xlim(2016,2021)
plt.ylim(0,20)
plt.xlabel('Time (years)', fontsize=sizel)
plt.ylabel('Error DEC (mas)', fontsize=sizel)
plt.tick_params(axis='both', which='major', labelsize=sizel)
xt = np.arange(2016,2022,1)
plt.xticks(xt, xt)
plt.legend(labelspacing=0.25, borderpad=0.5, handlelength=1.7, prop={'size':sizel})
fig =plt.gcf()
fig.set_size_inches((17.6*u.cm).to(u.imperial.inch).value,(9.9*u.cm).to(u.imperial.inch).value)
fig.savefig('PH15_err_DEC.eps',dpi=300, format='eps', bbox_inches='tight')

plt.clf()

plt.plot(b[0], b[2], label='all')
plt.plot(a[0], a[2], label='all-GJ15')
plt.plot(c[0], c[2], label='GJ15')
plt.xlim(2016,2021)
plt.ylim(0,30)
plt.xlabel('Time (years)', fontsize=sizel)
plt.ylabel('Error Dist Sat (km)', fontsize=sizel)
plt.tick_params(axis='both', which='major', labelsize=sizel)
xt = np.arange(2016,2022,1)
plt.xticks(xt, xt)
plt.legend(labelspacing=0.25, borderpad=0.5, handlelength=1.7, prop={'size':sizel})
fig =plt.gcf()
fig.set_size_inches((17.6*u.cm).to(u.imperial.inch).value,(9.9*u.cm).to(u.imperial.inch).value)
fig.savefig('PH15_err_Dist.eps',dpi=300, format='eps', bbox_inches='tight')

plt.clf()

plt.plot(b[0], b[1]*1000, label='all')
plt.plot(a[0], a[1]*1000, label='all-GJ15')
plt.plot(c[0], c[1]*1000, label='GJ15')
plt.xlim(2016,2021)
plt.ylim(0,20)
plt.xlabel('Time (years)', fontsize=sizel)
plt.ylabel('Error (mas)', fontsize=sizel)
plt.tick_params(axis='both', which='major', labelsize=sizel)
xt = np.arange(2016,2022,1)
plt.xticks(xt, xt)
plt.legend(labelspacing=0.25, borderpad=0.5, handlelength=1.7, prop={'size':sizel})
fig =plt.gcf()
fig.set_size_inches((17.6*u.cm).to(u.imperial.inch).value,(9.9*u.cm).to(u.imperial.inch).value)
fig.savefig('PH15_err_angsep.eps',dpi=300, format='eps', bbox_inches='tight')
