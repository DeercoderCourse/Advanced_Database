#!/usr/bin/env python
"""
Author: Chang Liu
Description: For calculating the cosine value of three vectors
"""
import math

A = (3.06, 500, 6)
B = (2.68, 320, 4)
C = (2.92, 640, 6)

alpha = 0.01
beta = 0.5

def distance(A, alpha, beta):
    sum = 1 * A[0] * A[0]
    sum += alpha * alpha * A[1] * A[1]
    sum += beta * beta * A[2] * A[2]
    return math.sqrt(sum)

def multiply(A, B, alpha, beta):
    sum = 1 * A[0] * B[0] + alpha * alpha * A[1] * B[1] + beta * beta * A[2] * B[2]
    return sum

if __name__=='__main__':
    cosAB = multiply(A, B, alpha, beta) / distance(A, alpha, beta) / distance(B, alpha, beta)
    cosBC = multiply(B, C, alpha, beta) / distance(B, alpha, beta) / distance(C, alpha, beta)
    cosAC = multiply(A, C, alpha, beta) / distance(A, alpha, beta) / distance(C, alpha, beta)
    print cosAB, cosBC, cosAC
