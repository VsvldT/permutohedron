import itertools as it
import numpy as np

#The array MF is the array of missing faces of the simplicial complex K
MF = [[1, 2], [2, 3], [1, 3]]
MF1 = [[4, 5], [5, 6], [4, 6]]

def term_in_complex(term, dim):
    p = 0
    q = 0
    for i in range(3):
        for j in range(6 - dim):
            if(set(MF[i]) <= set(term[j])):
                p = 1
            if(set(MF1[i]) <= set(term[j])):
                q = 1
        if(p and q):
            return 0
        p = 0
        q = 0
    return 1

#The following function calculates the differential of the generator of bar construction
def diff(bar_generator, dim):
    sum_of_terms = []
    for i in range(6 - dim - 1):
        p = 1
        term = []
        for j in range(i):
            term.append(bar_generator[j])
        product = bar_generator[i] + bar_generator[i+1]
        product.sort()
        #Тут надо править
        #if(len(product) > 3) or (product in MF):
        #    p = 0
        #Конец правки
        term.append(product)
        
        for j in range(6 - dim - i - 2):
            term.append(bar_generator[j+i+2])
        if term_in_complex(term, dim + 1):
            sum_of_terms.append(term)
    return sum_of_terms

#The following function defines the cellular chain complex corresponding to the simplicial complex K
def c_complex():
    perm = it.permutations([1,2,3,4,5,6])
    c = []
    for i in range(5):
        c.append([])
    
    for permutation in perm:
        lst_perm = list(permutation)
        
        for partition in range(5):
            elem1 = lst_perm[:partition+1]
            elem2 = lst_perm[partition+1:]
            elem1.sort()
            elem2.sort()
            if(term_in_complex([elem1, elem2], 4)):
                if not([elem1, elem2] in c[4]):
                    c[4].append([elem1, elem2])

        for partition in it.combinations([1,2,3,4,5], 2):
            elem1 = lst_perm[:partition[0]]
            elem2 = lst_perm[partition[0]:partition[1]]
            elem3 = lst_perm[partition[1]:]
            elem1.sort()
            elem2.sort()
            elem3.sort()
            #if(max(len(elem1), len(elem2), len(elem3)) < 4) and (not ((elem1 in MF) or (elem2 in MF) or (elem3 in MF))):
            if(term_in_complex([elem1, elem2, elem3], 3)):
                if not([elem1, elem2, elem3] in c[3]):
                    c[3].append([elem1,elem2,elem3])
        for partition in it.combinations([1,2,3,4,5], 3):
            elem1 = lst_perm[:partition[0]]
            elem2 = lst_perm[partition[0]:partition[1]]
            elem3 = lst_perm[partition[1]:partition[2]]
            elem4 = lst_perm[partition[2]:]
            elem1.sort()
            elem2.sort()
            elem3.sort()
            elem4.sort()
            #if(max(len(elem1), len(elem2), len(elem3), len(elem4)) < 4) and (not ((elem1 in MF) or (elem2 in MF) or (elem3 in MF) or (elem4 in MF))):
            if(term_in_complex([elem1, elem2, elem3, elem4], 2)):
                if not( [elem1, elem2, elem3, elem4] in c[2]):
                    c[2].append([elem1, elem2, elem3, elem4])
        for partition in it.combinations([1,2,3,4,5], 4):
            elem1 = lst_perm[:partition[0]]
            elem2 = lst_perm[partition[0]:partition[1]]
            elem3 = lst_perm[partition[1]:partition[2]]
            elem4 = lst_perm[partition[2]:partition[3]]
            elem5 = lst_perm[partition[3]:]
            elem1.sort()
            elem2.sort()
            elem3.sort()
            elem4.sort()
            elem5.sort()
            #if(max(len(elem1), len(elem2), len(elem3), len(elem4), len(elem5)) < 4) and (not ((elem1 in MF) or (elem2 in MF) or (elem3 in MF) or (elem4 in MF) or (elem5 in MF))):
            if(term_in_complex([elem1, elem2, elem3, elem4, elem5], 1)):
                if not([elem1, elem2, elem3, elem4, elem5] in c[1]):
                    c[1].append([elem1, elem2, elem3, elem4, elem5])
        c[0].append([[lst_perm[0]],[lst_perm[1]],[lst_perm[2]],[lst_perm[3]],[lst_perm[4]],[lst_perm[5]]])
    return c

def main():
    c = c_complex()
    
    #for j in range(4):
    #    print(len(c[j]))

    d0 = []
    for i in range(len(c[0])):
        d0.append([])
        term = diff(c[0][i], 0)
        for j in range(len(c[1])):
            if(c[1][j] in term):
                d0[i].append(1)
            else:
                d0[i].append(0)
    
    d1 = []
    for i in range(len(c[1])):
        d1.append([])
        term = diff(c[1][i], 1)
        for j in range(len(c[2])):
            if(c[2][j] in term):
                d1[i].append(1)
            else:
                d1[i].append(0)
    
    d2 = []
    for i in range(len(c[2])):
        d2.append([])
        term = diff(c[2][i], 2)
        for j in range(len(c[3])):
            if(c[3][j] in term):
                d2[i].append(1)
            else:
                d2[i].append(0)

    d3 = []
    for i in range(len(c[3])):
        d3.append([])
        term = diff(c[3][i], 3)
        for j in range(len(c[4])):
            if(c[4][j] in term):
                d3[i].append(1)
            else:
                d3[i].append(0)

    
    file0 = open("d0.txt", "w")
    #print(len(c[1]), len(c[0]), sep=' ', file=file0)
    for i in range(len(c[1])):
        for j in range(len(c[0])):
            print(d0[j][i], end=' ', file=file0)
        print(file=file0)
    
    file0.close()
    
    
    file1 = open("d1.txt", "w")
    #print(len(c[2]), len(c[1]), sep=' ', file=file1)
    for i in range(len(c[2])):
        for j in range(len(c[1])):
            print(d1[j][i], end=' ', file=file1)
        print(file=file1)
    file1.close()
    
    
    file2 = open("d2.txt", "w")    
    #print(len(c[3]), len(c[2]), sep=' ', file=file2)
    for i in range(len(c[3])):
        for j in range(len(c[2])):
            print(d2[j][i], end=' ', file=file2)
        print(file=file2)
    file2.close()

    file3 = open("d3.txt", "w")    
    #print(len(c[4]), len(c[3]), sep=' ', file=file3)
    for i in range(len(c[4])):
        for j in range(len(c[3])):
            print(d3[j][i], end=' ', file=file3)
        print(file=file3)
    file3.close()

    
    print(len(c[0]), len(c[1]), len(c[2]), len(c[3]), len(c[4])) 
main()
