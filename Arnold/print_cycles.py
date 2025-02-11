from chain_complex import c_complex


c = c_complex()

f2 = open("H2.txt", "r")
for line in f2:
    cnt = 0
    for j in line.split():
        if(int(j)):
            print(c[2][cnt], end='+')
        cnt += 1
    print()
f2.close()
