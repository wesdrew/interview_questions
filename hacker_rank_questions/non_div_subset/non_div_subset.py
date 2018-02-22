#!/bin/python

import sys

########################################################################
# k divides a + b if:                                                  #
#                                                                      #
#     a % k = 0                                                        #
#     b % k = 0                                                        #
#                                                                      #
#     4 % 3 = 1                                                        #
#     5 % 3 = 2                                                        #
#                                                                      #
#     (4 + 5) % 3 = 0                                                  #
#                                                                      #
#     so if the sum of a % k and b % k is k, it is also divisable.     #
#                                                                      #
#     Use a dict with key : value pair of (a_i % k) : a                #
#                                                                      #
#     the size of the maximal subset where no two members are divisble #
#     by k excludes:                                                   #
#                                                                      #
#                                                                      #
#   
########################################################################


# maps residual r to the number of integers where integer % k = r

def get_residual_subset_sizes(k, arr):
    d = dict()
    for i in range(0, k):
        d[i] = list()
    for int in arr:
        d.get(int % k).append(int)
    for i in range(0, k):
        d[i] = len(d[i])        # only need the size of subset
    return d
    

###################################################################
# 1. get len of lists of integers                                 #
# 2. add largest list to set                                      #
# 3. for index of that list, disqualify all ints less than k that #
#     index + int = k                                             #
###################################################################


def indivisable_set_size(residual_set_sizes, k):
    size = 0
    # we can add only one element from the set of numbers that are divided cleanly by k
    if residual_set_sizes[0] > 0:
        size += 1
    # if k is even, only one element can come from set[k / 2]
    if k % 2 == 0:
        size += 1
    for i in range(1, (k+1)/2):                              # double check this
        size += max(residual_set_sizes[i], residual_set_sizes[k-i])
    return size


def nonDivisibleSubset(k, arr):
    # Complete this function
    subset_sizes = get_residual_subset_sizes(k, arr)
    return indivisable_set_size(subset_sizes, k)

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = nonDivisibleSubset(k, arr)
    print result
