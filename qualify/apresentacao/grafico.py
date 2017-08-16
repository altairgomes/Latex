import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))/np.sqrt(2*np.pi*np.power(sig, 2.))


tam = [28,21]*u.cm

fig = plt.figure(frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

x = np.linspace(0, 28.0, 1000)
y = np.zeros(len(x)) + 20.0 + 0.1*np.random.normal(0, 1, len(x))
y[np.where((x < 25.6) & (x > 2.4))] = y[np.where((x < 25.6) & (x > 2.4))] - 3.35

plt.plot(x, y, color='black')

plt.plot([27.0, 27.0], [0.0, 2.0], color='black', zorder=0.9)

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
fig.savefig('Fundo.png', format='png', dpi=300, transparent=True)
