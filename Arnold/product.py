from alg_tools import *

c = c_complex()

#Итог. Надо причесать эту прогу, и по заданному шаблону обновить все остальные. Затем, если будет не лень, создать единый скрипт, 
#в который надо будет вводить имя файла с заданием симплициального комплекса, а дальше уже он сам компилирует одни и те же проги и выводит ответ в нужную папку.

def cycle_in_ker(cycle):
    Ker1 = []
    fin = open("Ker2.txt", "r")
    for line in fin:
        row = []
        for i in line.split():
            row.append(int(i))
        Ker1.append(row.copy())
    fin.close()

    glav_per = Gauss(Ker1, len(Ker1), len(Ker1[0]))
    Ker1.append(cycle.copy())
    FastGauss(Ker1, len(Ker1), len(cycle), glav_per)
    p = 1
    for i in range(len(cycle)):
        if Ker1[len(Ker1) - 1][i]:
            p = 0
            break
    return p

def cycle_in_H2(cycle, H2):
    Im1 = []
    fin = open("Im1.txt", "r")
    for line in fin:
        row = []
        for i in line.split():
            row.append(int(i))
        Im1.append(row.copy())
    fin.close()
    
    
    glav_per = Gauss(Im1, len(Im1), len(cycle))
    Im1.append(cycle.copy())
    FastGauss(Im1, len(Im1), len(cycle), glav_per)
    p = 0
    for i in range(len(cycle)):
        if Im1[len(Im1)-1][i]:
            p = 1
            print(c[2][i], '0', sep=' ')
            break
    if not p:
        return 0
    Im1.pop()
    
    Im1.append(H2[0].copy())
    #FastGauss(Im1, len(Im1), len(cycle), glav_per)
    #glav_per.append(len(Im1)-1)
    glav_per = Gauss(Im1, len(Im1), len(cycle))
    Im1.append(cycle.copy())
    FastGauss(Im1, len(Im1), len(cycle), glav_per)
    p = 0
    for i in range(len(cycle)):
        if Im1[len(Im1)-1][i]:
            p = 1
            print(c[2][i], '1', sep=' ')
            break
    if not p:
        return 1
    Im1.pop()
    
    Im1 = []
    fin = open("Im1.txt", "r")
    for line in fin:
        row = []
        for i in line.split():
            row.append(int(i))
        Im1.append(row.copy())
    fin.close()

    
    #Im1.pop()
    #glav_per.pop()
    Im1.append(H2[1].copy())
    #FastGauss(Im1, len(Im1), len(cycle), glav_per)
    #glav_per.append(len(Im1) - 1)
    glav_per = Gauss(Im1, len(Im1), len(cycle))
    Im1.append(cycle.copy())
    FastGauss(Im1, len(Im1), len(cycle), glav_per)
    p = 0
    for i in range(len(cycle)):
        if Im1[len(Im1)-1][i]:
            p = 1
            print(c[2][i], '2', sep=' ')
            break
    if not p:
        return 2

    return 3
    Im1.pop()
    Im1.pop()
    
    Im1.append(H2[2].copy())
    FastGauss(Im1, len(Im1), len(cycle), glav_per)
    #glav_per = Gauss(Im1, len(Im1), len(cycle))
    Im1.append(cycle.copy())
    FastGauss(Im1, len(Im1), len(cycle), glav_per)
    p = 0
    for i in range(len(cycle)):
        if Im1[len(Im1)-1][i]:
            p = 1
            print(c[2][i], '3', sep=' ')
            break
    if not p:
        return 3
    else:
        return -1


fin = open("H2.txt", "r")
b_2 = 0
len2 = 0
a = []
for line in fin:
    row = []
    for i in line.split():
        row.append(int(i))
    b_2 += 1
    len2 = len(row)
    a.append(row.copy())



H2 = []
print(b_2, len2)
for i in range(b_2):
    rs = []
    for j in range(len2):
        rs.append(a[i][j])
    H2.append(rs.copy())
rs = []
for j in range(len2):
    rs.append(a[0][j] ^ a[1][j])
H2.append(rs.copy())
fin.close()
#for i in range(b_2):
#    print(H2[i])


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
    a.append(row.copy())
fin.close()
print(b_1, len1)

#print(mult([[1], [2, 3], [4], [5, 6]], [[1], [3], [2], [4, 6], [5]]))

tablica = []
for i in range(b_1):
    tablica.append([0]*b_1)


q = 1
out = open("mult_check.txt", "w")
for i in range(b_1):
    for j in range(b_1):
        res_ij = []
        nenul_1 = []
        nenul_2 = []
        res_coord = []
        for k in range(len1):
            if(a[i][k]):
                nenul_1.append(k)
            if(a[j][k]):
                nenul_2.append(k)
        for k in nenul_1:
            for l in nenul_2:
                r = mult(c[1][k], c[1][l])
                if r and q:
                    #q = 0
                    print(c[1][k], "U", c[1][l], "=", r, sep=' ')
                if r:
                    if r in res_ij:
                        res_ij.remove(r)
                    else:
                        res_ij.append(r.copy())
        for k in range(len2):
            if c[2][k] in res_ij:
                res_coord.append(1)
            else:
                res_coord.append(0)
        #print(res_ij)
        otvet = cycle_in_H2(res_coord.copy(), H2.copy())
        #otvet = cycle_in_ker(res_coord)
        if otvet:
            print("u_", i, " U ", "u_", j, " = ", otvet, sep='')
        #else:
        #    print("Wtf, some mysterious force made u_", i, "U", "u_", j, "to be not a cycle...", sep=' ')
        tablica[i][j] = otvet
fout = open("tablica.txt", "w")
for i in range(b_1):
    for j in range(b_1):
        print(tablica[i][j], end=' ', file=fout)
    print(file=fout)
out.close()
fout.close()
