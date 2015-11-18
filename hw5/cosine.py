#!/usr/bin/env python
"""
Author: Chang Liu
Description: For calculating the cosine value of three vectors
"""
import math

A = (1.5, 2.5, 0, 2.5, -1.5, 0, 0.5, -0.5)
B = (0, 1.25, 2.25, 1.25, -0.75, 0.25, -0.75, 0)
C = (-0.25, 0, -1.25, 0.75, 0, 1.75, 2.75, 0.75)

def distance(A):
    size = len(A)
    i = 0
    sum = 0
    while i < size:
        sum += A[i] * A[i]
        i += 1
    return math.sqrt(sum)

def multiply(A, B):
    sum = 0
    size = len(A)
    i = 0
    while i < size:
        sum += A[i] * B[i]
        i += 1
    return sum

if __name__=='__main__':
    cosAB = multiply(A, B) / distance(A) / distance(B)
    cosBC = multiply(B, C) / distance(B) / distance(C)
    cosAC = multiply(A, C) / distance(A) / distance(C)
    print cosAB, cosBC, cosAC
