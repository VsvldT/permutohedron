This project was made to calculate the cohomology ring of diagonal arrangement complements via bar-construcion (in real case) or its modification (in complex case).

The order of executing the programs is the following:
1) chain_complex.py <- creates the chain complex and saves matrices of <i>-th differential in the file d<i>.txt;
2) kernel.py <- calculates kernels and images of differentials using Gauss method and saves <i>-th kernel and image in the files Ker<i>.txt and Im<i>.txt correspondingly;
3) cohomology.py <- finds the generators of <i>-th cohomology group in <i>-th kernel and saves them in the file H<i>.txt;
4) product.py <- calculates the structure constants of the cohomology algebra and saves them in the file tablica.txt. There is the only one file since the considered spaces have non-trivial cohomology only in dimensions 0, 1, 2 and, therefore, non-trivial product is concentrated in dimension 1. File tabli4ka.txt can be obtained from tablica.txt by removing zero rows and columns.

The file alg_tools.py consists of algebraic tools used in all programs, such as Gauss method and its slight modification, dualizing of Saneblidze-Umble diagonal, procedure of constructing the complex of cellular chain groups etc.
The file simplicial_complex.py contains the information about the considered simplicial complex and the function which determines whether the element of tensor product (over the exterior Stanley--Reisner algebra) belongs to the bar-construction (or its modification for complex case) or not. It is the only one file which depends on the simplicial complex, so there is no need to change other files for different simplicial complexes.

