# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we can use recursive to solve this problem 
        # cn lc soltuion: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/cong-qian-xu-yu-zhong-xu-bian-li-xu-lie-gou-zao-9/
        # lc solution: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
        
        # preorder: [root, leftchildren, rightchildren]
        # inorder: [leftchildren, root, rightchildren] we need to find the index of root in inorder
        # then we can recurvisely build left and right children
        
        """
        if not inorder:
            return None
        
        root_idx = inorder.index(preorder.pop(0)) # the root of preorder must be the first element
        # we can build the tree if we know the root
        root = TreeNode(inorder[root_idx])
        # then we recursivley build left and right child
        root.left = self.buildTree(preorder, inorder[:root_idx]) # since preorder pop the first element, the remaining first element must be the root of left children
        root.right = self.buildTree(preorder, inorder[root_idx+1:]) # since we pop all left children, the remaining must be the root of right children
        
        return root
        """
    
    # time ON space ON
    
    # since [] is a shallow copy, which will duplicate the slice. we could use four pointer to save space
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

        # time ON Space ON