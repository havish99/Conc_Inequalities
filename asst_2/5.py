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

def h(x):
    return (1+x)*np.log(1+x)-x

def chernoff(x,t,n):
	return np.power((0.5*(np.exp(0.5*x)+np.exp(-0.5*x))),n)*np.exp(-x*t)

n = 100
k = 10000
n1 = 10
b = n1
a = n1
p = 0.5
t = np.linspace(0,49,1e4)
data = np.zeros((k,))
for i in range(n):
    x = np.random.binomial(n1,p,(k,))
    data = data + x

v = n*n1*p*(1-p)

## the bounds
bennet_bound = np.exp(-v*h(b*t*1.0/v)/b**2)
hoeffding_bound = np.exp(-2*np.square(t)/(n*np.square(a)))
x1 = np.log((n+2*t)*1.0/(n-2*t))
chernoff_bound = chernoff(x1,t,n)

plt.plot(bennet_bound,'g',label='Bennet Bound')
plt.plot(hoeffding_bound,'b',label='Hoeffding Bound')
plt.plot(chernoff_bound,'y',label='Chernoff Bound')
labels = ['Bennet Bound', 'Hoeffding Bound','Chernoff Bound']
plt.legend(labels)
plt.show()
