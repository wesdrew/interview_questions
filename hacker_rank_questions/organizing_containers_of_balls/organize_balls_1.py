#!/bin/python

import sys

"""

possible == 1. each container contains only balls of the same type
            2. no two balls of the same type are located in different 
               containers


input matrix:

                ball colors ->

container_id
    |
    |
    |
    V


Ah! This is just a test if the matrix is invertible!!


calculate determinant!

    determinant of 2*2 matrix : ad - bc   | a b |
                                          | c d |

    determinant of n*n matrix: j * det(minor_i,j) - j+1*det(minor_i,j+1) + j+2*det(minor_i, j+2)... 

"""

# sign flips from positive to negative on each call
def _determinant(coefficient, matrix):
    if len(matrix) is 2:
        return coefficient * (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    else:
        sum = 0
        sign = 1
        for j in range(0, len(matrix[0])):
            minor = _minor(matrix, j)
            sum += _determinant(matrix[0][j] * sign, minor)
            sign *= -1          # flip sign
        return sum

# return a submatrix that removes first row and jth column from matrix
def _minor(matrix, k):
    minor = list()
    for i in range(1, len(matrix)):
        minor.append(list())
        for j in range(0, len(matrix[0])):
            if j != k:
                minor[i-1].append(matrix[i][j])
    return minor


def organizingContainers(container):
    det = _determinant(1, container)
    if det:
        return "Possible"
    else:
        return "Impossible"


if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n = int(raw_input().strip())
        container = []
        for container_i in xrange(n):
            container_temp = map(int,raw_input().strip().split(' '))
            container.append(container_temp)
        result = organizingContainers(container)
        print result


