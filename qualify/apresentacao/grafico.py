import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))/np.sqrt(2*np.pi*np.power(sig, 2.))


tam = [28,21]*u.cm

fig = plt.figure(frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

plt.plot([0.0, 2.4], [20.0, 20.0], color='black')
plt.plot([2.4, 2.4], [20.0, 16.65], color='black')
plt.plot([2.4, 25.6], [16.65, 16.65], color='black')
plt.plot([25.6, 25.6], [16.65, 20.0], color='black')
plt.plot([25.6, 28.0], [20.0, 20.0], color='black')

plt.plot([27.0, 27.0], [0.0, 2.0], color='black', zorder=0.9)

x = np.linspace(0, 28.0, 1000)
y = 3*gaussian(x, 1.4, 0.5) + gaussian(x, 3.4, 0.5) + 1
plt.plot(x,y, color='black', zorder=0.9)

circle1=plt.Circle((27.0,1.0),0.15, color='black')
circle2=plt.Circle((27.0,1.0),0.1, color='white', zorder=1.1)
plt.gcf().gca().add_artist(circle1)
plt.gcf().gca().add_artist(circle2)

plt.xlim(0,tam[0].value)
plt.ylim(0,tam[1].value)

#fig = plt.gcf()
fig.set_size_inches(tam[0].to(u.imperial.inch).value, tam[1].to(u.imperial.inch).value)
fig.savefig('Fundo.png', format='png', transparent=True)
