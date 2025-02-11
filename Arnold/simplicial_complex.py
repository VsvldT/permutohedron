#The array MF is the array of missing faces of the simplicial complex K
MF = [[1, 2], [2, 3], [1, 3]]
MF1 = [[4, 5], [5, 6], [4, 6]]

def term_in_complex(term):
    p = 0
    q = 0
    for i in range(3):
        for j in range(len(term)):
            if(set(MF[i]) <= set(term[j])):
                p = 1
            if(set(MF1[i]) <= set(term[j])):
                q = 1
        if(p and q):
            return 0
        p = 0
        q = 0
    return 1

