# premium question
# https://blog.csdn.net/qq_37821701/article/details/108821029
# https://baihuqian.github.io/2018-08-02-sparse-matrix-multiplication/

"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A’s column number is equal to B’s row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

"""

# two methods to solve, brutal force and hashmap

"""
brutal force C[i][k] += A[i][j]*B[j][k]

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(B) == 0:
            return [[]]

        a, c, b = len(A), len(B), len(B[0])
        AB = [[0 for _ in range(b)] for _ in range(a)]

        for i in range(a):
            for j in range(c):
                if A[i][j] != 0:
                    for k in range(b):
                        if B[j][k] != 0:
                            AB[i][k] += A[i][j] * B[j][k]

        return AB

"""

"""
use dictionary to store non-zero elements in A
"""
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        l = len(A[0])
        n = len(B[0])
        ret = [[0 for col in range(n)] for row in range(m)]
        dic = {}
        # final all nonzero elements in A
        for i in range(m):
            tmp = {}
            for j in range(l):
                if A[i][j] != 0:
                    tmp[j] = A[i][j]
            dic[i] = tmp
        # compute matrix multiplication
        for i in range(m):
            tmp = dic.get(i)
            for j, val in tmp.items():
                for k in range(n):
                    ret[i][k] += val * B[j][k]
        return ret
