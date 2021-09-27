# https://leetcode.com/discuss/interview-question/901091/how-to-write-an-efficient-solution-for-this-challenge-portfolio-balances-hackerrank

"""
An investor opens a new account and wants to invest in a number of assets. Each asset begins with a balance of 0, and its value is stored in an array using 1-based indexing. Periodically, a contribution is received and equal investments are made in a subset of the portfolio.Each contribution will be given by investment amount, start index, end index. Each investment in that range will receive the contribution amount. Determine the maximum amount invested in any one investment after all contributions.

For example, start with an array of 5 elements (n = 5): investments = [0, 0, 0, 0, 0]. The variables left and right represent the starting and ending indices, inclusive. Another variable, contribution, is the new funds to invest per asset. The first investment is at index 1.

left    right   contribution              investments array

											[  0,  0,  0,  0,  0]
1          2        10                      [ 10, 10,  0,  0,  0]
2          4         5                      [ 10, 15,  5,  5,  0]
3          5        12                      [ 10, 15, 17, 17, 12] 
In the first round, a contribution of 10 is made to investments 1 and 2. In the second round, a contribution of 5 is made to assets 2, 3 and 4. Finally, in the third round, a contribution of 12 is added to investments 3, 4 and 5. The maximum invested in any one asset is 17

*Note: The investments array is not provided in the function. It is to be created after the number of assets available is known.

Function Description:
Complete the maxValue function:

maxValue has the following parameters:
int n = the number of investments available
List<List<int>> rounds = each rounds[i] contains a list of 3 integers: [left, right, contribution]

maxValue returns int = the maximum invested in any one asset
"""

def maxValue(n, rounds):
    # Write your code here
    investments = [0]*n
 
    starts = []
    stops = []
    amount = []
    # print(n, rounds)
    for roun in rounds:
        left, right, amount = roun[0], roun[1], roun[2]
        # print(left, right, amount)
        for i in range(left-1, right):
            investments[i] += amount
 
    return max(investments)
maxValue(5,[(1, 2, 10), (2, 4, 5), (3, 5, 12)])

# another solution
import itertools
def maxValue(n, rounds):
    investments = [0]*(n+1)
    for start, end, amount in rounds:
        investments[start-1] += amount
        investments[end] -= amount
    investments = itertools.accumulate(investments) # shortcut for pref
    return max(investments)
maxValue(5,[(1, 2, 10), (2, 4, 5), (3, 5, 12)])