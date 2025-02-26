from alg_tools import *

c = c_complex()

f = open("H1.txt", "r")
for line in f:
    cnt = 0
    for j in line.split():
        if(int(j)):
            print(c[1][cnt], end='+')
        cnt += 1
    print()
    print()
    print()
f.close()

#fin = open("Im1.txt", "r")
#Im1 = []
#cnt = 0
#for line in fin:
#    row = []
#    for elem in line.split():
#        row.append(int(elem))
#    Im1.append(row)
#    cnt = len(line)
#fin.close()
#Gauss(Im1, len(Im1), len(Im1[0]))
#f = open("Gaussed_Im_1.txt", "w")
#for i in range(len(Im1)):
#    for j in range(len(Im1[0])):
#        print(Im1[i][j], end=' ', file=f)
#    print(file=f)
#f.close()
