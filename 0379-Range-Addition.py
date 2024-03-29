# https://baihuqian.github.io/2018-08-16-range-addition/
# https://www.cnblogs.com/grandyang/p/5628786.html
# lc plus question

"""
Assume you have an array of length n initialized with all 0’s and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex … endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:

    [-2, 0, 3, 5, 3]

Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]

"""
class Solution:
    def getModifiedArray(int length, list updates):
        ans = [0]*length
        for i in range(len(updates)):
            ans[updates[i][0]] = updates[i][-1] #mark the start position
            if (ans[updates[i][1]] < length):
                ans[updates[i][1]] = -updates[i][-1] # mark end position -= val
        # then we iterate the arr and add the val num into the next idx
        for i in range(1, length):
            ans[i] = ans[i-1]
     return ans
"""
    Thinking of using advanced data structures? You are thinking it too complicated.
For each update operation, do you really need to update all elements between i and j?
Update only the first and end element is sufficient.
The optimal time complexity is O(k + n) and uses O(1) extra space.
    """

for i in range
