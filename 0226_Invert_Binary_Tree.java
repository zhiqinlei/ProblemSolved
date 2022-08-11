/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null){
            return null;
        }
        
        final Deque<TreeNode> stack = new LinkedList<>(); // deque as stack
        stack.push(root);
        while(!stack.isEmpty()){ // must use isEmpty()
            final TreeNode node = stack.pop();
            final TreeNode tmp = node.left;
            node.left = node.right;
            node.right = tmp;    
            
            if (node.left != null) { // inside the loop
                stack.push(node.left);
            }
            if (node.right != null) {
                stack.push(node.right);
            }
        }
        
        return root;
    }
}