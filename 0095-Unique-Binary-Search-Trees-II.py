# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # we can use recursive to solve this problem
        # https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode-solut/
        # as a BST, left node must be less than root and right must be larger
        # we iterate n and choose n[i] as root. Thus, left child must be in 0 to i-1 and right in i+1 to end
        
        def helper(start, end): # use start and end to represent the idx slice of n
            if start > end: # must include this condition! it is the out of the loop
                return [None]
            
            allPossibleTrees = []
            
            for i in range(start, end+1): # choose i as root and divide left and right trees
                leftTrees = helper(start, i-1)
                rightTrees = helper(i+1, end)
                
                for l in leftTrees: # iterate left and right trees to add all possible child treenodes
                    for r in rightTrees:
                        curTree = TreeNode(i) # initilize root
                        curTree.left = l
                        curTree.right = r 
                        allPossibleTrees.append(curTree)
            return allPossibleTrees
        
        return helper(1, n) # start with 1, because n from 1 to n
    # time OnGn Space OnGn Gn is the num of tree 4n/n(3/2) , thus 4n/n(1/2)