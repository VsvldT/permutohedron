from alg_tools import *

def cycle_in_H2(cycle):
    print()
    print("CYCLE:", cycle, sep='\n')
    print()
#1 = H2[0], 2 = H2[1], 3 = H2[0] + H2[1]
    if sublist(H2[0], cycle):
        return 1
    if sublist(H2[1], cycle):
        return 2
    if sublist(H2[2], cycle):
        return 3
    return 0

c = c_complex()
fin = open("H2.txt", "r")
b_2 = 0
len2 = 0
a = []
for line in fin:
    row = []
    for i in  line.split():
        row.append(int(i))
    b_2 += 1
    len2 = len(row)
    a.append(row)
H2 = []
print(b_2, len2)
for i in range(b_2):
    rs = []
    for j in range(len2):
        if(a[i][j]):
            rs.append(c[2][j])
    H2.append(rs)
rs = []
for j in range(len2):
    if(a[0][j] + a[1][j]):
        rs.append(c[2][j])
H2.append(rs)

fin.close()
for i in range(b_2):
    print(H2[i])
fin = open("H1.txt", "r")
b_1 = 0
len1 = 0
a = []
for line in fin:
    row = []
    for i in line.split():
        row.append(int(i))
    b_1 += 1
    len1 = len(row)
    a.append(row)
fin.close()
print(b_1, len1)

#print(mult([[1], [2, 3], [4], [5, 6]], [[1], [3], [2], [4, 6], [5]]))

tablica = []
for i in range(b_1):
    tablica.append([0]*b_1)


q = 1
for i in range(b_1):
    for j in range(b_1):
        res_ij = []
        nenul_1 = []
        nenul_2 = []
        res_koord = []
        for k in range(len1):
            if(a[i][k]):
                nenul_1.append(k)
            if(a[j][k]):
                nenul_2.append(k)
        for k in nenul_1:
            for l in nenul_2:
                r = mult(c[1][k], c[1][l])
                if r and q:
                    q = 0
                    print(c[1][k], "U", c[1][l], "=", r, sep=' ')
                if r:
                    if r in res_ij:
                        res_ij.remove(r)
                    else:
                        res_ij.append(r)
        if cycle_in_H2(res_ij):
            print("u_", i, " U ", "u_", j, " = ", cycle_in_H2(res_ij), sep='')
            tablica[i][j] = cycle_in_H2(res_ij)
fout = open("tablica.txt", "w")
for i in range(b_1):
    for j in range(b_1):
        print(tablica[i][j], end=' ', file=fout)
    print(file=fout)
fout.close()
