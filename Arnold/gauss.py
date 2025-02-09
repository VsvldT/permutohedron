import itertools as it
import numpy as np


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
    #print(len(lead_coef))
    return lead_coef
