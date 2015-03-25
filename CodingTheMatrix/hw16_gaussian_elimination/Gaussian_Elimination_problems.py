# version code 62505f329d9b
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from vecutil import *
from GF2 import one
from echelon import *



## 1: (Problem 1) Recognizing Echelon Form
# Write each matrix as a list of row lists

echelon_form_1 = [[1, 2, 0, 2, 0],
                  [0, 1, 0, 3, 4],
                  [0, 0, 2, 3, 4],
                  [0, 0, 0, 2, 0], # replace the 1
                  [0, 0, 0, 0, 4]] # replace the 3

echelon_form_2 = [[0, 4, 3, 4, 4],
                  [0, 0, 4, 2, 0], # replace the 6 and 5
                  [0, 0, 0, 0, 1], 
                  [0, 0, 0, 0, 0]] # replace the 2

echelon_form_3 = [[1, 0, 0, 1],
                  [0, 0, 0, 1], # replace the 1
                  [0, 0, 0, 0]]

echelon_form_4 = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0], # replace the 1 and 1
                  [0, 0, 0, 0]]


 # for each row, the first nonzero entry is in position k and every previous row's non-zero entry is less than k
## 2: (Problem 2) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> is_echelon([[1,1]])
        True
        >>> is_echelon([[1]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
        >>> is_echelon([[2,1,0],[0,-4,0],[0,0,1]])
        True
        >>> is_echelon([[2,1,0],[-4,0,0],[0,0,1]])
        False
        >>> is_echelon([[2,1,0],[0,3,0],[1,0.1]])
        False
        >>> is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]])
        True
        >>> M1 = [[0,0,0],[0,0,0],[0,0,0]]
        >>> M2 = [[1,0,0],[0,1,0],[0,1,0]]
        >>> M3 = [[0]*4,[1]*4]
        >>> M4 = [[1,0,0,0,0,0,0,0], [0,1,1,1,1,1,1,1], [0,0,1,1,1,0,1,0], [0,0,0,0,0,1,1,0]]
        >>> M5 = [[1]]
        >>> M6 = [[0]]
        >>> is_echelon(M1)
        True
        >>> is_echelon(M2)
        False
        >>> is_echelon(M3)
        False
        >>> is_echelon(M4)
        True
        >>> is_echelon(M5)
        True
        >>> is_echelon(M6)
        True
        >>> is_echelon([[1,2,3],[0,1,7],[0,0,8]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> is_echelon([[1,1]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
        False
        >>> is_echelon([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        True
        >>> is_echelon([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
        False
        >>> is_echelon([[0,0,2,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
        False
    '''
    idx = -1
    for row in A:
      do_increment = True
      for col, value in enumerate(row):
        if value != 0:
          if col <= idx:
            return False
          idx = col
          do_increment = False
          break
      if do_increment:
        idx = len(row) + 1
    return True


## 3: (Problem 3) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = [ 1, 0, 3, 0] # [[10,2,-3,53],[0,0,1,2013]] * [x1,x2,x3,x4] = [1,3]
echelon_form_vec_b = [-3, 0,-2, 3] # [[2, 0, 1,3],[0,0,5,3],[0,0,0,1]] * [x1,x2,x3,x4] = [1,-1,3]
echelon_form_vec_c = [-5, 0, 2, 0, 2] # [[2,2,4,3,2],[0,0,-1,11,1],[0,0,0,0,5]] * [x1,x2,x3,x4] = [2,0,10]



## 4: (Problem 4) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

# [[1,3,-2,1,0],[0,0,2,-3,0],[0,0,0,0,0]] * [x1,x2,x3,x4,x5] = [5,3,2]
solving_with_echelon_form_a = None # 
# [[1,2,-8,-4,0],[0,0,2,12,0],[0,0,0,0,0],[0,0,0,0,0]] * [x1,x2,x3,x4,x5] = [5,4,0,0]
solving_with_echelon_form_b = [21, 0, 2, 0, 0]



## 5: (Problem 5) Echelon Solver
#
# The slickest way to write this procedure is to adapt the code of the
# procedure triangular solve(rowlist, label list, b) in module triangular. 
# As in that procedure, ini- tialize a vector x to zero, then iterate 
# through the rows of rowlist from last row to first row; in each iteration,
# assign to an entry of x. In this procedure, however, you must assign to 
# the variable corresponding to the column containing the first nonzero 
# entry in that row. (If there are no nonzero entries in that row, the 
# iteration should do nothing.)
# This approach leads to a very simple implementation consisting of about
# seven lines. The code closely resembles that for triangular solve.
def echelon_solve(row_list, label_list, b):
    '''
    Input:
        - row_list: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in row_list
        - b: a vector (represented as a list)
    Output:
        - Vec x such that row_list * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    >>> echelon_solve(U_rows, cols, b_list) 
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    >>> U_rows= [Vec(D,{'A':one,'C':one,'D':one}), Vec(D,{'B':one,'E':one}),Vec(D,{'C':one,'E':one}), Vec(D,{'E':one})]
    >>> b_list= [one,0,one,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) 
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': one, 'E': one, 'A': one})
    >>> U_rows = [Vec({0, 1}, {1:one, 0:0})]
    >>> echelon_solve(U_rows, [1, 0], [0, 0])
    Vec({0, 1},{})
    '''
    tmp = Vec(set(label_list), {})
    for i, row in enumerate(reversed(row_list)):
      t = b[len(b) - i - 1] + sum(row[j] * tmp[j] for j in label_list)
      if t == one:
        for j in label_list:
          if row[j] == one:
            tmp[j] = one
            break
    return tmp

## 6: (Problem 6) Solving General Matrices via Echelon

def solve(A, b):
    M = echelon.transformation(A)
    print("M=",A, "Mt", M)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    row_list = [U_rows_dict[i] for i in sorted(U_rows_dict)]
    return echelon_solve(row_list,col_label_list, M*b)

D = {'A','B','C','D'}
A = Mat(({'a', 'b', 'c', 'd'}, {'A', 'B', 'C', 'D'}),
   {     
         ('a', 'A'): one, ('a', 'B'): one, ('a', 'C'):   0, ('a', 'D'): one,
         ('b', 'A'): one, ('b', 'B'):   0, ('b', 'C'):   0, ('b', 'D'): one,
         ('c', 'A'): one, ('c', 'B'): one, ('c', 'C'): one, ('c', 'D'): one, 
         ('d', 'A'):   0, ('d', 'B'):   0, ('d', 'C'): one, ('d', 'D'): one
   }
)
r = Vec({'a', 'b', 'c', 'd'}, {'a': one, 'b':   0, 'c': one, 'd':   0})
M = transformation(A)
x = M * r
U = M * A
U_r = mat2rowdict(U)

row_list = [ U_r[i] for i in U_r ] # Provide as a list of Vec instances
label_list = sorted(A.D[1])        # Provide as a list
b = [ x[i] for i in x.D ]          # Provide as a list of GF(2) values

## 7: (Problem 7) Nullspace A
null_space_rows_a = { 3, 4} # Put the row numbers of M from the PDF

## 8: (Problem 8) Nullspace B
null_space_rows_b = {4} # Put the row numbers of M from the PDF

