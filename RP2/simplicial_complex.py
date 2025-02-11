#The array MF is th array of missing faces of the simplicial complex K
MF = [[1, 2, 3], [1, 2, 4], [1, 3, 5], [2, 3, 6], [2, 4, 5], [3, 4, 5], [1, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6]]

def term_in_complex(term):
    p = 0
    q = 0
    for i in range(len(term)):
        for j in range(len(MF)):
            if(set(MF[j]) <= set(term[i])):
                return 0
    return 1

