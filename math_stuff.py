import math
from sympy.solvers import solve
from sympy import Symbol
from math import sqrt, cos, sin
import struct

def inter_line_circle(p, v, c, r):
    xa, ya = p
    vxa, vya = v 
    cx, cy = c
    x1 = (-vxa*ya + vxa*(-vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)) + vya*xa)/vya
    y1 = -vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)
    x2 = (-vxa*ya + vxa*(vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)) + vya*xa)/vya
    y2 = vya*sqrt(-cx**2*vya**2 + 2*cx*cy*vxa*vya - 2*cx*vxa*vya*ya + 2*cx*vya**2*xa - cy**2*vxa**2 + 2*cy*vxa**2*ya - 2*cy*vxa*vya*xa + r**2*vxa**2 + r**2*vya**2 - vxa**2*ya**2 + 2*vxa*vya*xa*ya - vya**2*xa**2)/(vxa**2 + vya**2) + (cx*vxa*vya + cy*vya**2 + vxa**2*ya - vxa*vya*xa)/(vxa**2 + vya**2)
    return (x1, y1), (x2, y2)

def normal_vector_line_on_point_circle(p,c):
    return p[0] - c[0], p[1] - c[1]

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def normalize(v):
    length = math.sqrt(v[0]**2 + v[1]**2)
    return v[0] / length, v[1] / length

def fast_sqrt(number):
    threehalfs = 1.5
    x2 = number * 0.5
    y = number
    
    packed_y = struct.pack('f', y)       
    i = struct.unpack('i', packed_y)[0]  # treat float's bytes as int 
    i = 0x5f3759df - (i >> 1)            # arithmetic with magic number
    packed_i = struct.pack('i', i)
    y = struct.unpack('f', packed_i)[0]  # treat int's bytes as float
    
    y = y * (threehalfs - (x2 * y * y))  # Newton's method
    return y 