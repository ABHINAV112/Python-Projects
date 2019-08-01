from sys import argv
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end='')
        print()
def empty_matrix(n):
    return [[' ' for i in range(n)] for i in range(n)]
        
def A(n):
    A_matrix=empty_matrix(n)
    if n%2==1:
        mid=(n-1)//2
        for i in range(n):
            for j in range(n):
                if i==0:
                    if mid==j:
                        A_matrix[i][j]='A'
                    
                
                if 1<=i<=mid:
                    if j+i == mid or j-i == mid:
                        A_matrix[i][j]='A'

                    
                    
                if i== mid+1:
                    A_matrix[i][j]='A'
                if i > mid+1:
                    if j==0 or j==n-1:
                        A_matrix[i][j]='A'
    else:
        mid1=n//2-1
        mid2=mid1+1
        for i in range(n):
            for j in range(n):
                if i==0:
                    if mid1==j or mid2==j:
                        A_matrix[i][j]='A'
                    

                if 1<=i<=mid1:
                    if j+i==mid1 or j-i==mid2:
                        A_matrix[i][j]='A'
                  

                if i==mid2:
                    A_matrix[i][j]='A'

                if i > mid2:
                    if j==0 or j==n-1:
                        A_matrix[i][j]='A'
                    

    return A_matrix


def B(n):
    B_matrix=empty_matrix(n)
    mid= (n-1)//2
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or i==mid:
                if j!=n-1:
                    B_matrix[i][j]='B'
                

            else:
                if j==0 or j==n-1:
                    B_matrix[i][j]='B'
            
    return B_matrix


def C(n):
    C_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                if j!=0:
                    C_matrix[i][j]='C'

            elif i==1 or i==n-2:
                if j==1 or j==0:
                    C_matrix[i][j]='C'

            else:
                if j==0:
                    C_matrix[i][j]='C'
            
    return C_matrix
                    
def D(n):
    D_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                if j!=n-1:
                    D_matrix[i][j]='D'
        
            elif i==1 or i==n-2:
                if j==0 or j==n-1 or j==n-2:
                    D_matrix[i][j]='D'
                
            else:
                if j==0 or j==n-1:
                    D_matrix[i][j]='D'
            
    return D_matrix

def E(n):
    E_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or i==mid:
                E_matrix[i][j]='E'
                
            elif j==0:
                E_matrix[i][j]='E'
    return E_matrix

def F(n):
    F_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if i==0 or i==mid:
                F_matrix[i][j]='F'

            elif j==0:
                F_matrix[i][j]='F'

    return F_matrix


def G(n):
    G_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                if j!=0 and j!=n-1:
                   G_matrix[i][j]='G'
                

            elif 1<=i<mid:
                if j==0:
                    G_matrix[i][j]='G'

            elif i==mid:
                if j==0 or mid<j<=n-1:
                    G_matrix[i][j]='G'

            elif mid<i<n-1:
                if j==0 or j==n-1:
                    G_matrix[i][j]='G'
                
    return G_matrix

def H(n):
    H_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if i==mid:
                H_matrix[i][j]='H'
            elif j==0 or j==n-1:
                H_matrix[i][j]='H'
    return H_matrix

def I(n):
    I_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if j==mid:
                I_matrix[i][j]='I'

            elif i==0 or i==n-1:
                I_matrix[i][j]='I'
                
    return I_matrix

def J(n):
    J_matrix =  empty_matrix(n)
    mid=(n-1)//2+1
    for i in range(n):
        for j in range(n):
            if i==0:
                J_matrix[i][j]='J'

            elif 1<=i<mid:
                if j==mid :
                    J_matrix[i][j]='J' 

            elif mid<=i<n-1:
                if j==mid or j==0:
                    J_matrix[i][j]='J' 
            else:
                if 0<j<mid:
                    J_matrix[i][j]='J' 
    return J_matrix

def K(n):
    K_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if i<=mid:
                if j in [n-1-2*i,n-2-2*i,0]:
                    K_matrix[i][j]='K'

            elif i>=mid:
                if j in[(i-mid)*2-1,(i-mid)*2,0]:
                    K_matrix[i][j]='K'
    return K_matrix

def L(n):
    L_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if i!=n-1 and  j==0:
                L_matrix[i][j]='L' 
            elif i==n-1:
                L_matrix[i][j]='L' 
    return L_matrix

def M(n):
    M_matrix=empty_matrix(n)

    mid= (n-1)//2
    for i in range(n):
        for j in range(n):
            if i<=mid:
                if i==j or i+j==n-1 or j in [0,n-1]:
                    M_matrix[i][j]='M'

            else:
                if j in [0,n-1]:
                    M_matrix[i][j]='M'

    return M_matrix

def N(n):
    N_matrix=empty_matrix(n)
    mid= (n-1)//2
    for i in range(n):
        for j in range(n):
            
            if j in [i,0,n-1]:
                N_matrix[i][j]='N'

    return N_matrix

    
def O(n):
    O_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):

            if i in [0,n-1]:
                if not (j in [0,n-1]):
                    O_matrix[i][j]='O' 
     

            else:
                if j in [0,n-1]:
                    O_matrix[i][j]='O'
                    
    return O_matrix

def P(n):
    P_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if i in [0,mid]:
                if j!=n-1:
                    P_matrix[i][j]='P' 
            elif 0<i<mid:
                if j in [0,n-1]:
                    P_matrix[i][j]='P' 
            else:
                if j==0:
                    P_matrix[i][j]='P'
    return P_matrix

def Q(n):
    return empty_matrix(n)

def R(n):
    R_matrix=empty_matrix(n)
    mid = (n-1)//2
    for i in range(n):
        for j in range(n):
            if i==0 or i==mid:
                if j!=n-1:
                    R_matrix[i][j]='R' 
            else:
                if j==0 or j==n-1:
                    R_matrix[i][j]='R' 
    return R_matrix

def S(n):
    S_matrix=empty_matrix(n)
    mid = (n-1)//2
    for i in range(n):
        for j in range(n):
            if i in [0,n-1,mid]:
                if j!=0 and j!=n-1:
                    S_matrix[i][j]='S' 

            elif 0<i<mid:
                if j==0:
                    S_matrix[i][j]='S' 
            else:
                if j==n-1:
                    S_matrix[i][j]='S' 

    return S_matrix

def T(n):
    T_matrix=empty_matrix(n)
    mid = (n-1)//2
    for i in range(n):
        for j in range(n):
            if i==0:
                T_matrix[i][j]='T' 
            else:
                if j==mid:
                    T_matrix[i][j]='T' 
    return T_matrix

def U(n):
    U_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if i!=n-1:
                if j in [0,n-1]:
                    U_matrix[i][j]='U' 
            else:
                if not(j in [0,n-1]):
                    U_matrix[i][j]='U' 
    return U_matrix

def V(n):
    V_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if j in [i//2,n-i//2-1]:
                V_matrix[i][j]='V'
    return V_matrix

def W(n):
    W_matrix=empty_matrix(n)
    mid= (n-1)//2
    for i in range(n):
        for j in range(n):
            if i<mid:
                if j in [0,n-1]:
                    W_matrix[i][j]='W'
            elif mid<=i<n-1:
                if j in [0,mid,n-1]:
                    W_matrix[i][j]='W'
            else:
                if not(j in [0,mid,n-1]):
                    W_matrix[i][j]='W'
    return W_matrix
                    
def X(n):
    X_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if j in [i,n-i-1]:
                X_matrix[i][j]='X'
    return X_matrix

def Y(n):
    Y_matrix=empty_matrix(n)
    mid=(n-1)//2
    for i in range(n):
        for j in range(n):
            if i<=mid:
                if j in [i,n-i-1]:
                    Y_matrix[i][j]='Y'

            elif n%2==0:
                if j in [mid,mid+1]:
                    Y_matrix[i][j]='Y'

            else:
                if j == mid:
                    Y_matrix[i][j]='Y'

    return Y_matrix

def Z(n):
    Z_matrix=empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if i in [0,n-1]:
                Z_matrix[i][j]='Z'

            elif j==n-i-1:
                Z_matrix[i][j]='Z'

    return Z_matrix

def tester():
    a=list(range(ord('A'),ord('Z')+1))
    a.remove(ord('Q'))
    size=int(input())
    for i in a:
        exec('print_matrix('+chr(i)+'({}))'.format(size))
        print()


if(__name__=="__main__"):
        if(len(argv)>1):
                sentence = argv[1]
                letter_size = int(argv[2])
        else:
                sentence = input("Please enter your sentence:")
                letter_size = int(input("enter in the size of the letter"))
        sentence = sentence.upper()
        output = [ [] for i in range(letter_size) ]
        for i in sentence:
                if(i.isalpha()):
                        exec("curr_letter = {}({})".format(i,letter_size))
                else:
                        curr_letter = empty_matrix(letter_size)
                for j in range(len(curr_letter)):
                        output[j]+=curr_letter[j]+[" "]

        print_matrix(output)