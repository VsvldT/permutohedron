import itertools as it
import numpy as np

MF = [[1, 2, 3], [1, 2, 4], [1, 3, 5], [2, 3, 6], [2, 4, 5], [3, 4, 5], [1, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6]]

def diff(arr, dim):
    lst = []
    for i in range(6-dim - 1):
        p = 1
        term = []
        for j in range(i):
            term.append(arr[j])
        mult = arr[i] + arr[i+1]
        mult.sort()
        if(len(mult) > 3) or (mult in MF):
            p = 0
        term.append(mult)
        
        for j in range(6 - dim - i - 2):
            term.append(arr[j+i+2])
        if p:
            lst.append(term)
    return lst

def c_complex():
    perm = it.permutations([1,2,3,4,5,6])
    c = []
    for i in range(4):
        c.append([])
    
    for sigma in perm:
        tau = list(sigma)
        for razb in it.combinations([1,2,3,4,5], 2):
            t1 = tau[:razb[0]]
            t2 = tau[razb[0]:razb[1]]
            t3 = tau[razb[1]:]
            #print(t1, t2, t3)
            t1.sort()
            t2.sort()
            t3.sort()
            if(max(len(t1), len(t2), len(t3)) < 4) and (not ((t1 in MF) or (t2 in MF) or (t3 in MF))):
                if not([t1, t2, t3] in c[3]):
                    c[3].append([t1,t2,t3])
        for razb in it.combinations([1,2,3,4,5], 3):
            t1 = tau[:razb[0]]
            t2 = tau[razb[0]:razb[1]]
            t3 = tau[razb[1]:razb[2]]
            t4 = tau[razb[2]:]
            t1.sort()
            t2.sort()
            t3.sort()
            t4.sort()
            if(max(len(t1), len(t2), len(t3), len(t4)) < 4) and (not ((t1 in MF) or (t2 in MF) or (t3 in MF) or (t4 in MF))):
                if not( [t1, t2, t3, t4] in c[2]):
                    c[2].append([t1, t2, t3, t4])
            #i = -1
            #mx = len(t1)
            #predmx = len(t1)
            #j = -1
             
            #if(mx <= len(t2)):
            #    j = i
            #    predmx = mx
            #    i = 0
            #    mx = len(t2)
            #if(mx <= len(t3)):
            #    j = i
            #    predmx = mx
            #    i = 1
            #    mx = len(t3)
            #if(mx <= len(t4)):
            #    j = i
            #    predmx = mx
            #    i = 2
            #    mx = len(t4)
            #if(j < 0):
            #    ind2 = 0
            #else:
            #    ind2 = razb[j]
            #if(i < 0):
            #    ind1 = 0
            #else:
            #    ind1 = razb[i]
            #if((mx < 3) & (tau[ind1] < tau[ind1+1]) & (tau[ind2] < tau[ind2+1]) ):
            #    c[2].append([t1,t2,t3,t4])
        for razb in it.combinations([1,2,3,4,5], 4):
            t1 = tau[:razb[0]]
            t2 = tau[razb[0]:razb[1]]
            t3 = tau[razb[1]:razb[2]]
            t4 = tau[razb[2]:razb[3]]
            t5 = tau[razb[3]:]
            t1.sort()
            t2.sort()
            t3.sort()
            t4.sort()
            t5.sort()
            if(max(len(t1), len(t2), len(t3), len(t4), len(t5)) < 4) and (not ((t1 in MF) or (t2 in MF) or (t3 in MF) or (t4 in MF) or (t5 in MF))):
                if not([t1, t2, t3, t4, t5] in c[1]):
                    c[1].append([t1, t2, t3, t4, t5])
            #i = -1
            #mx = len(t1)
            #if(mx < len(t2)):
            #    i = 0
            #    mx = len(t2)
            #if(mx < len(t3)):
            #    i = 1
            #    mx = len(t3)
            #if(mx < len(t4)):
            #    i = 2
            #    mx = len(t4)
            #if(mx < len(t5)):
            #    i = 3
            #    mx = len(t5)
            #if(i < 0):
            #    ind = 0
            #else:
            #    ind = razb[i]
            #if(tau[ind] < tau[ind+1]):
            #    c[1].append([t1,t2,t3,t4,t5])
        c[0].append([[tau[0]],[tau[1]],[tau[2]],[tau[3]],[tau[4]],[tau[5]]])
    return c

def main():
    c = c_complex()
    dd = diff([[6], [5], [4],[3], [2],[1]], 0)
    term = [[5, 6], [4],[3], [2],[1]]
    print(dd)
    
    dd = diff([[6],[5],[3,4],[1,2]], 2)
    print(dd)
    
    for j in range(4):
        print(len(c[j]))
    
    
    #a = 1
    #b = 0
    #print(a ^ b, a^a, b^b) # так в питоне пишется быстрая сумма по модулю 2
    
    d01 = []
    for i in range(len(c[0])):
        d01.append([])
        term = diff(c[0][i], 0)
        for j in range(len(c[1])):
            if(c[1][j] in term):
                d01[i].append(1)
            else:
                d01[i].append(0)
    
    #for i in range(10):
    #    for j in range(10):
    #        print(d01[i][j], end=' ')
    #    print()
    
    d12 = []
    for i in range(len(c[1])):
        d12.append([])
        term = diff(c[1][i], 1)
        for j in range(len(c[2])):
            if(c[2][j] in term):
                d12[i].append(1)
                #print(c[1][j], term, sep=' ')
            else:
                d12[i].append(0)
    
    d23 = []
    for i in range(len(c[2])):
        d23.append([])
        term = diff(c[2][i], 2)
        for j in range(len(c[3])):
            if(c[3][j] in term):
                d23[i].append(1)
                #print(c[1][j], term, sep=' ')
            else:
                d23[i].append(0)
    
    f01 = open("d01.txt", "w")
    #b = Gauss(d01,len(c[0]), len(c[1]))
    b = []
    for i in range(len(c[1])):
        b.append([])
        for j in range(len(c[0])):
            b[i].append(d01[j][i])
    
    for i in range(len(c[1])):
        for j in range(len(c[0])):
            print(b[i][j], end=' ', file=f01)
        print(file=f01)
    
    f01.close()
    
    
    f12 = open("d12.txt", "w")
    #b = Gauss(d12,len(c[1]), len(c[2]))
    
    b = []
    for i in range(len(c[2])):
        b.append([])
        for j in range(len(c[1])):
            b[i].append(d12[j][i])
    
    for i in range(len(c[2])):
        for j in range(len(c[1])):
            print(b[i][j], end=' ', file=f12)
        print(file=f12)
    f12.close()
    
    
    f23 = open("d23.txt", "w")
    #b = Gauss(d23,len(c[2]), len(c[3]))
    
    b = []
    for i in range(len(c[3])):
        b.append([])
        for j in range(len(c[2])):
            b[i].append(d23[j][i])
    
    for i in range(len(c[3])):
        for j in range(len(c[2])):
            print(b[i][j], end=' ', file=f23)
        print(file=f23)
    
    f23.close()
    
    print(len(c[0]), len(c[1]), len(c[2]), len(c[3])) 

