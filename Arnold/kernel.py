from gauss import Gauss

f0 = open("d0.txt", "r")
len0 = 0
len1 = 0
a = []
b = []
for line in f0:
    row = []
    row_b = []
    for j in line.split():
        row.append(int(j))
        row_b.append(int(j))
    len1 += 1
    len0 = len(row)
    a.append(row)
    b.append(row_b)
f0.close()
print(len0, len1, sep=' ')
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


f1 = open("d1.txt", "r")
len1 = 0#1800
len2 = 0#1080
a = []
b = []
for line in f1:
    row = []
    row_b = []
    for j in line.split():
        row.append(int(j))
        row_b.append(int(j))
    len2 += 1
    len1 = len(row)
    a.append(row)
    b.append(row_b)
f1.close()

print(len1, len2, sep=' ')
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


f2 = open("d2.txt", "r")
len3 = 0#90
len2 = 0#1080
a = []
b = []
for line in f2:
    row = []
    row_b = []
    for j in line.split():
        row.append(int(j))
        row_b.append(int(j))
    len3 += 1
    len2 = len(row)
    a.append(row)
    b.append(row_b)
f2.close()
print(len2, len3, sep=' ')
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

f3 = open("d3.txt", "r")
len4 = 0#90
len3 = 0#1080
a = []
b = []
for line in f3:
    row = []
    row_b = []
    for j in line.split():
        row.append(int(j))
        row_b.append(int(j))
    len4 += 1
    len3 = len(row)
    a.append(row)
    b.append(row_b)
f3.close()
print(len3, len4, sep=' ')
glav_per_3 = Gauss(a, len4, len3)
Ker_3 = []
Im_3 = []
for i in range(len3):
    if not(i in glav_per_3):
        v = [0] * len3
        v[i] = 1
        for j in range(len(glav_per_3)):
            v[glav_per_3[j]] = a[j][i]
        Ker_3.append(v)
    else:
        v = [0] * len4
        u = [0] * len3
        u[i] = 1
        for j in range(len4):
            v[j] = b[j][i]
        Im_3.append(v)

out = open("Ker3.txt", "w")
for i in range(len3 - len(glav_per_3)):
    for j in range(len3):
        print(Ker_3[i][j], file=out, end=' ')
    print(file=out)
out.close()

out = open("Im3.txt", "w")
for i in range(len(glav_per_3)):
    for j in range(len4):
        print(Im_3[i][j], file=out, end=' ')
    print(file=out)
out.close()

