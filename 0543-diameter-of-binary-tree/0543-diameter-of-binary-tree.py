# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return -1
            else:
                LeftDepth = 1 + dfs(node.left)
                RightDepth = 1 + dfs(node.right)
                #print(LeftDepth,RightDepth,node.val)
                #gLeftDepth = max(gLeftDepth,LeftDepth)
                #gRightDepth = max(gRightDepth, RightDepth)
                ans = max(ans, LeftDepth+RightDepth)
                return max(LeftDepth,RightDepth)
                
        
        gLeftDepth = 0
        gRightDepth = 0
        dia = dfs(root)
        return ans