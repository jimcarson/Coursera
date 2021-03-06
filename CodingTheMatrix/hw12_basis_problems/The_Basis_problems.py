# version code 36f614bd24c7+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from GF2 import one
from math import sqrt, pi
from matutil import coldict2mat, rowdict2mat
from solver import solve
from vec import Vec
from vecutil import list2vec



## 1: (Problem 1) Span of Vectors over R, A
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.
#
# For example, [1, 3, 5] would mean 1*[2,0,4,0] + 3*[0,1,0,1] + 5*[0,0,-1,-1]

# Span = listlist2mat([[2,0,4,0], [0,1,0,1], [0,0,-1,-1]])
rep_1 = [1.0,  1.0,  0.0]  # 2 1 4 1
rep_2 = [0.5,  1.0,  1.0]  # 1 1 1 0
rep_3 = [0.0,  1.0, -1.0]  # 0 1 1 2

## 2: (Problem 2) Span of Vectors over R, B
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

# Span = listlist2mat([[0,0,1], [2,0,1], [4,1,2]])
lin_comb_coefficients_1 = [ 3.0, -1.0,  1.0] # 2 1 4
lin_comb_coefficients_2 = [ 0.5, -1.5,  1.0] # 1,1,1
lin_comb_coefficients_3 = [ 0.5, -5.5,  4.0] # 5,4,3
lin_comb_coefficients_4 = [ 1.0, -2.0,  1.0] # 0,1,1

## 3: (Problem 3) Span of Vectors over GF2 A
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.
# Span = listlist2mat([[0,1,0,1],[0,0,1,0],[1,0,0,1],[1,1,1,1]])

gf2_rep_1 = [ one,   0, one,   0]
gf2_rep_2 = [ one,   0,   0, one]
gf2_rep_3 = [ one, one,   0, one]



## 4: (Problem 4) Span of Vectors over GF2 B
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

#      a     b    c    d    e    f    g    h
# v1   one   one
# v2         one  one
# v3   one             one
# v4         one            one
# v5              one       one
# v6                   one  one
# v7                             one       one
# v8                                  one  one

gf2_lc_rep_1 = [one, one, one,   0,   0,   0,   0,   0 ] # 0 0 one one 0 0 0 0 
gf2_lc_rep_2 = [one, one, one,   0, one, one, one, one ] # 0 0 0 0 0 one one 0
gf2_lc_rep_3 = [  0, one, one, one, one, one,   0,   0 ] # one 0 0 0 one 0 0 0 
gf2_lc_rep_4 = [  0, one,   0,   0, one, one,   0,   0 ] # 0 one 0 one 0 0 0 0 
 


## 5: (Problem 5) Linear Dependence over R A
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

lin_dep_R_1 = [-2.0, 1.0, 1.0]  # [1,2,0], [2,4,1], [0,0,-1]
lin_dep_R_2 = [-4.0, 1.0,-4.0/7.0]  # [2,4,0], [8,16,4], [0,0,7]
lin_dep_R_3 = [-0.3, 0.0, 0.0, 1.0, 3.0]  # [0,0,5], [1,34,2],[123,456,789],[-3,-6,0],[1,2, 0.5]



## 6: (Problem 6) Linear Dependence over R B
# Please record your solution as a list of coefficients

linear_dep_R_1 = [1, -1, 3] # [1,2,3], [4,5,6], [1,1,1]
linear_dep_R_2 = [ 2 * sqrt(2), sqrt(2)/pi, 1 ] # [0, -1, 0, -1] [pi, pi, pi, pi], [-sqrt(2), sqrt(2), -sqrt(2), sqrt(2)]
linear_dep_R_3 = [ 1, 1, 1, 1, 1] # [1, -1, 0, 0, 0], [0, 1, -1, 0, 0], [0, 0, 1, -1, 0], [0,0,0,1,-1], [-1,0,0,0,1]



## 7: (Problem 7) Superfluous vector
# Choose one of the vectors to express as a linear combination of the other two,
# and assign the name of that vector to sum_to (as a string)
# For each of the other two vectors, assign the coefficient to the corresponding variable.
# For example, if you want to say that w equals 2*u+3*v, you would
# assign 'w' to sum_to, assign 2 to u_coeff, and assign 3 to v_coeff.
# (In this case, it would not matter what was assigned to w_coeff.)
sum_to = 'u'
u_coeff = 1    # [3,9,6,5,5]
v_coeff = 1    # [4,10,6,6,8]
w_coeff = -1   # [1,1,0,1,3]



## 8: (Problem 8) 4 linearly dependent vectors, every 3 are independent
# Please use the Vec class to represent your vectors

indep_vec_1 = Vec({0,1,2},{0:1, 1:0, 2:0})
indep_vec_2 = Vec({0,1,2},{0:1, 1:1, 2:1})
indep_vec_3 = Vec({0,1,2},{0:0, 1:1, 2:0})
indep_vec_4 = Vec({0,1,2},{0:0, 1:0, 2:1})



## 9: (Problem 9) Linear Dependence over GF(2) A
# For each subproblem, assign to the corresponding variable the list of
# coefficients (0 or one) for which the linear combination is zero.

zero_comb_1 = [one,one,  0,one] # [one,one,one,one], [one,0,one,0], [0,one,one,0], [0,one,0,one]
zero_comb_2 = [  0,one,one,one] # [0,0,0,one], [0,0,one,0], [one,one,0,one], [one,one,one,one]
zero_comb_3 = [one,one,  0,  0,one] # [one,one,0,one,one], [0,0,one,0,0], [0,0,one,one,one], [one,0,one,one,one], [one,one,one,one,one]



## 10: (Problem 10) Linear Dependence over GF(2) B
# In each subproblem, give your solution as a list of coefficients selected from {0, one}


#      a     b    c    d    e    f    g    h
# v1   one   one
# v2         one  one
# v3   one             one
# v4         one            one
# v5              one       one
# v6                   one  one
# v7                             one       one
# v8                                  one  one

# [coeff of v1, coeff of v2, coeff of v3, coeff of v4, coeff of v5]
sum_to_zero_1 = [  0, one,   0, one, one] # v1, v2, v3, v4, v5

# [coeff of v1, coeff of v2, coeff of v3, coeff of v4, coeff of v5, coeff of v7, coeff of v8]
sum_to_zero_2 = [  0, one,   0, one, one,   0,   0] # v1, v2, v3, v4, v5, v7, v8

# [coeff of v1, coeff of v2, coeff of v3, coeff of v4, coeff of v6]
sum_to_zero_3 = [one,    0, one, one, one] # v1, v2, v3, v4, v6

# [coeff of v1, coeff of v2, coeff of v3, coeff of v5, coeff of v6, coeff of v7, coeff of v8]
sum_to_zero_4 = [one, one, one, one, one,   0,   0] # v1, v2, v3, v5, v6, v7, v8



## 11: (Problem 11) Exchange Lemma for Vectors over $\R$
## Please express your answer as a list of ints, such as [1,0,0,0,0]
# S = {[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]}
# A = {[1,0,0,0,0], [0,1,0,0,0]}
# For each of the following vectors, z, find a vector w in S - A such that 
# Span S = Span (S U {z} - {w})

exchange_1 = [0,0,1,0,0] # z = [1,1,1,1,1]
exchange_2 = [0,0,0,1,0] # z = [0,1,0,1,0]
exchange_3 = [0,0,0,0,1] # z = [1,0,1,0,1]



## 12: (Problem 12) Exchange Lemma for Vectors over GF(2)
# Please give the name of the vector you want to replace as a string (e.g. 'v1')

replace_1 = 'v3' # A = {v1,v4}, z = (0, 0, 0, 1, 1, 0, 0, 0)
replace_2 = 'v1' # A = {v2,v3}, z = (0, 0, 1, 1, 0, 0, 0, 0)
replace_3 = 'v1' # A = {v2,v3}, z = (1, 0, 0, 0, 1, 0, 0, 0)



## 13: (Problem 13) rep2vec
def rep2vec(u, veclist):
    '''
    Input:
        - u: a Vec whose domain is set(range(len(veclist)))
        - veclist: a list of Vecs
    Output:
        the Vec whose coordinate representation is u
        (i.e u[0] is the coefficient of veclist[0], u[1] is the coefficient of veclist[1], etc.)
    Example:
        >>> v0 = Vec({'a','b','c','d'}, {'a':1})
        >>> v1 = Vec({'a','b','c','d'}, {'a':1, 'b':2})
        >>> v2 = Vec({'a','b','c','d'}, {'c':4, 'd':8})
        >>> rep2vec(Vec({0,1,2}, {0:2, 1:4, 2:6}), [v0,v1,v2]) == Vec({'d', 'a', 'c', 'b'},{'a': 6, 'c': 24, 'b': 8, 'd': 48})
        True
        >>> rep2vec(Vec({0,1,2}, {0:2, 1:4}), [v0, v1, v2]) == Vec({'d', 'a', 'c', 'b'},{'a': 6, 'c': 0, 'b': 8, 'd': 0})
        True
    '''
    # rep2vec(u, veclist):
    return coldict2mat(veclist) * u



## 14: (Problem 14) vec2rep
def vec2rep(veclist, v):
    '''
    Input:
        - veclist: a list of Vecs
        - v: a Vec in the span of set(veclist)
    Output:
        the Vec u whose domain is set(range(len(veclist))) that is the coordinate representation of v with respect to veclist
    Example:
        >>> v0 = Vec({'a','b','c','d'}, {'a':2})
        >>> v1 = Vec({'a','b','c','d'}, {'a': 16, 'b':4})
        >>> v2 = Vec({'a','b','c','d'}, {'c':8})
        >>> v = Vec({'d', 'a', 'c', 'b'},{'a': -1, 'c': 10, 'b': -1})
        >>> vec2rep([v0,v1,v2], v)  == Vec({0, 1, 2},{0: 1.5, 1: -0.25, 2: 1.25})
        True
    '''
    # vec2rep(veclist,v)
    return solve(coldict2mat(veclist),v)

## 15: (Problem 15) Superfluous Vector in Python
def is_superfluous(S, v):
    '''
    Input:
        - S: set of vectors as instances of Vec class
        - v: vector in S as instance of Vec class
    Output:
        True if the span of the vectors of S is the same as the span of the vectors of S, excluding v.
        False otherwise.
    Examples:
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> S = {Vec(D, {'a':1,'b':-1}), Vec(D, {'c':-1,'b':1}), Vec(D, {'c':1,'d':-1}), Vec(D, {'a':-1,'d':1}), Vec(D, {'b':1, 'c':1, 'd':-1})}
    >>> is_superfluous(S,Vec(D, {'b':1, 'c':1, 'd':-1}))
    False
    >>> is_superfluous(S,Vec(D, {'a':-1,'d':1}))
    True
    >>> is_superfluous(S,Vec(D, {'c':1,'d':-1}))
    True
    >>> S == {Vec(D,{'a':1,'b':-1}),Vec(D,{'c':-1,'b':1}),Vec(D,{'c':1,'d':-1}),Vec(D, {'a':-1,'d':1}),Vec(D,{'b':1, 'c':1, 'd':-1})}
    True
    >>> is_superfluous({Vec({0,1}, {})}, Vec({0,1}, {}))
    True
    >>> is_superfluous({Vec({0,1}, {0:1})}, Vec({0,1}, {0:1}))
    False
    >>> from GF2 import one
    >>> from vecutil import list2vec
    >>> S = {list2vec(v) for v in [[one,0,0,0],[0,one,0,0],[0,0,one,0],[0,0,0,one],[one,one,one,0]]}
    >>> is_superfluous(S, list2vec([one,0,0,0]))
    True
    >>> is_superfluous(S, list2vec([one,one,one,0]))
    True
    >>> is_superfluous(S, list2vec([0,0,0,one]))
    False
    '''
    if v not in S or v.is_almost_zero():
        return True
    if len(S) == 1:
        return False
    T = S.copy()
    T.remove(v)
    u = vec2rep(list(T), v)
    return (v -  rep2vec(u, list(T))).is_almost_zero()

## 16: (Problem 16) is_independent in Python
def is_independent(S):
    '''
    Input:
        - S: a set of Vecs
    Output:
        - boolean: True if vectors in S are linearly independent
    Examples:
    >>> is_independent(set())
    True
    >>> is_independent({Vec({'a'},{})})
    False
    >>> is_independent({Vec({'a'},{'a':1})})
    True
    >>> is_independent({list2vec(v) for v in [[1,2,1],[2,1,2],[1,1,1]]})
    False
    >>> is_independent({list2vec(v) for v in [[1,2,1],[2,1,2],[1,1,0]]})
    True
    >>> from GF2 import one
    >>> from vecutil import list2vec
    >>> is_independent({list2vec(v) for v in [[one,one,0],[0,one,one],[one,0,one],[one,0,0]]})
    False
    >>> is_independent({list2vec(v) for v in [[one,one,0,0,0],[0,one,0,0,one],[0,0,one,one,0],[0,0,0,one,one],[one,0,0,0,one]]})
    False
    >>> is_independent({list2vec(v) for v in [[one,one,0,0,0],[0,one,one,0,0],[0,0,one,one,0],[0,0,0,one,one]]})
    True
    '''
    for v in S:
      if is_superfluous(S, v):
         return False
    return True


## 17: (Problem 17) Exchange Lemma in Python
def exchange(S, A, z):
    '''
    Input:
        - S: a set of Vecs (not necessarily linearly independent)
        - A: a set of Vecs, a proper subset of S
        - z: an instance of Vec such that A | {z} is linearly independent
    Output: a vector w in S but not in A such that Span S = Span ({z} | S - {w})
    Examples:
        >>> from vecutil import list2vec
        >>> from vec import Vec
        >>> S = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]}
        >>> A = {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]}
        >>> z = list2vec([0,2,1,1])
        >>> (exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})) or (exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 1, 1: 2, 2: 3, 3: 4}))
        True
        >>> S == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]}
        True
        >>> A == {list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]}
        True
        >>> z == list2vec([0,2,1,1])
        True
        >>> S = {Vec({0,1,2,3,4}, {i:one, (i+1)%5:one}) for i in range(5)}
        >>> A = {list2vec([0,one,one,0,0]),list2vec([0,0,one,one,0])}
        >>> z = list2vec([0,0,one,0,one])
        >>> exchange(S, A, z) in {list2vec(v) for v in [[one, one,0,0,0],[one,0,0,0,one],[0,0,0,one,one]]}
        True
        >>> from The_Basis_problems import exchange
        >>> from vec import Vec
        >>> from GF2 import one
        >>> D = {0,1,2,3}
        >>> S = {Vec(D,{0:one, 2:one}), Vec(D,{0:one, 1:one, 2:one, 3:one}), Vec(D,{0:one, 1:one}), Vec(D,{0:one, 1:one, 2:one})}
        >>> A = {Vec(D,{0:one, 1:one, 2:one})}
        >>> z = Vec(D,{1:one})
        >>> exchange(S, A, z) == Vec(D,{0:one, 2:one})
        True
        >>> D = {0,1,2,3,4}
        >>> S = {Vec(D,{3:one}), Vec(D,{0:one, 4:one}), Vec(D,{0:one, 2:one, 3:one, 4:one}), Vec(D,{1:one, 2:one, 3:one, 4:one}), Vec(D,{0:one, 1:one, 2:one}), Vec(D,{0:one, 1:one, 4:one})}
        >>> A = {Vec(D,{0:one, 4:one}), Vec(D,{1:one, 2:one, 3:one, 4:one}), Vec(D,{3:one}), Vec(D,{0:one, 1:one, 2:one})}
        >>> z = Vec(D,{1:one, 3:one, 4:one})
        >>> exchange(S, A, z)== Vec(D,{0:one, 2:one, 3:one, 4:one})
        True
        >>> exchange(S, A, z)==Vec(D,{0:one, 2:one, 3:one, 4:one})
        True
    '''
    # if not is_independent(A|{z}): return None
    # Output: a vector w in S but not in A such that Span S = Span ({z} | S - {w})
    # solve, is_superfluous
    for w in S:
      if w not in A and is_superfluous({z} | S, w):
          return w
    return w

    #T = S.copy()
    #T.add(z)
    #for vec in T:
    #    if vec not in A and vec != z and is_superfluous(T, vec):
    #        return vec

