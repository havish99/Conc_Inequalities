import numpy as np
import matplotlib.pyplot as plt

def tail_prob(data,t):
    tail = []
    for i in range(0,len(t)):
        temp = np.count_nonzero(data-np.mean(data)>t[i])
        temp = temp*1.0/len(data)
        tail.append(temp)
    return tail

n = 10 # summation length
a = 1 # interval bounds
k = 10000 # number of samples at a time
t = np.linspace(0,10,1e4)
data = np.zeros((k,))


for i in range(n):
    x = np.random.uniform(-a,a,(k,))
    data = data + x

x1 = np.random.normal(0,np.sqrt(8),(k,))
tail_probs = np.array(tail_prob(data,t))
plt.plot(tail_probs,'r',label='Custom Distribution')
tail_probs1 = np.array(tail_prob(x1,t))
plt.plot(tail_probs1,'b',label='Reference Gaussian')
labels = ['Custom Distribution','Reference Gaussian']
plt.legend(labels)
plt.show()
