import numpy as np
import matplotlib.pyplot as plt

n = 10000
k = 10000

def distribution(name):
	n = 10000
	k = 10000
	data = np.zeros((k,))
	if name == 'Uniform':
		for i in range(n):
			data += np.random.uniform(-100,100,(k,))
		data = data/n

	if name == 'Rayleigh':
		for i in range(n):
			data += np.random.rayleigh(1, (k,))
		data = data/n

	if name == 'exponential':
		for i in range(n):
			data += np.random.exponential(1, (k,))
		data = data/n

	if name == 'Laplacian':
		for i in range(n):
			data += np.random.laplace(1,2,(k,))
		data = data/n

	return data

distros = [distribution('Uniform'),distribution('Rayleigh'),distribution('exponential'),distribution('Laplacian')]

fig, ax = plt.subplots(4, 1)

for i in range(len(distros)):
    hist, bins = np.histogram(distros[i],bins=50,normed=True)
    bin_centers = (bins[1:]+bins[:-1])*0.5
    ax[i].plot(bin_centers, hist)
plt.show()