import itertools as it
import numpy as np
from alg_tools import *


def main():
    c = c_complex()

    d0 = []
    for i in range(len(c[0])):
        d0.append([])
        term = diff(c[0][i], 0)
        for j in range(len(c[1])):
            if(c[1][j] in term):
                d0[i].append(1)
            else:
                d0[i].append(0)
    
    d1 = []
    for i in range(len(c[1])):
        d1.append([])
        term = diff(c[1][i], 1)
        for j in range(len(c[2])):
            if(c[2][j] in term):
                d1[i].append(1)
            else:
                d1[i].append(0)
    
    d2 = []
    for i in range(len(c[2])):
        d2.append([])
        term = diff(c[2][i], 2)
        for j in range(len(c[3])):
            if(c[3][j] in term):
                d2[i].append(1)
            else:
                d2[i].append(0)

    d3 = []
    for i in range(len(c[3])):
        d3.append([])
        term = diff(c[3][i], 3)
        for j in range(len(c[4])):
            if(c[4][j] in term):
                d3[i].append(1)
            else:
                d3[i].append(0)

    
    file0 = open("d0.txt", "w")
    for i in range(len(c[1])):
        for j in range(len(c[0])):
            print(d0[j][i], end=' ', file=file0)
        print(file=file0)
    
    file0.close()
    
    
    file1 = open("d1.txt", "w")
    for i in range(len(c[2])):
        for j in range(len(c[1])):
            print(d1[j][i], end=' ', file=file1)
        print(file=file1)
    file1.close()
    
    
    file2 = open("d2.txt", "w")    
    for i in range(len(c[3])):
        for j in range(len(c[2])):
            print(d2[j][i], end=' ', file=file2)
        print(file=file2)
    file2.close()

    file3 = open("d3.txt", "w")    
    for i in range(len(c[4])):
        for j in range(len(c[3])):
            print(d3[j][i], end=' ', file=file3)
        print(file=file3)
    file3.close()

    
    print(len(c[0]), len(c[1]), len(c[2]), len(c[3]), len(c[4])) 
main()
