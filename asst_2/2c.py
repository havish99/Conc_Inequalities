import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def tail_prob(data,t):
    tail = []
    for i in range(0,len(t)):
        temp = np.count_nonzero(data-np.mean(data)>t[i])
        temp = temp*1.0/len(data)
        tail.append(temp)
    return tail

b = 1
k = 10000
t = np.linspace(0,10,1e4)

data = np.random.laplace(0,b,(k,))

x1 = np.random.normal(0,np.sqrt(2)*b,(k,)) ### the reference gaussian is taken to have 10 times the standard deviation

tail_probs = np.array(tail_prob(data,t))
plt.plot(tail_probs,'r',label='laplacian')
tail_probs1 = np.array(tail_prob(x1,t))
plt.plot(tail_probs1,'b',label='Reference Gaussian')
labels = ['laplacian','Reference Gaussian']
plt.legend(labels)
plt.show()
