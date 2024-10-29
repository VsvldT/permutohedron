import itertools as it
import numpy as np


def Gauss(a, m, n):
    glav_per = []
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
                glav_per.append(i+cnt)
                for j in range(m):
                    if(i != j):
                        if(a[j][i+cnt]):
                            for k in range(n-i-cnt):
                                a[j][k+i+cnt] = a[j][k+i+cnt]^a[i][k+i+cnt]
    print(len(glav_per))
    return glav_per
def main():
    f01 = open("d01.txt", "r")
    len0 = 720
    len1 = 1800
    a = []
    b = []
    for line in f01:
        row = []
        row_b = []
        for j in line.split():
            row.append(int(j))
            row_b.append(int(j))
        a.append(row)
        b.append(row_b)
    f01.close()

    glav_per_0 = Gauss(a, len1, len0)
    Ker_0 = []
    Im_0 = []
    for i in range(len0):
        if not(i in glav_per_0):
            v = [0] * len0
            v[i] = 1
            for j in range(len(glav_per_0)):
                v[glav_per_0[j]] = a[j][i]
            Ker_0.append(v)
        else:
            v = [0] * len1
            for j in range(len1):
                v[j] = b[j][i]
            Im_0.append(v)

    out = open("Ker0.txt", "w")
    for i in range(len0 - len(glav_per_0)):
        for j in range(len0):
            print(Ker_0[i][j], file=out, end=' ')
        print(file=out)
    out.close()
    
    out = open("Im0.txt", "w")
    for i in range(len(glav_per_0)):
        for j in range(len1):
            print(Im_0[i][j], file=out, end=' ')
        print(file=out)
    out.close()
    
    
    f12 = open("d12.txt", "r")
    len1 = 1800
    len2 = 1080
    a = []
    b = []
    for line in f12:
        row = []
        row_b = []
        for j in line.split():
            row.append(int(j))
            row_b.append(int(j))
        a.append(row)
        b.append(row_b)
    f12.close()
    
    
    glav_per_1 = Gauss(a, len2, len1)
    Ker_1 = []
    Im_1 = []
    for i in range(len1):
        if not(i in glav_per_1):
            v = [0] * len1
            v[i] = 1
            for j in range(len(glav_per_1)):
                v[glav_per_1[j]] = a[j][i]
            Ker_1.append(v)
        else:
            v = [0] * len2
            u = [0] * len1
            u[i] = 1
            for j in range(len2):
                v[j] = b[j][i]
            Im_1.append(v)
    
    out = open("Ker1.txt", "w")
    for i in range(len1 - len(glav_per_1)):
        for j in range(len1):
            print(Ker_1[i][j], file=out, end=' ')
        print(file=out)
    out.close()
    
    out = open("Im1.txt", "w")
    for i in range(len(glav_per_1)):
        for j in range(len2):
            print(Im_1[i][j], file=out, end=' ')
        print(file=out)
    out.close()
    
    
    f23 = open("d23.txt", "r")
    len3 = 90
    len2 = 1080
    a = []
    b = []
    for line in f23:
        row = []
        row_b = []
        for j in line.split():
            row.append(int(j))
            row_b.append(int(j))
        a.append(row)
        b.append(row_b)
    f23.close()
    
    glav_per_2 = Gauss(a, len3, len2)
    Ker_2 = []
    Im_2 = []
    for i in range(len2):
        if not(i in glav_per_2):
            v = [0] * len2
            v[i] = 1
            for j in range(len(glav_per_2)):
                v[glav_per_2[j]] = a[j][i]
            Ker_2.append(v)
        else:
            v = [0] * len3
            u = [0] * len2
            u[i] = 1
            for j in range(len3):
                v[j] = b[j][i]
            Im_2.append(v)
    
    out = open("Ker2.txt", "w")
    for i in range(len2 - len(glav_per_2)):
        for j in range(len2):
            print(Ker_2[i][j], file=out, end=' ')
        print(file=out)
    out.close()
    
    out = open("Im2.txt", "w")
    for i in range(len(glav_per_2)):
        for j in range(len3):
            print(Im_2[i][j], file=out, end=' ')
        print(file=out)
    out.close()

