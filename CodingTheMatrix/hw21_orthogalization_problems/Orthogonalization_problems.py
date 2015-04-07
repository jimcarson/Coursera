# version code 0672c0a36066
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from QR import *
from solver import *
from dictutil import *
from mat import Mat
from math import sqrt
from matutil import *
from orthogonalization import *
from triangular import *
from vec import Vec
from vecutil import *
from read_data import *



# page 367

def find_orthogonal_complement(U_basis, W_basis):
    '''
       Find orthogonal complement, from 9.6, page 367
    Input:
       - U basis for U, W basis for W
    Output:
       - orthogonal complment.  Vectors u*1..k have same span and are nonzero 
         as u1..k is linearly independent.  n-k of the remaining vectors of 
         w*1..n are nonzero and every one is orthogonal to u1..n, so they 
         are orthogonal to every vector in U.  
    >>> L = [list2vec(v) for v in [[8,-2,2], [0,3,3], [1,0,0], [0,1,0], [0,0,1]]]
    >>> Lstar = orthogonalize(L)
    >>> Lstar[2].is_almost_zero()
    False
    >>> Lstar[3].is_almost_zero()
    True
    >>> Lstar[4].is_almost_zero()
    True
    '''
    k = len(U_basis)
    n = len(W_basis)
    v = [list2vec(i) for i in U_basis + W_basis]
    w = orthogonalize(v)
    return [w[i] for i in range(k, k+n) if not w[i].is_almost_zero()]

## 1: (Problem 1) Generators for orthogonal complement
U_vecs_1 = [[0,0,3,2]]
W_vecs_1 = [[1,2,-3,-1],[1,2,0,1],[3,1,0,-1],[-1,-2,3,1]]
# Give a list of Vecs
ortho_compl_generators_1 = find_orthogonal_complement(U_vecs_1, W_vecs_1)

U_vecs_2 = [[3,0,1]]
W_vecs_2 = [[1,0,0],[1,0,1]]

# Give a list of Vecs
ortho_compl_generators_2 = find_orthogonal_complement(U_vecs_2, W_vecs_2)

U_vecs_3 = [[-4,3,1,-2],[-2,2,3,-1]]
W_vecs_3 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

# Give a list of Vecs
ortho_compl_generators_3 = find_orthogonal_complement(U_vecs_3, W_vecs_3)

## 2: (Problem 2) Basis for null space
# Take augmented matrix, reduce to echelon form.
A = listlist2mat([[-4,-1,-3,-2],[0,4,0,-1]])
Q = listlist2mat([[-1,0],[0,1]])
R = listlist2mat([[4,1,3,2],[0,4,0,-1]])
echelon_form = listlist2mat([[1,0,.75, 9./16],[0,1,0,-.25]])
orthonormal_basis = list2vec([-0.4826895750, -0.0638853, 0.835242, -0.2555412])
#null_space_basis = list2vec([-3,0,4,0]) #,[-9,4,0,16]]
null_space_basis = [-0.4826895750, -0.0638853, 0.835242, -0.2555412]

## 3: (Problem 3) Orthonormalize(L)
def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> for v in orthonormalize(L): print(v)
    ... 
    <BLANKLINE>
        a     b     c     d
    -----------------------
     0.73 0.548 0.183 0.365
    <BLANKLINE>
         a     b      c      d
    --------------------------
     0.187 0.403 -0.566 -0.695
    <BLANKLINE>
         a      b      c     d
    --------------------------
     0.528 -0.653 -0.512 0.181
    '''
    return [ i/sqrt(i*i) for i in orthogonalize(L)]



## 4: (Problem 4) aug_orthonormalize(L)
def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
            
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    >>> from matutil import coldict2mat
    >>> print(coldict2mat(Qlist))
    <BLANKLINE>
               0      1      2
         ---------------------
     a  |   0.73  0.187  0.528
     b  |  0.548  0.403 -0.653
     c  |  0.183 -0.566 -0.512
     d  |  0.365 -0.695  0.181
    <BLANKLINE>
    >>> print(coldict2mat(Rlist))
    <BLANKLINE>
              0    1      2
         ------------------
     0  |  5.48 8.03   9.49
     1  |     0 11.4 -0.636
     2  |     0    0   6.04
    <BLANKLINE>
    >>> print(coldict2mat(Qlist)*coldict2mat(Rlist))
    <BLANKLINE>
           0  1  2
         ---------
     a  |  4  8 10
     b  |  3  9  1
     c  |  1 -5 -1
     d  |  2 -5  5
    <BLANKLINE>

    '''
    Qlist = orthonormalize(L)
    Qm = coldict2mat(Qlist).transpose()
    Rm = Qm * coldict2mat(L)
    Rlist = list(mat2coldict(Rm).values())
    return Qlist, Rlist



## 6: (Problem 6) QR Solve

def QR_factor(A):
    col_labels = sorted(A.D[1], key=repr)
    Acols = dict2list(mat2coldict(A),col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    #Now make Mats
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q,R



## 5: (Problem 5) QR factorization of small matrices
#Compute the QR factorization

#Please represent your solution as a list of rows, such as [[1,0,0],[0,1,0],[0,0,1]]


QR5a = listlist2mat([[6,6],[2,0],[3,3]])
QR5b = listlist2mat([[2,3],[2,1],[1,1]])
Q, R = QR_factor(QR5a)
part_1_Q = [[.857,.256],[.286,-.958],[.429,.128]]
part_1_R = [[7, 6.43],[0,1.92]]

Q, R = QR_factor(QR5b)
part_2_Q = [[.667, .707],[.667, -.707],[.333,0]]
part_2_R = [[3, 3], [0, 1.41]]


import scipy
import scipy.linalg
def QR_solve(A, b):
    '''
    Input:
        - A: a Mat with linearly independent columns
        - b: a Vec whose domain equals the set of row-labels of A
    Output:
        - vector x that minimizes norm(b - A*x)
    Note: This procedure uses the procedure QR_factor, which in turn uses dict2list and list2dict.
           You wrote these procedures long back in python_lab.  Make sure the completed python_lab.py
           is in your matrix directory.
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR_factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result.is_almost_zero()
        True
    '''
    # Qp, Rp  = scipy.linalg.qr(scipy.array(A))
    # Q = Qp.tolist()
    # R = Rp.tolist()
    Q, R = QR_factor(A)
    Rlist = list( mat2rowdict(R).values())
    bprime = Q.transpose() * b
    return triangular_solve_n(Rlist,bprime)



## 7: (Problem 7) Least Squares Problem
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]])
least_squares_b1 = list2vec([10, 8, 6])

x_hat_1 =  triangular_solve_n(list(mat2rowdict(least_squares_R1).values()),least_squares_Q1.transpose()*least_squares_b1)

least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

# x_hat_2 = QR_solve(least_squares_A2, least_squares_b2)
x_hat_2 =  triangular_solve_n(list(mat2rowdict(least_squares_R2).values()),least_squares_Q2.transpose()*least_squares_b2)




## 8: (Problem 8) Small examples of least squares
#Find the vector minimizing (Ax-b)^2

#Please represent your solution as a list

A8a = listlist2mat([[8,1],[6,2],[0,6]])
b8a = list2vec([10,8,6])

Q,R = QR_factor(A8a)
your_answer_1 = [1.08, 0.984]

A8b = listlist2mat([[3,1],[4,1]])
b8b = list2vec([10,13])
Q,R = QR_factor(A8b)
your_answer_2 = [3,1]



## 9: (Problem 9) Linear regression example
#Find a and b for the y=ax+b line of best fit

A = read_vectors("age-height.txt")
# Q, R = QR_factor(A)
# age	height
# { {18,76.1} {19,77} {20,78.1} {21,78.2} {22,78.8} {23,79.7} {24,79.9} {25,81.1} {26,81.2} {27,81.8} {28,82.8} {29,83.5} }
a = 0.634965
b = 64.9283

