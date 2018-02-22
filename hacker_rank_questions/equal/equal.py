#!/bin/python

import sys


"""

1 <= N <= 10000 -> range of possible chocolates to have 

recurrence relation:
    steps(1) = 1
    steps(2) = 1
    steps(5) = 1
    steps(N) = 1 + steps(N - k), where k is max(1,2,5) and N - k > 0


another way to do this:

    2 2 3 7 <- sort the chocolate holders

    0 0 1 5 <- subtract by the minimum in the list, now represents differences between
                holders

    0 0 1 (5) <- select the maximum, adding 1, 2, 5 to the other 3 will have the effect
                 of subtracting 1, 2, or 5 from the maximum
                in this case, we add 5 to the other holders (-5 from the maximum)

    0 0 (1) 0 <- add 1 to other holders (-1 from the maximum)

    0 0 0 0 <- chocolates are equalized!


"""

def equal(arr):
    steps = 0
    arr.sort()
    min = arr[0]
    for i in range(0, len(arr)):
        arr[i] = arr[i] - min
    diff = arr.index(max(arr))
    while arr[diff] != 0:
        rem = diff % 5
        steps += diff / 5
        steps += rem / 2
        steps += (rem % 2) / 1
        arr[diff] = 0
        diff = arr.index(max(arr)) # find new maximum in arr
    return steps
    

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = equal(arr)
        print result


