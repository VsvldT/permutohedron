import itertools as it
import numpy as np
from simplicial_complex import *

#The following function calculates the differential of the generator of bar construction
def diff(bar_generator, dim):
    sum_of_terms = []
    for i in range(6 - dim - 1):
        p = 1
        term = []
        for j in range(i):
            term.append(bar_generator[j])
        product = bar_generator[i] + bar_generator[i+1]
        product.sort()
        term.append(product)
        
        for j in range(6 - dim - i - 2):
            term.append(bar_generator[j+i+2])
        if term_in_complex(term):
            sum_of_terms.append(term)
    return sum_of_terms

#The following function defines the cellular chain complex corresponding to the simplicial complex K
def c_complex():
    perm = it.permutations([1,2,3,4,5,6])
    c = []
    for i in range(5):
        c.append([])
    
    for permutation in perm:
        lst_perm = list(permutation)
        
        for partition in range(5):
            elem1 = lst_perm[:partition+1]
            elem2 = lst_perm[partition+1:]
            elem1.sort()
            elem2.sort()
            if(term_in_complex([elem1, elem2])):
                if not([elem1, elem2] in c[4]):
                    c[4].append([elem1, elem2])

        for partition in it.combinations([1,2,3,4,5], 2):
            elem1 = lst_perm[:partition[0]]
            elem2 = lst_perm[partition[0]:partition[1]]
            elem3 = lst_perm[partition[1]:]
            elem1.sort()
            elem2.sort()
            elem3.sort()
            
            if(term_in_complex([elem1, elem2, elem3])):
                if not([elem1, elem2, elem3] in c[3]):
                    c[3].append([elem1,elem2,elem3])
        for partition in it.combinations([1,2,3,4,5], 3):
            elem1 = lst_perm[:partition[0]]
            elem2 = lst_perm[partition[0]:partition[1]]
            elem3 = lst_perm[partition[1]:partition[2]]
            elem4 = lst_perm[partition[2]:]
            elem1.sort()
            elem2.sort()
            elem3.sort()
            elem4.sort()

            if(term_in_complex([elem1, elem2, elem3, elem4])):
                if not( [elem1, elem2, elem3, elem4] in c[2]):
                    c[2].append([elem1, elem2, elem3, elem4])
        for partition in it.combinations([1,2,3,4,5], 4):
            elem1 = lst_perm[:partition[0]]
            elem2 = lst_perm[partition[0]:partition[1]]
            elem3 = lst_perm[partition[1]:partition[2]]
            elem4 = lst_perm[partition[2]:partition[3]]
            elem5 = lst_perm[partition[3]:]
            elem1.sort()
            elem2.sort()
            elem3.sort()
            elem4.sort()
            elem5.sort()

            if(term_in_complex([elem1, elem2, elem3, elem4, elem5])):
                if not([elem1, elem2, elem3, elem4, elem5] in c[1]):
                    c[1].append([elem1, elem2, elem3, elem4, elem5])
        c[0].append([[lst_perm[0]],[lst_perm[1]],[lst_perm[2]],[lst_perm[3]],[lst_perm[4]],[lst_perm[5]]])
    return c

def Gauss(a, m, n):
    lead_coef = []
    minim = min(m, n)
    cnt = 0
    buf = 0
    for i in range(minim):
        if(i + cnt > n):
            break
        if(not a[i][i+cnt]):
            while (i+cnt < n): #& (not a[i][i+cnt]):
                if(a[i][i+cnt]):
                    break
                for j in range(m-i-1):
                    if(a[j+i+1][i+cnt]):
                        for k in range(n-i-cnt):
                            buf = a[j+i+1][k+i+cnt]
                            a[j+i+1][k+i+cnt] = a[i][k+i+cnt]
                            a[i][k+i+cnt] = buf
                        break
                if(not a[i][i+cnt]):
                    cnt += 1
        if(i+cnt < n): # & (a[i][i+cnt])):
            if(a[i][i+cnt]):
                lead_coef.append(i+cnt)
                for j in range(m):
                    if(i != j):
                        if(a[j][i+cnt]):
                            for k in range(n-i-cnt):
                                a[j][k+i+cnt] = a[j][k+i+cnt]^a[i][k+i+cnt]
    return lead_coef

def FastGauss(a, m, n, glav_per):
    for i in range(len(glav_per)):
        if a[m-1][glav_per[i]]:
            for j in range(n-glav_per[i]):
                a[m-1][j+glav_per[i]] = a[m-1][j+glav_per[i]] ^ a[i][j+glav_per[i]]


def sublist(sub, lst):
    return str(sub).strip('[]') in str(lst).strip('[]')

# 12 x 1|2 = 12
# 2|1 x 12 = 12
# 1|2|3 x 123 = 123
# 123 x 3|2|1 = 123
# 1|23 x 13|2 = 123
# 2|13 x 23|1 = 123
# 13|2 x 3|12 = 123
# 12|3 x 2|13 = 123
## 1|23 x 3|12 = 123
## 12|3 x 23|1 = 123
def mult(a, b):
    n = len(a)
    m = len(b)
    cnta = 0
    cntb = 0
    res = []
    p = 0
    maxim = max(n, m)
    for i in range(maxim):
        j = i + cnta
        k = i + cntb

        if((i + cnta >= n) or (i + cntb >= m)):
            if((i + cnta < n) or (i + cntb < m)):
                return 0
            else:
                break

        if a[j] == b[k]:
            if (len(a[j]) == 1):
                res.append(a[j])
                continue
            else:
                return 0

        if (len(a[j]) == 1) and (len(a[j+1]) == 1) and (len(b[k]) == 2):
            if (a[j][0] == b[k][0]) and (a[j+1][0] == b[k][1]):
                res.append(b[k])
                cnta += 1
                continue
            else:
                return 0
        if (len(b[k]) == 1) and (len(b[k+1]) == 1) and (len(a[j]) == 2):
            if (b[k][0] == a[j][1]) and (b[k+1][0] == a[j][0]):
                res.append(a[j])
                cntb += 1
                continue
            else:
                return 0
        

        if (len(a[j]) == 1) and (len(a[j+1]) == 2) and (len(b[k]) == 2) and (len(b[k+1]) == 1):
            if (a[j][0] == b[k][0]) and (a[j+1][0] == b[k+1][0]) and (a[j+1][1] == b[k][1]) and (a[j+1][1] > a[j][0]):
                temp = [a[j][0], a[j+1][0], a[j+1][1]]
                temp.sort()
                res.append(temp)
                cnta += 1
                cntb += 1
                continue
            else:
                return 0

        if (len(a[j]) == 2) and (len(a[j+1]) == 1) and (len(b[k]) == 1) and (len(b[k+1]) == 2):
            if (a[j][0] == b[k+1][0]) and (a[j][1] == b[k][0]) and (a[j+1][0] == b[k+1][1]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j][1], a[j+1][0]]
                temp.sort()
                res.append(temp) 
                cnta += 1
                cntb += 1
                continue
            else:
                return 0

        if (len(a[j]) == 1) and (len(a[j+1]) == 2) and (len(b[k]) == 1) and (len(b[k+1]) == 2):
            if (a[j][0] == b[k+1][0]) and (a[j+1][0] == b[k+1][1]) and (a[j+1][1] == b[k+1][0]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j+1][0], a[j+1][1]]
                temp.sort()
                res.append(temp)
                cnta += 1
                cntb += 1
                continue
            else:
                return 0

        if (len(a[j]) == 2) and (len(a[j+1]) == 1) and (len(b[k]) == 2) and (len(b[k+1]) == 1):
            if (a[j][0] == b[k+1][0]) and (a[j][1] == b[k][0]) and (a[j+1][0] == b[k][1]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j][1], a[j+1][0]]
                temp.sort()

                res.append(temp)
                cnta += 1
                cntb += 1
                continue
            else:
                return 0
        
        else:
            if (j+2 >= n) or (k+2 >= m):
                return 0
        
        if (len(a[j]) == 1) and (len(a[j+1]) == 1) and (len(a[j+2]) == 1) and (len(b[k]) == 3):
            if(a[j][0] == b[k][0]) and (a[j+1][0] == b[k][1]) and (a[j+2][0] == b[k][2]):
                res.append(b[k])
                cnta += 2
                continue
            else:
                return 0
        if (len(b[k]) == 1) and (len(b[k+1]) == 1) and (len(b[k+2]) == 1) and (len(a[j]) == 3):
            if(b[k][0] == a[j][2]) and (b[k+1][0] == a[j][1]) and (b[k+2][0] == a[j][0]):
                res.append(a[j])
                cntb += 2
                continue
            else:
                return 0
        else:
            return 0
    if(term_in_complex(res)):
        return res
    return 0


