for i in a:
    n, ra, dec = np.loadtxt(i, usecols=[31,28,29], unpack=True)
    print '{:45s}'.format(i), '{:3.0f} & {:3.0f}$\pm${:3.0f} & {:3.0f}$\pm${:3.0f}'.format(n.mean(), ra.mean()*1000, ra.std()*1000, dec.mean()*1000, dec.std()*1000)
    
def ret(s):
    ra, dec = np.array([]), np.array([])
    for i in a:
        if s in i:
            x, y = np.loadtxt(i, usecols=[0,1], unpack=True)
            ra = np.hstack((ra,x))
            dec = np.hstack((dec,y))
    print '{:10s}'.format(s), '{} & {:3.0f}$\pm${:3.0f} & {:3.0f}$\pm${:3.0f}'.format(len(ra), ra.mean()*1000, ra.std()*1000, dec.mean()*1000, dec.std()*1000)