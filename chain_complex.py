import itertools as it
import numpy as np

#The array MF is th array of missing faces of the simplicial complex K
MF = [[1, 2, 3], [1, 2, 4], [1, 3, 5], [2, 3, 6], [2, 4, 5], [3, 4, 5], [1, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6]]

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
        if(len(product) > 3) or (product in MF):
            p = 0
        term.append(product)
        
        for j in range(6 - dim - i - 2):
            term.append(bar_generator[j+i+2])
        if p:
            sum_of_terms.append(term)
    return sum_of_terms

#The following function defines the cellular chain complex corresponding to the simplicial complex K
def c_complex():
    perm = it.permutations([1,2,3,4,5,6])
    c = []
    for i in range(4):
        c.append([])
    
    for permutation in perm:
        lst_perm= list(permutation)
        for partition in it.combinations([1,2,3,4,5], 2):
            elem1 = lst_perm[:partition[0]]
            elem2 = lst_perm[partition[0]:partition[1]]
            elem3 = lst_perm[partition[1]:]
            elem1.sort()
            elem2.sort()
            elem3.sort()
            if(max(len(elem1), len(elem2), len(elem3)) < 4) and (not ((elem1 in MF) or (elem2 in MF) or (elem3 in MF))):
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
            if(max(len(elem1), len(elem2), len(elem3), len(elem4)) < 4) and (not ((elem1 in MF) or (elem2 in MF) or (elem3 in MF) or (elem4 in MF))):
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
            if(max(len(elem1), len(elem2), len(elem3), len(elem4), len(elem5)) < 4) and (not ((elem1 in MF) or (elem2 in MF) or (elem3 in MF) or (elem4 in MF) or (elem5 in MF))):
                if not([elem1, elem2, elem3, elem4, elem5] in c[1]):
                    c[1].append([elem1, elem2, elem3, elem4, elem5])
        c[0].append([[lst_perm[0]],[lst_perm[1]],[lst_perm[2]],[lst_perm[3]],[lst_perm[4]],[lst_perm[5]]])
    return c

def main():
    c = c_complex()
    
    #for j in range(4):
    #    print(len(c[j]))

    d01 = []
    for i in range(len(c[0])):
        d01.append([])
        term = diff(c[0][i], 0)
        for j in range(len(c[1])):
            if(c[1][j] in term):
                d01[i].append(1)
            else:
                d01[i].append(0)
    
    d12 = []
    for i in range(len(c[1])):
        d12.append([])
        term = diff(c[1][i], 1)
        for j in range(len(c[2])):
            if(c[2][j] in term):
                d12[i].append(1)
            else:
                d12[i].append(0)
    
    d23 = []
    for i in range(len(c[2])):
        d23.append([])
        term = diff(c[2][i], 2)
        for j in range(len(c[3])):
            if(c[3][j] in term):
                d23[i].append(1)
            else:
                d23[i].append(0)
    
    file01 = open("d01.txt", "w")
    for i in range(len(c[1])):
        for j in range(len(c[0])):
            print(d01[j][i], end=' ', file=file01)
        print(file=file01)
    
    file01.close()
    
    
    file12 = open("d12.txt", "w")
    for i in range(len(c[2])):
        for j in range(len(c[1])):
            print(d12[j][i], end=' ', file=file12)
        print(file=file12)
    file12.close()
    
    
    file23 = open("d23.txt", "w")    
    for i in range(len(c[3])):
        for j in range(len(c[2])):
            print(d23[j][i], end=' ', file=file23)
        print(file=file23)
    
    file23.close()
    
    print(len(c[0]), len(c[1]), len(c[2]), len(c[3])) 


main()
