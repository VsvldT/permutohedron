import numpy as np
from sympy.combinatorics.permutations import Permutation

m = 4


def nozero(a):
    return [x for x in a if x != 0]

def shift(perm):
    return [x-1 for x in perm]

def rsgn(c_E):
    return (-1)**((sum(len(x)**2 for x in c_E)- m) // 2)

def sgn_1(r_A, p):
    #p = len(r_A)
    buf = []
    for i in r_A:
        buf += i
    psgn = Permutation(shift(buf)).signature()
    if p <= 1:
        return psgn
    return psgn * (-1)**( sum( (i+1) * len(r_A[p-i-2]) for i in range(p-1)) )

def sgn_2(r_A, p):
    #p = len(r_A)
    return (-1)**(((p-1)*(p-2))//2) * sgn_1(r_A, p)

def csgn(q, p, c_E, r_E, c_A, r_A):
    return (-1)**((q * (q - 1))//2) * rsgn(c_E) * sgn_1(r_A, q) * sgn_2(c_E, p) * sgn_2(c_A, p)


#tuturuu = [[2, 3], [1, 4]]
#print("sgn_1(tuturuu) = ", sgn_1(tuturuu))


fin = open("matrices.txt", "r")
fout = open("output.txt", "w")

row = []

for line in fin:
    row = line.split()
    q = int(row[0])
    p = m + 1 - q
    
    E = []
    for i in range(q):
        E.append([])
        for j in range(p):
            E[i].append(int(row[1 + p*i + j]))
    E = np.array(E)
    r_E = []
    for i in range(q):
        r_E.append(nozero(E[q-1-i, :]))
    c_E = []
    for i in range(p):
        c_E.append(nozero(E[:, i]))
    print("c_E = ", c_E)
    print("r_E = ", r_E)
    
    A = []
    for i in range(q):
        A.append([])
        for j in range(p):
            A[i].append(int(row[1 + q*p + p*i + j]))
    A = np.array(A)
    r_A = []
    for i in range(q):
        r_A.append(nozero(A[q-1-i, :]))
    c_A = []
    for i in range(p):
        c_A.append(nozero(A[:, i]))
    print("c_A = ", c_A)
    print("r_A = ", r_A)
    
    print("csgn = ", csgn(q, p, c_E, r_E, c_A, r_A))
    
    #sigma = Permutation(shift(r))
    #print(sigma.signature())
fin.close()
fout.close()