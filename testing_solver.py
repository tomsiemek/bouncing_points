from sympy.solvers import solve
from sympy import Symbol, N
from math import sqrt
#x = Symbol('x')
#dwa = 2
#jeden = 1
#sol = solve(x**dwa - jeden, x)
#print(sol)

def inter_line_circle():
    x = Symbol('x')
    y = Symbol('y')
    xa = Symbol('xa')
    vxa = Symbol('vxa')
    ya = Symbol('ya')
    vya = Symbol('vya')
    cx = Symbol('cx')
    cy = Symbol('cy')
    r = Symbol('r')
    sol = solve([((x-xa)/vxa) - ((y-ya)/vya), (x-cx)**2 + (y-cy)**2 - r**2], x, y)
    return sol

def givedd(p,v,c,r):
    xa, ya = p
    vxa, vya = v
    cx, cy = c
    x1 = (-vxa*ya + vxa*(-vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)) + vya*xa)/vya
    y1 = -vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)
    x2 = (-vxa*ya + vxa*(vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)) + vya*xa)/vya
    y2 = vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)
    return (x1, y1), (x2, y2)

def styczna():
    #xa, ya = p
    #cx, cy = c
    x = Symbol('x')
    y = Symbol('y')
    xa = Symbol('xa')
    ya = Symbol('ya')
    cx = Symbol('cx')
    cy = Symbol('cy')
    r = Symbol('r')
    return solve((xa - cx)*(x - cx) + (ya - cy)*(y - cy) - r**2, y)

print(styczna())
#sol = inter_line_circle()
#print(sol)
#for a in sol:
#   for b in a:
#        print(b)
#        print("--------------")