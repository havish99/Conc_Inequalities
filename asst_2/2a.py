import numpy as np
import matplotlib.pyplot as plt

def tail_prob(data,t):
    tail = []
    for i in range(0,len(t)):
        temp = np.count_nonzero(data-np.mean(data)>t[i])
        temp = temp*1.0/len(data)
        tail.append(temp)
    return tail

k = 10000
t = np.linspace(0,10,1e4)

stdev = 1
data = np.random.normal(0,stdev,(k,))

x1 = np.random.normal(0,stdev+2,(k,)) ### the reference gaussian is taken to have 10 times the standard deviation

tail_probs = np.array(tail_prob(data,t))
plt.plot(tail_probs,'r',label='Sample Gaussian')
tail_probs1 = np.array(tail_prob(x1,t))
plt.plot(tail_probs1,'b',label='Reference Gaussian')
labels = ['Sample Gaussian','Reference Gaussian']
plt.legend(labels)
plt.show()
