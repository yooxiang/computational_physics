x = 1 #test variable to change
y = 2#variable to store (made not one to start the while loop)
p = -1 #starting exponent

while x !=y:
    y = 1
    x = 1
    x = x + 2**p #add small value
    p = p-1 #reducuce this number for the next interation until the floating-point accuray is reached

print("floating point accuracy for the hardware is", 2**(p+2)) #plus two since the loop takes away one extra, and it is the penultimate value needed
#%% #repeat for different precisions. 
import numpy as np
x = np.float64(1)
y = np.float64(2)
p = np.float64(-1)
while x !=y:
    y = np.float64(1)
    x = np.float64(1)
    x = x + 2**p
    p = p - np.float64(1)
    
print("floating point accuracy for the double precision is", 2**(p+2))
#%%
import numpy as np
x = np.float32(1)
y = np.float32(2)
p = np.float32(-1)
while x !=y:
    y = np.float32(1)
    x = np.float32(1)
    x = x + np.float32(2)**p

    p = p - np.float32(1)
    
print("floating point accuracy for the single precision is", 2**(p+2))
#%%
x = np.float128(1)
y = np.float128(2)
p = np.float128(-1)
while x !=y:
    y = np.float128(1)
    x = np.float128(1)
    x = x + np.float128(2)**p
    p = p- np.float128(1)

print("floating point accuarcy for extended precision is",np.float128(2)**(p+np.float128(2)))