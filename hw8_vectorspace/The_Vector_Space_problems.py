# version code 565cc389e900+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec, scalar_mul, add
from GF2 import one
from itertools import product # Suggestion from Vadim Bielikov


## 1: (Problem 1) Vector Comprehension and Sum
def vec_select(veclist, k):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [Vec(v.D, v.f) for v in veclist if v[k] == 0 ]

def vec_sum(veclist, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    return Vec(D, {}) if len(veclist) == 0 else sum(veclist)

def vec_select_sum(veclist, k, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return vec_sum(vec_select(veclist,k),D)

## 2: (Problem 2) Vector Dictionary
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,4}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> result = scale_vecs({3: v1, 5: v2})
    >>> len(result)
    2
    >>> [v in [Vec({1,2,4},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})] for v in result]
    [True, True]
    '''
    return [scalar_mul(vecdict[i], 1./i) for i in vecdict.keys()]

## 3: (Problem 3) Constructing span of given vectors over GF(2)
def GF2_span(D, S):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> S = [Vec(D, {'a': one, 'c' :one}), Vec(D, {'b':one})]
    >>> len(GF2_span(D,S))
    4

    >>> GF2_span(D, {Vec(D, {'a':one, 'c':one}), Vec(D, {'c':one})}) == {Vec({'a', 'b', 'c'},{}), Vec({'a', 'b', 'c'},{'a': one, 'c': one}), Vec({'a', 'b', 'c'},{'c': one}), Vec({'a', 'b', 'c'},{'a': one})}
    True

    >>> GF2_span(D, {Vec(D, {'a': one, 'b': one}), Vec(D, {'a':one}), Vec(D, {'b':one})}) == {Vec({'a', 'b', 'c'},{'a': one, 'b': one}), Vec({'a', 'b', 'c'},{'b': one}), Vec({'a', 'b', 'c'},{'a': one}), Vec({'a', 'b', 'c'},{})}
    True

    >>> S={Vec({0,1},{0:one}), Vec({0,1},{1:one})}
    >>> GF2_span({0,1}, S) == {Vec({0, 1},{0: one, 1: one}), Vec({0, 1},{1: one}), Vec({0, 1},{0: one}), Vec({0, 1},{})}
    True

    '''
    '''
    pseudo code:
    1.create a list of lists(of len S) of all possible combinations of 0 and ones. (use itertools.product)
    2.create a convert_list by converting set S to a list
    3.create an empty result set
    4.create an empty sum set  -- this will be used to add vectors multiplied by possible combinations of zeros and ones
    5 iterate over each combination in a combinations list
        iterate over a list of indexes in a combination
           multiply current element of convert_list by current element in current combination list
        add a sum of vectors in a sum_set to a result set
        you need to reset the sum_set
    and now you have a result set to return
'''
    #if len(S) == 0: 
    #    return Vec(D,{})
    # r = set()
    # for i in product({0,one}, repeat=len(S)):
    #     r.append(sum([u*v for (u,v) in zip(i,S)]))
    # return r
    #return [sum([a*v for (a,v) in zip(i,S)]) for i in product({0,one},repeat=len(S))] if len(S) !=0 else Vec(D,{})
    # probably spent eight hours trying to grok this;  simple solution hantempo
    if len(S) == 0:
        return {Vec(D,{})}
    r = set()
    s = S.copy()
    k = s.pop()
    s = GF2_span(D, s)
    r.update(s)
    r.update({v + k for v in s})
    return r


## 4: (Problem 4) Is it a vector space 1
# {[x,y,z] : x,y,z in R and x+y+z = 1
is_a_vector_space_1 = False

## 5: (Problem 5) Is it a vector space 2
# {[x,y,z] : x,y,z in R and x+y+z = 0
is_a_vector_space_2 = True

## 6: (Problem 6) Is it a vector space 3
# {[x1,x2,x3,x4,x5] : x1,x2,x3,x4,x5 in R, x2 = 0 or x5=0 is vector space
is_a_vector_space_3 = False

## 7: (Problem 7) Is it a vector space 4
# V is the set of 5-vectors over GF(2) that have an even number of 1s
is_a_vector_space_4a = True
# V is the set of 5-vectors over GF(2) that have an odd number of 1s
is_a_vector_space_4b = False

