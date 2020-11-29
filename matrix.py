
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers


#function to generate matrices of size nxn
def matrix(n):
    
    matrix = []
    i=0
    j=0
    while(i!=n):
        lst = [0]
        j=0
        while(j!=n-1):
            m = randint(1,15)
            if (m != 0): 
                lst.append(m)
            else:
                j-=1
            j+=1
        i+=1
        matrix.append(lst)
    return matrix

print(matrix(15))
    
    
