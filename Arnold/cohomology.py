import numpy as np
import itertools as it
from alg_tools import *


fin = open("Im0.txt", "r")
a = []
m = 0
n = 0
for line in fin:
    m += 1
    row = []
    for i in line.split():
        row.append(int(i))
    n = len(row)
    a.append(row)
fin.close()

glav_per = Gauss(a, m, n)
cnt = 0
p = 1
fin = open("Ker1.txt", "r")
out = open("H1.txt","w")
for line in fin:
    row = []
    for i in line.split():
        row.append(int(i))
    a.append(row)
    m += 1
    cnt += 1
    p = 1
    FastGauss(a, m, n, glav_per)
    for i in range(n):
        if a[m-1][i]:
            if p:
                glav_per.append(i)
                p = 0
    if p:
        a.pop()
        m -= 1
        cnt -= 1
    else:
        for i in range(n):
            print(a[m-1][i], end=' ', file=out)
        print(file=out)
print(cnt)
fin.close()
out.close()

fin = open("Im1.txt", "r")
a = []
m = 0
n = 0
for line in fin:
    m += 1
    row = []
    for i in line.split():
        row.append(int(i))
    n = len(row)
    a.append(row)
fin.close()

glav_per = Gauss(a, m, n)
cnt = 0
p = 1
fin = open("Ker2.txt", "r")
out = open("H2.txt","w")
for line in fin:
    row = []
    for i in line.split():
        row.append(int(i))
    a.append(row)
    m += 1
    cnt += 1
    p = 1
    FastGauss(a, m, n, glav_per)
    for i in range(n):
        if a[m-1][i]:
            if p:
                glav_per.append(i)
                p = 0
    if p:
        a.pop()
        m -= 1
        cnt -= 1
    else:
        for i in range(n):
            print(a[m-1][i], end=' ', file=out)
        print(file=out)
print(cnt)
fin.close()
out.close()


fin = open("Im2.txt", "r")
a = []
m = 0
n = 0
for line in fin:
    m += 1
    row = []
    for i in line.split():
        row.append(int(i))
    n = len(row)
    a.append(row)
fin.close()

glav_per = Gauss(a, m, n)
cnt = 0
p = 1
fin = open("Ker3.txt", "r")
out = open("H3.txt","w")
for line in fin:
    row = []
    for i in line.split():
        row.append(int(i))
    a.append(row)
    m += 1
    cnt += 1
    p = 1
    FastGauss(a, m, n, glav_per)
    for i in range(n):
        if a[m-1][i]:
            if p:
                glav_per.append(i)
                p = 0
    if p:
        a.pop()
        m -= 1
        cnt -= 1
    else:
        for i in range(n):
            print(a[m-1][i], end=' ', file=out)
        print(file=out)
print(cnt)
fin.close()
out.close()
