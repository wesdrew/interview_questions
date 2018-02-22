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


sample:

    2 2
    1 2


    ______
    |x o |
    | o  |
    | x  |
    |____|     

    ______
    | x  |
    |o   |
    |o   |
    |____|     


    ______
    |x o |
    |    |
    |o   |
    |____|     

    ______
    | x  |
    |o   |
    |p   |
    |____|     
                  1 2 0 
    ______        1 1 1
    |x o |        1 1 1
    |p   |
    |    |
    |____|     






"""


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


