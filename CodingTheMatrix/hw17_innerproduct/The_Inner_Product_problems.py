# version code 3ebd92e7eece+
coursera = 1
from orthogonalization import *
from vec import *
from vecutil import *
from mat import *
from matutil import *
from math import sqrt
# Please fill out this stencil and submit using the provided submission script.

def norm(l):
   return sqrt(sum((i*i) for i in l))

## 1: (Problem 1) Norm; simply sqrt(sum(v[i]^2) for i 
norm1 = norm([2, 2, 1]) # [2,2,1]
norm2 = norm([ sqrt(2), sqrt(3), sqrt(5), sqrt(6) ])
norm3 = norm([1,1,1,1,1,1,1,1,1])

## 2: (Problem 2) Closest Vector
# Write each vector as a list
closest_vector_1 = [1.6, 3.2]
closest_vector_2 = [0,1,0] 
closest_vector_3 = [3, 2, 1, -4]

## 3: (Problem 3) Projection Orthogonal to and onto Vectors
# Write each vector as a list
# round up to 6 decimal points if necessary
project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1] # vec2list(project_orthogonal(list2vec([2,1]),[list2vec([3,0])]))
project_onto_2 = [-1.0/6, -2.0/6, 1.0 / 6 ] #
projection_orthogonal_2 = [7.0 / 6, 8.0 / 6, 23.0 / 6] # vec2list(project_orthogonal(list2vec([1.,1.,4.]),[list2vec([1,2,-1])]))
project_onto_3 = [1, 1, 4]
projection_orthogonal_3 = [0,0,0] # vec2list(project_orthogonal(list2vec([1.,1.,4.]),[list2vec([3,3,12])]))

#print("p1",project_onto_1)
#print("p1",projection_orthogonal_1)
#print("p2",project_onto_2)
#print("p2",projection_orthogonal_2)
#print("p3",project_onto_3)
#print("p3",projection_orthogonal_3)
