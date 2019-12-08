import scipy as sp
import matplotlib.pyplot as plt
from REPORT_TWO import solve

def Linear_Interpolation(x,x_data,y_data):
    f = sp.zeros(len(x)) #empty list for new y values
    for k in range(len(x)): #goes through each x point
        ind=0
        for i in range(len(x_data)-1): #function to decide which x_data value it belongs to
            if (x[k] >= x_data[i]) & (x[k] <= x_data[i+1]): 
                ind = i
        f[k] = (((x_data[ind+1]-x[k])*y_data[ind]) + ((x[k] - x_data[ind])*y_data[ind+1]))/(x_data[ind+1]-x_data[ind]) #works out y from forumula given
    return f #returns list of new y

'''
below is list of functions for the cubic spline code
it is contained oustide the function to make the code more readable
'''

def A(x,i,j):
    return (x[i]-x[j])/3

def B(x, i, j):
    return (x[i]-x[j])/6

def F(x, y, i, j):
    return (y[i]-y[j])/(x[i]-x[j])
  
def A2(x,i,k):
    return (x_given[i+1]-x[k])/(x_given[i+1]-x_given[i])
    
def B2(x,i,k):
    return (x[k]-x_given[i])/(x_given[i+1]-x_given[i]) 
    
def C(x,i,k):
    return (1/6)*(A2(x,i,k)**3 - A2(x,i,k))*(x_given[i+1]-x_given[i])**2
    
def D(x,i,k):
    return (1/6)*(B2(x,i,k)**3 - B2(x,i,k))*(x_given[i+1]-x_given[i])**2
    
def cubic(x, x_data, y_data):
    M = sp.zeros([len(x_data)-2,len(x_data)-2]) #matrix to store coefficents to solve for derivatives
    f = sp.zeros(len(x)) #matrix to store new y values
    b = sp.zeros(len(x_data)-2) #derivatives
    for i in range(len(x_data)-2):
        M[i][i] = A(x_data,i+2, i) #fills matrix dialanols
        if i+1 < 0: #ensure fills in within correct bounds of matrix
            M[i][i+1] = B(x_data, i+2, i+1)
        if i -1 > 0:#ensure fills in within correct bounds of matrix
            M[i][i-1] = B(x_data, i+1, i)
        b[i] = F(x_data, y_data, i+2, i+1)  - F(x_data, y_data, i+1, i)
         
    derivatives = solve(M,b) #use solver from question two to solve for derivatives
   
    derivatives_shifted = sp.zeros(11)# derivatives only contain 9, need to add 0s to make it natual spline
    derivatives_shifted[1:10] = derivatives
    derivatives_shifted[0]= 0
    derivatives_shifted[10] =0
    for k in range(len(x)): #deciding the index, as done for the linear 
        for i in range(len(x_data)-1):
            if (x[k] >= x_data[i]) & (x[k] <= x_data[i+1]): 
                ind = i
        f[k] = y_data[ind]*A2(x, ind, k)+ y_data[ind+1]*B2(x,ind,k) + C(x,ind,k)*derivatives_shifted[ind] + D(x,ind,k)*derivatives_shifted[ind+1]
    return f #returns the y values


x_given= sp.array([-2.1,-1.45,-1.3,-0.2,0.1,0.15,0.9,1.1,1.5,2.8,3.8]) #data given in the question 
y_given = sp.array([0.012155,0.122151,0.184520,0.960789,0.990050,0.977751,0.422383,0.298197,0.105399,3.936690e-4,5.355348e-7])

x = sp.linspace(min(x_given),max(x_given),1000)
plt.plot(x,cubic(x,x_given,y_given),'-', label = 'Cubic Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,Linear_Interpolation(x,x_given,y_given),label = 'Linear Interpolation')
plt.grid()

plt.plot(x_given,y_given,'o',label = 'Data Points')
plt.legend()
plt.savefig("3_1", dpi = 1000)
plt.savefig("four", dpi = 1000)

plt.show()

