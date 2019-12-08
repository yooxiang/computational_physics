import numpy as np
def Decomposition(M):
    Length = len(M) #length of the matrix entered
    Lower=np.zeros([len(M[0]),len(M)]) #create lower matrix with 0s
    Upper=np.zeros([len(M[0]),len(M)]) #same for the upper matrix
    
    for j in range (Length): #two for loops to interate through the elements of L and U
        sum_Upper = 0.0 #variables to store the sum as given in the formula
        sum_Lower = 0.0
        
        for i in range(j+1): #go through each row element for the Upper matrix
            sum_Upper = 0.0
            for k in range(i): #loop for the sum
        
                sum_Upper = sum_Upper + Lower[i][k]*Upper[k][j] 
          
            Upper[i][j] = M[i][j] - sum_Upper #calculation of each upper element
      
        for i in range(j,Length): #iterate through each row for the lower element
            if j == i:
                Lower[i][j] = 1 #set the diaganol to 0
            else:
                    for k in range(j):
                        sum_Lower = sum_Lower + Lower[i][k]*Upper[k][j]
                    Lower[i][j] = ((Upper[j][j])**-1)*(M[i][j]-sum_Lower)
                  
    return Lower, Upper #function returns the lower and then the upper matrix

def combine(M): #combine the lower and upper for form asked in question
    Lower = Decomposition(M)[0]
    Upper = Decomposition(M)[1]
    Length= len(Lower)

    return_matrix = np.zeros((Length,Length)) #combine the lower and upper for form asked in question

    for j in range(Length):
       
        for i in range(j, Length): #loop to take elements from lower
           
            return_matrix[i][j] = Lower[i][j]
         
        for i in range(j+1): #loop to take elements from upper
            return_matrix[i][j] = Upper[i][j]
            
    return return_matrix #returns desired form
        
            
    

def Determinant(M): #determinant function
    L,U = Decomposition(M)
    det = 1 #reset to 0
    print("asdf a asdfasdfa",U)
    for j in range(len(U)):
       
        det = det * U[j][j] #calcualtion of determinant 
    return det



def solve(M, b):
    L = Decomposition(M)[0]
    U = Decomposition(M)[1]
    y = np.zeros([len(M[0])]) #set y equal to list array of 0s
    y[0] = b[0]/L[0][0] #work out 0th element
    for i in range(1, len(b)):
        Sum=0
        for k in range(i):
           
            Sum = Sum +L[i][k]*y[k]
        y[i] = (1/L[i][i])*(b[i] - Sum) #forward subsitution

    x = np.zeros([len(M[0])]) #back substition
    for i in range(len(b)-1, -1, -1):
        Sum = 0
        for k in range(i+1, len(b)):
            Sum = Sum + U[i][k]*x[k]
        x[i] = (1/U[i][i])*(y[i] - Sum)
    return x #returns solution

def invert(M):
    b = np.zeros([len(M[0]),len(M)]) #creates matrix of length M with zeros
    inverse = []
    for i in range(len(b)):
        b[i][i] = 1 #set all the diagalnosl to 0 
        
    for i in range(len(b)):
        column = solve(M, b[i]) #pick out a column to solve for the inverse row by row
        inverse.append(column) #apppend the result into a column
        
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            inverse[i][j],inverse[j][i] = inverse[j][i],inverse[i][j] #switch over the rows and columns
            
    return inverse

    
A=[[3,1,0,0,0],[3,9,4,0,0],[0,9,20,10,0],[0,0,-22,31,-25],[0,0,0,-55,61]] #as given in the question
b = [2, 5, -4, 8, 9]
x = solve(A, b)
print("combined lower and upper matrix is", combine(A))
print("lower matrix is", Decomposition(A)[0], "upper matrix is", Decomposition(A)[1])
print("determinant is", Determinant(A))
print("x is ", solve(A,b))
print("inversion is ", invert(A))


    