import numpy as np
import matplotlib.pyplot as plt

def tail_prob(data,t):
    tail = []
    for i in range(0,len(t)):
        temp = np.count_nonzero(data-np.mean(data)>t[i])
        temp = temp*1.0/len(data)
        tail.append(temp)
    return tail

n =10 #int(input("Enter number of degrees of freedom: "))
k = 10000
t = np.linspace(0,100,1e5)
data = np.zeros((k,))


for i in range(n):
    x = np.random.normal(0,1,(k,))
    data = data + x**2

x1 = np.random.normal(0,np.sqrt(2*n),(k,))
tail_probs = np.array(tail_prob(data,t))
plt.plot(t,tail_probs,'r',label='Chi-square')
tail_probs1 = np.array(tail_prob(x1,t))
plt.plot(t,tail_probs1,'b',label='Reference Gaussian')
labels = ['Chi-square','Reference Gaussian']
plt.legend(labels)
plt.show()
