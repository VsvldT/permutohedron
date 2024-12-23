from gauss import Gauss

f01 = open("d01.txt", "r")
len0 = 0
len1 = 0
a = []
b = []
for line in f01:
    row = []
    row_b = []
    for j in line.split():
        row.append(int(j))
        row_b.append(int(j))
    len1 += 1
    len0 = len(row)
    a.append(row)
    b.append(row_b)
f01.close()
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


f12 = open("d12.txt", "r")
len1 = 0#1800
len2 = 0#1080
a = []
b = []
for line in f12:
    row = []
    row_b = []
    for j in line.split():
        row.append(int(j))
        row_b.append(int(j))
    len2 += 1
    len1 = len(row)
    a.append(row)
    b.append(row_b)
f12.close()

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


f23 = open("d23.txt", "r")
len3 = 0#90
len2 = 0#1080
a = []
b = []
for line in f23:
    row = []
    row_b = []
    for j in line.split():
        row.append(int(j))
        row_b.append(int(j))
    len3 += 1
    len2 = len(row)
    a.append(row)
    b.append(row_b)
f23.close()
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


