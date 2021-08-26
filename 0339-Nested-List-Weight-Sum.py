"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list – whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1’s at depth 2, one 2 at depth 1.

Example 2:

Input: [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""
# https://zhenyu0519.github.io/2020/03/16/lc339/
# lc plus
# use dfs to solve

"""
This question can be solved by Depth First Search.

Weight sum is level depth times sum. We will go throught the list, if the element is digit, we sum up. If element is list, we use dfs to get into new depth and go through the new list again. The depth is start from 1.


"""

def depthSum(self, nestedList: List[NestedInteger]) -> int:
    def dfs(nestedList, depth):
        temp_sum = 0
        for element in nestedList:
            if element.isInteger(): # if the element is integer, add it to the sum
                temp_sum += int(element) * depth 
            else: # element is a list
                dfs(element, depth+1) # go to the next level
        return temp_sum # need to return because we have to add it into summ

    return dfs(nestedList, 1) # base level is 1

"""
Time complexity analysis
O(N). N is the total number of nested elements, which is the number of items the algotrithm has to iterate in total.

Space complexity analysis
O(D). D is maximum depth, which is times we call the getDepthSum() function.
"""