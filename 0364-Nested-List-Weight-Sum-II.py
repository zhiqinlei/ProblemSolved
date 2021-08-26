# https://zhenyu0519.github.io/2020/03/16/lc364/#bigo
# https://www.acwing.com/solution/LeetCode/content/9861/

# lc plus question

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list – whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Sample I/O
Example 1
Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2
Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
"""

# similar to 339, use dfs or bfs to solve

"""
This question can be solved by Depth First Search and it is similar with question 339. Nested List Weight Sum. This time is digit elements will be higher level than list elements.

Weight sum is level depth times sum. We first iterate all elements from the list, if the element is digit, we sum up. If element is list, we merge all list element into one list. After iterate all elements, we use dfs, to recursively find the sum of the new list, the level sum is previous sum plus the new list sum.


"""

# dfs 
def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    def dfs(nestedList, list_sum):
        temp_list = [] # use templist to record lists in this depth
        for elem in nestedList:
            if elem.isInteger():
                list_sum += elem.getInteger() # add all integer in this level
            else: # if elem is list, add to temp list
                temp_list += elem.getList()
        
        if len(temp_list) != 0: # if there is list in this depth
            dfs(temp_list, list_sum) # do dfs again, the list elem will be treat as integer and integer will be calculate again
        return list_sum
    return dfs( nestedList, 0)

# We traversal all elements of nested list so total time complexity is O(n) where n is the number of the elements

# BFS
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        res = 0
        Sum = 0

        while (len(nestedList) > 0):

            new_nestedList = []

            for ele in nestedList:
                if ele.isInteger():
                    Sum += ele.getInteger()
                else:
                    new_nestedList += ele.getList()

            nestedList = new_nestedList
            res += Sum

        return res
