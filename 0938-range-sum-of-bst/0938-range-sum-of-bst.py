# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if root is None:
            return 0
        
        total = 0
        if low <= root.val <= high:
            total += root.val
            
        if low < root.val:
            total += self.rangeSumBST(root.left,low,high)
            
        if high > root.val:
            total += self.rangeSumBST(root.right,low,high)
        #print(total,root.val)
        return total
            
                
                
        