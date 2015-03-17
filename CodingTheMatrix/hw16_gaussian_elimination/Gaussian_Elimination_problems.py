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
      flag = True
      for col, value in enumerate(row):
        if value != 0:
          if col <= idx:
            return False
          idx = col
          flag = False
          break
      if flag:
        idx = len(row) + 1
    return True


## 3: (Problem 3) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = [ 1, 0, 3, 0]
echelon_form_vec_b = [-3, 0,-2, 3]
echelon_form_vec_c = [-5, 0, 2, 0, 2]



## 4: (Problem 4) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21, 0, 2, 0, 0]



## 5: (Problem 5) Echelon Solver
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
    '''
    pass


## 6: (Problem 6) Solving General Matrices via Echelon
row_list = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list of GF(2) values



## 7: (Problem 7) Nullspace A
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## 8: (Problem 8) Nullspace B
null_space_rows_b = {...} # Put the row numbers of M from the PDF

