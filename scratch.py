import copy
from solve import Solve

class Triangle:
    corners = (0,0,0)
    values = (0,0,0)
    isEmpty = True

    def __init__(self, corns):
        self.corners = corns

    def setValues(self, vals):
        self.isEmpty = False
        self.values = vals

## Runtime variables

## All the triangles
START_CORNERS= [(1,3,7),(1,7,11),(1,2,11),(1,2,4),(1,3,4),(3,4,9),(4,9,12),(2,4,12),(3,5,9),(5,8,9),(8,9,12),(3,5,7),(5,6,7),(5,6,8),(8,10,12),(2,10,12),(6,10,11),(6,7,11),(6,8,10),(2,10,11)]
START_PIECES = [(0,1,2),(1,2,3), (1,2,3), (0,0,0),(1,2,3),(1,1,1),(1,2,3), (0,1,2), (0,0,3),(0,3,3),(0,0,1), (0,0,2),(0,1,2),(0,1,2),(3,3,3),  (0,1,2),  (0,2,2),  (2,2,2), (0,1,2), (1,1,0)]

## Creating the triangle list
START_TRIANGLES = []
for cval in START_CORNERS:
    START_TRIANGLES.append(Triangle(cval))

Solve(START_TRIANGLES, START_PIECES)
