from chain_complex import c_complex

def sublist(sub, lst):
    return str(sub).strip('[]') in str(lst).strip('[]')

MF = [[1, 2, 3], [1, 2, 4], [1, 3, 5], [2, 3, 6], [2, 4, 5], [3, 4, 5], [1, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6]]

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
        #print("#", j, "#", k)
        if((i + cnta >= n) or (i + cntb >= m)):
            if((i + cnta < n) or (i + cntb < m)):
                return 0
            else:
                break
        #print(j, k, a, b, sep=' ')
        if a[j] == b[k]:
            if (len(a[j]) == 1):
                res.append(a[j])
                continue
            else:
                return 0
       # if (len(a[j]) == 1) and (len(b[k]) == 1):
       #     if a[j] == b[k]:
       #         res.append(b[k])
       #         #print(b[k])
       #         continue
       #     else:
       #         return 2

        if (len(a[j]) == 1) and (len(a[j+1]) == 1) and (len(b[k]) == 2):
            if (a[j][0] == b[k][0]) and (a[j+1][0] == b[k][1]):
                res.append(b[k])
                #print(b[k])
                cnta += 1
                continue
            else:
                return 0
        if (len(b[k]) == 1) and (len(b[k+1]) == 1) and (len(a[j]) == 2):
            if (b[k][0] == a[j][1]) and (b[k+1][0] == a[j][0]):
                res.append(a[j])
                #print(a[j])
                cntb += 1
                continue
            else:
                return 0
        
        if (len(a[j]) == 1) and (len(a[j+1]) == 2) and (len(b[k]) == 2) and (len(b[k+1]) == 1):
            if (a[j][0] == b[k][0]) and (a[j+1][0] == b[k+1][0]) and (a[j+1][1] == b[k][1]) and (a[j+1][1] > a[j][0]):
                temp = [a[j][0], a[j+1][0], a[j+1][1]]
                temp.sort()
                if not (temp in MF):
                    res.append(temp)#[a[j][0], a[j+1][0], a[j+1][1]].sort())
                else:
                    return 0
                cnta += 1
                cntb += 1
                continue
            else:
                return 0
        if (len(a[j]) == 2) and (len(a[j+1]) == 1) and (len(b[k]) == 1) and (len(b[k+1]) == 2):
            if (a[j][0] == b[k+1][0]) and (a[j][1] == b[k][0]) and (a[j+1][0] == b[k+1][1]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j][1], a[j+1][0]]
                temp.sort()
                if not (temp in MF):
                    res.append(temp) #[a[j][0], a[j][1], a[j+1][0]].sort())
                else:
                    return 0
                cnta += 1
                cntb += 1
                continue
            else:
                return 0
        if (len(a[j]) == 1) and (len(a[j+1]) == 2) and (len(b[k]) == 1) and (len(b[k+1]) == 2):
            if (a[j][0] == b[k+1][0]) and (a[j+1][0] == b[k+1][1]) and (a[j+1][1] == b[k+1][0]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j+1][0], a[j+1][1]]
                temp.sort()
                if not (temp in MF):
                    res.append(temp)#[a[j][0], a[j+1][0], a[j+1][1]].sort())
                else:
                    return 0
                cnta += 1
                cntb += 1
                continue
            else:
                return 0
        if (len(a[j]) == 2) and (len(a[j+1]) == 1) and (len(b[k]) == 2) and (len(b[k+1]) == 1):
            if (a[j][0] == b[k+1][0]) and (a[j][1] == b[k][0]) and (a[j+1][0] == b[k][1]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j][1], a[j+1][0]]
                temp.sort()
                if not (temp in MF):
                    res.append(temp)#[a[j][0], a[j][1], a[j+1][0]].sort())
                else:
                    return 0
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
    return res

# 12 x 1|2 = 12         v
# 2|1 x 12 = 12         v
# 1|2|3 x 123 = 123     v
# 123 x 3|2|1 = 123     v
# 1|23 x 13|2 = 123     v
# 2|13 x 23|1 = 123     v
# 13|2 x 3|12 = 123     v
# 12|3 x 2|13 = 123     v
## 1|23 x 3|12 = 123    v
## 12|3 x 23|1 = 123    v


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
            #print("", end="")
            #print(c[2][j], end=' ')
    #print()
fin.close()
print(H2)
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

print(mult([[1], [2, 3], [4], [5, 6]], [[1], [3], [2], [4, 6], [5]]))

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
        if sublist(H2, res_ij):
            print("u_", i, " U ", "u_", j, " = v", sep='')
            tablica[i][j] = 1
            if not i in nevyr:
                nevyr.append(i)
fout = open("tablica.txt", "w")
for i in range(b_1):
    for j in range(b_1):
        print(tablica[i][j], end=' ', file=fout)
    print(file=fout)
fout.close()

for s in range(len(nevyr)):
    for t in range(len(nevyr)):
        i = nevyr[s]
        j = nevyr[t]
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
        if sublist(H2, res_ij):
            print("u_", i, " U ", "u_", j, " = v", sep='')
            tablica[i][j] = 1
fout = open("tabli4ka.txt", "w")
for i in range(len(nevyr)):
    for j in range(len(nevyr)):
        print(tablica[nevyr[i]][nevyr[j]], end=' ', file=fout)
    print(file=fout)
fout.close()

#print([[1, 2], [3], [4], [5], [6]], "U", [[2], [1], [3], [4, 5], [6]], "=", mult([[1, 2], [3], [4], [5], [6]], [[2], [1], [3], [4, 5], [6]]), sep=' ')
