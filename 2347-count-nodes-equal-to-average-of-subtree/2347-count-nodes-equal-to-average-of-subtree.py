# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal res
            #print(node)
            if node is None:
                return 0,0
            total, count = dfs(node.left)
            temp1, temp2 = dfs(node.right)
            total = temp1 + total + node.val
            count = temp2 + count + 1
            #print(node.val, total, count)
            if count > 0 and total//count == node.val:
                res += 1
            return total,count
        res = 0
        dfs(root)
        return res

        
        