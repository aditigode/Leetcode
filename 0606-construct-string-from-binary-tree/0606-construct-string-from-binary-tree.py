# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def paranthesis(root):
            
            if root is None:
                return ""
            
            
            left_tree = paranthesis(root.left)
            right_tree = paranthesis(root.right)
            
            if left_tree and right_tree:
                return str(root.val) + '(' + left_tree + ')' + '(' + right_tree + ')'
            
            elif not left_tree and not right_tree:
                #print(root.val)
                return str(root.val)
            
            elif not left_tree:
                return str(root.val) + '()' + '(' + right_tree + ')'
            
            elif not right_tree:
                return str(root.val) + '(' + left_tree + ')'
        
        res = paranthesis(root)
        
        return res
        