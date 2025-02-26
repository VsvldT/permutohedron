from alg_tools import *

"""
#The follofing function computes the dualizing of SU diagonal by the rule, described in the comments below.
# 12 x 1|2 = 12
# 2|1 x 12 = 12
# 1|2|3 x 123 = 123 !!! 9
# 123 x 3|2|1 = 123 !!! 9
# 1|23 x 13|2 = 123
# 2|13 x 23|1 = 123 
# 13|2 x 3|12 = 123 
# 12|3 x 2|13 = 123 
## 1|23 x 3|12 = 123 !!! 6
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

        if((i + cnta >= n) or (i + cntb >= m)):
            if((i + cnta < n) or (i + cntb < m)):
                return 1
            else:
                break

        if a[j] == b[k]:
            if (len(a[j]) == 1):
                res.append(a[j])
                continue
            else:
                return 2

        if (len(a[j]) == 1) and (len(a[j+1]) == 1) and (len(b[k]) == 2):
            if (a[j][0] == b[k][0]) and (a[j+1][0] == b[k][1]):
                res.append(b[k])
                cnta += 1
                continue
            else:
                return 3
        if (len(b[k]) == 1) and (len(b[k+1]) == 1) and (len(a[j]) == 2):
            if (b[k][0] == a[j][1]) and (b[k+1][0] == a[j][0]):
                res.append(a[j])
                cntb += 1
                continue
            else:
                return 4
        

        if (len(a[j]) == 1) and (len(a[j+1]) == 2) and (len(b[k]) == 2) and (len(b[k+1]) == 1):
            if (a[j][0] == b[k][0]) and (a[j+1][0] == b[k+1][0]) and (a[j+1][1] == b[k][1]) and (a[j+1][1] > a[j][0]):
                temp = [a[j][0], a[j+1][0], a[j+1][1]]
                temp.sort()
                res.append(temp)
                cnta += 1
                cntb += 1
                continue
            else:
                return 5

        if (len(a[j]) == 2) and (len(a[j+1]) == 1) and (len(b[k]) == 1) and (len(b[k+1]) == 2):
            if (a[j][0] == b[k+1][0]) and (a[j][1] == b[k][0]) and (a[j+1][0] == b[k+1][1]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j][1], a[j+1][0]]
                temp.sort()
                res.append(temp) 
                cnta += 1
                cntb += 1
                continue
            else:
                return 6

        if (len(a[j]) == 1) and (len(a[j+1]) == 2) and (len(b[k]) == 1) and (len(b[k+1]) == 2):
            if (a[j][0] == b[k+1][0]) and (a[j+1][0] == b[k+1][1]) and (a[j+1][1] == b[k][0]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j+1][0], a[j+1][1]]
                temp.sort()
                res.append(temp)
                cnta += 1
                cntb += 1
                continue
            else:
                return 7

        if (len(a[j]) == 2) and (len(a[j+1]) == 1) and (len(b[k]) == 2) and (len(b[k+1]) == 1):
            if (a[j][0] == b[k+1][0]) and (a[j][1] == b[k][0]) and (a[j+1][0] == b[k][1]) and (a[j][0] < a[j+1][0]):
                temp = [a[j][0], a[j][1], a[j+1][0]]
                temp.sort()

                res.append(temp)
                cnta += 1
                cntb += 1
                continue
            else:
                return 8
        
        else:
            if (j+2 >= n) and (k+2 >= m):
                return 9
        
        if (len(a[j]) == 1) and (len(a[j+1]) == 1) and (len(a[j+2]) == 1) and (len(b[k]) == 3):
            if(a[j][0] == b[k][0]) and (a[j+1][0] == b[k][1]) and (a[j+2][0] == b[k][2]):
                res.append(b[k])
                cnta += 2
                continue
            else:
                return 10
        if (len(b[k]) == 1) and (len(b[k+1]) == 1) and (len(b[k+2]) == 1) and (len(a[j]) == 3):
            if(b[k][0] == a[j][2]) and (b[k+1][0] == a[j][1]) and (b[k+2][0] == a[j][0]):
                res.append(a[j])
                cntb += 2
                continue
            else:
                return 11
        else:
            return 12
    if(term_in_complex(res)):
        return res
    return 13
"""



print(mult([[1], [2], [3]], [[1, 2, 3]]), mult([[1, 2, 3]], [[3], [2], [1]]), sep=' ')
print(mult([[1], [2, 3]], [[1, 3], [2]]), mult([[2], [1, 3]], [[2,3], [1]]), mult([[1,3], [2]], [[3], [1,2]]), sep=' ')
print(mult([[1,2], [3]], [[2], [1,3]]), mult([[1], [2, 3]], [[3], [1,2]]), mult([[1,2], [3]], [[2, 3], [1]]), sep=' ')
