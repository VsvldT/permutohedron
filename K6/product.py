from alg_tools import *

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
    for j in range(len2):
        if(a[i][j]):
            H2.append(c[2][j])
fin.close()

fin = open("H1.txt", "r")
b_1 = 0
len1 = 0
a = []
for line in fin:
    row = []
    for i in  line.split():
        row.append(int(i))
    b_1 += 1
    len1 = len(row)
    a.append(row)
fin.close()
q = 1

tablica = []
for i in range(b_1):
    tablica.append([0]*b_1)

nevyr = []

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
        if(len(res_ij) > 0):
            #u_i --- образующие H^1, v_j --- образующие H^2
            if not i in nevyr:
                nevyr.append(i)
            for k in range(b_2):
                if(H2[k] in res_ij):
                    if tablica[i][j]:
                        tablica[i][j] = str(tablica[i][j]) + '+' + str(k+1)
                    else:
                        tablica[i][j] = str(k+1)
    print("Success", i, sep=' ')
fout = open("tablica.txt", "w")
for i in range(b_1):
    for j in range(b_1):
        print(tablica[i][j], end='\t', file=fout)
    print(file=fout)
fout.close()

fout = open("tabli4ka.txt", "w")
for i in range(len(nevyr)):
    for j in range(len(nevyr)):
        print(tablica[nevyr[i]][nevyr[j]], end=' ', file=fout)
    print(file=fout)
fout.close()
