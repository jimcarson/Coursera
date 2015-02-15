# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    return [ ((A[i][j]+B[i][j],A[i][j+1]+B[i][j+1])) for i in range(0,len(A)) for j in range(0,len(A[i]),2) if len(A) > 0]

# print( tuple_sum([(1,2), (10,20)],[(3,4), (30,40)]))

## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
    return { v:k for k, v in d.items()}


## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [ p+i for i in range(n) ]

comprehension_with_row = [row(i,20) for i in range(15) ]
comprehension_without_row = list([j+i for j in range(20)] for i in range(15) )
# print(comprehension_with_row )
# print(comprehension_without_row )



## 4: (Problem 4) Probability Exercise 1
Pr_f_is_even = (.5+.1+.1)
Pr_f_is_odd  = (.2+.1)



## 5: (Problem 5) Probability Exercise 2
Pr_g_is_1    = (.2+.1+.1)
Pr_g_is_0or2 = (.2+.1+.2+.1)


#147 1 = .2+.1+.1
#25  2 = .2+.1
#36  0 = .2+.1
