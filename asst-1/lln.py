import numpy as np 
import matplotlib.pyplot as plt 

def LLN(n,distribution):
	mu = 0
	diff = []
	for i in range(1,n+1):
		if distribution =='Gaussian':
			data = np.random.normal(mu,1.0,i)
			diff.append(np.mean(data)-mu)

		if distribution =='Laplacian':
			data = np.random.laplace(mu,1.0,i)
			diff.append(np.mean(data)-mu)

		if distribution =='Uniform':
			data = np.random.uniform(-1,1,i)
			diff.append(np.mean(data)-mu)

		if distribution == 'Exponential':
			mu = 0.9
			data = np.random.exponential(mu,i)
			diff.append(np.mean(data)-mu) 

	return np.array(diff)


n=10000

data_gaussian = LLN(n,'Gaussian')
data_exponential = LLN(n,'Exponential')
data_laplacian = LLN(n,'Laplacian')
data_uniform = LLN(n,'Uniform')

f,axs = plt.subplots(4,sharex=True)
f.suptitle('Law of Large Numbers')

axs[0].plot(data_gaussian)
axs[0].plot(np.zeros(n))
axs[0].set_title('Gaussian')
axs[1].plot(data_exponential)
axs[1].plot(np.zeros(n))
axs[1].set_title('Exponential')
axs[2].plot(data_laplacian)
axs[2].plot(np.zeros(n))
axs[2].set_title('Laplacian')
axs[3].plot(data_uniform)
axs[3].plot(np.zeros(n))
axs[3].set_title('Uniform')

plt.show()
