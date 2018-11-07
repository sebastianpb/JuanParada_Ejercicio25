import numpy as np
import matplotlib.pyplot as plt


data = np.fromfile('sample.dat', dtype=float)

mu=data.mean()
sigma=data.std()
def f(x,mu,sigma):
    c=(1.0/(sigma*np.sqrt(2*np.pi)))
    return  c* np.exp(-0.5*((x-mu)/sigma)**2)
x=np.linspace(mu-4*sigma,mu+4*sigma,100)
plt.plot(x,f(x,mu,sigma))
_=plt.hist(data)
plt.savefig("sample.pdf")