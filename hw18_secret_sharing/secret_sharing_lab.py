# version code 3ebd92e7eece+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec



## 1: (Task 1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    pass



## 2: (Task 2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
secret_a0 = ...
secret_b0 = ...
secret_a1 = ...
secret_b1 = ...
secret_a2 = ...
secret_b2 = ...
secret_a3 = ...
secret_b3 = ...
secret_a4 = ...
secret_b4 = ...

