#!/bin/python

import sys

"""
        sum of all coins
    --------------->
|
|
| coin value
|
|
V

n = 5
c = {1, 2, 3}

    1   2   3   4
1   1   1   1   1
2   1   2   2   
3

1 1 1 1
2 1 1
2




    c -> list of denominations ex:    $2    $3   $4
    note: assuming no duplicates

    n -> amount to make with some subset of our coins


"""

def getWays(n, c):
    c.sort()                    # put our denominations in order
    subsets = []                # matrix: i := subset possible with c[0, i+1], j := n - (n - j)
    for denomination in range(0, len(c)):
        subsets.append([])
        for subamount in range(0, n+1):
            subsets[denomination].append(0)
    _populate_first_row(subsets, c[0])
    # 3 cases:
    #    1. subamount is less than highest coin in coin_set, therefore the 
    #    subset's cardinality is the subset for subamount without highest coin (i-1) 
    #    2. subamount is a multiple of the highest coin -> subamount % highest_coin = 0 
    #    There is 1 way to make subamount
    #    3. for each denomination in range(coins, -1, -1), 
    #        if subsets[denomination][subamount - denomination] is in the subsets matrix:
    #            subsets[denomiation][subamount] += subsets[denomination][subamount - denomination]
    #
    for d in range(1, len(c)):
        for amount in range(1, n+1):
            _subset_total(subsets, amount, d, c[0:d+1])
    return subsets[len(c) - 1][n]


def _populate_first_row(subsets, smallest_coin):
    # populate first row
    for sub_amount in range(1, n+1):
        if sub_amount % smallest_coin == 0:
            subsets[0][sub_amount] = 1
    return subsets

def _subset_total(subsets, amount, largest_coin, coins): 
    if amount < coins[largest_coin]:
        subsets[largest_coin][amount] = subsets[largest_coin-1][amount]
    else:
        if amount == coins[largest_coin]:
            subsets[largest_coin][amount] += 1
        subsets[largest_coin][amount] += subsets[largest_coin-1][amount]  # all the ways to make amount with l_coin
        subamount = amount - coins[largest_coin]
        subsets[largest_coin][amount] += subsets[largest_coin][subamount]

             
        
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units 
# using coins having the values given by 'c'
ways = getWays(n, c)
print ways
