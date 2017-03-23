import numpy as np
import pylab as pl
mu, sigma = 100, 15
data = np.loadtxt('output.txt')

# plot the first column as x, and second column as y
pl.plot(data[:,0], data[:,1], 'ro')
pl.xlabel('x')
pl.ylabel('y')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
pl.hist(data, histtype='stepfilled')
pl.show()
