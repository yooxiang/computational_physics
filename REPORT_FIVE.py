import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) #keep the seed the same
Random_Numbers = np.random.rand(100000) #generate all the numbers


def trans(x):
    return 2*np.arcsin(x) #invereted function that will give the correct pdf


x = np.random.rand(100000) #generate all the numbers
x_plot = np.linspace(0,3.1,100)


t =[]

def pdf(x):
    return (2/np.pi)*((np.cos(x/2))**2) #required pdf
counter = 0
loop_n = 0
while counter <100000:
    loop_n = loop_n + 1
    y = trans(np.random.rand())
    p = np.random.rand()*(2/np.pi)*np.cos(y/2) #comparioson functinon
    if p < pdf(y):
        t.append(y)
        counter = counter +1

#%%
plt.figure()
plt.title("question a histogram")
plt.hist(Random_Numbers,rwidth=0.9,bins=np.linspace(0,1,20)) #plot a
plt.xlabel("value")
plt.ylabel("frequencyr")

#%%
plt.figure()
plt.title("question b histogram")
plt.hist(trans(Random_Numbers),rwidth = 1, bins = 600) #plot b
plt.xlabel("bin")
plt.ylabel("frequency")
plt.plot(x_plot,np.cos(x_plot/2)*250, label = 'pdf')
plt.legend()

#%% plot c
plt.figure()
plt.title("question c histogram")
plt.hist(t,bins=200)
plt.xlabel("value")#plot c
plt.ylabel("frequency")
plt.plot(x_plot,1000*np.cos(x_plot/2)**2, label = 'pdf')
plt.plot(x_plot,np.cos(x_plot/2)*800, label = 'comparison function')

plt.legend()

plt.show()
print("ratio of time taken is ", counter/loop_n)