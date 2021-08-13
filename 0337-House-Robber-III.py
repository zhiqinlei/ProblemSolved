# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # https://leetcode-cn.com/problems/house-robber-iii/solution/da-jia-jie-she-iii-by-leetcode-solution/
        # cn lc solution
        # dynamic solution
        
        def robRoot(node):
            #ls表示偷左子树能带来的最大收益，ln表示不偷左子树能带来的最大收益，rs、rn同理
            if not node:
                return (0,0) # base case
            
            left_stole, left_save = robRoot(node.left)
            right_stole, right_save = robRoot(node.right)
            
            now = node.val + left_save + right_save
            later = max(left_stole, left_save) + max(right_stole, right_save)
            
            return now, later #if stole root, save its children, else stole children
        
        return max(robRoot(root))
        # O(n) Time, O(n) space
