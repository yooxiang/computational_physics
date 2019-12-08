import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-10, 10, 1000) #time

def g(t): # g function
    return (1/np.sqrt(2*np.pi))*np.exp((-t**2)/2)

def h(t): #h function
    if t < 3:
        return 0
    if t > 5:
        return 0
    if  t >= 3 and t <= 5:
        return 4

h_discrete = [] # list of discrete values of h
for i in range(len(t)):
    h_discrete.append(h(t[i]))
    
g_discrete = g(t) #list of discrete values of g


hf = np.fft.fft(np.fft.fftshift(h_discrete)) #discrete fourier transform of h, and shifted
gf = np.fft.fft(np.fft.fftshift(g_discrete*0.02)) #discrete fourier transform of g, and shifted and adjusted by factor 1000/20 as given in t 


convolution = hf*gf #not yet reverse transform of product of tranformed pair
convolutionf = np.fft.ifftshift(np.fft.ifft(convolution)) #shifted and reverse transformed convolution

plt.plot(t, abs(convolutionf), label = 'convolution')
plt.plot(t,g(t), label = 'g(t)')
plt.plot(t,h_discrete, label = 'h(t)')
plt.legend()
plt.xlabel("time")