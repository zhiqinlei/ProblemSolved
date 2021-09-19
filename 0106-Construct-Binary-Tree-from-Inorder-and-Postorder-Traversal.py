# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: [leftchildren, root, rightchildren], postorder: [leftchildren, rightchildre, root]
        # similar to 105, we can use recursive to solve this problem, just choose rightest element instead of leftest
        # do not use slice [], because it wastes time and space
        # lc solution: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why.
        # lc ch solution: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/cong-zhong-xu-yu-hou-xu-bian-li-xu-lie-gou-zao-14/
        
        """
        idx_map = {val:idx for idx, val in enumerate(inorder)} # build a val to idx map to save time
        
        def helper(inorder_left, inorder_right):
            if inorder_left > inorder_right: # exit
                return None
            
            val = postorder.pop() # pop the rightest element which is the root val
            root = TreeNode(val) # build the tree
            
            root_idx = idx_map[val] # find the root idx
            root.right = helper(root_idx +1, inorder_right) # build right children first, because the rightest element is root of right children
            root.left = helper(inorder_left, root_idx-1)
            
            return root
        
        return helper(0, len(inorder)-1) # must be length -1
    
    # time ON space ON
    """
    
    # another way to avoid destory postorder
        dict_inorder = {v:i for i, v in enumerate(inorder)}
        self.index = 1
        def build(idx_left, idx_right):
            if idx_left > idx_right:
                return None
            root = TreeNode(postorder[-self.index])
            self.index += 1
            idx_root = dict_inorder[root.val]
            root.right = build(idx_root+1, idx_right)
            root.left = build(idx_left, idx_root-1)
            return root
        return build(0, len(inorder)-1)