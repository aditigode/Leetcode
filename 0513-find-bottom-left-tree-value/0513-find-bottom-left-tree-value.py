# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
        q = collections.deque()
        q.append(root)
        leftmost = None
        while q:
            qLen = len(q)
            leftmost = None
            #level = []
            #print(qLen,leftmost)
            for i in range(qLen):
                node = q.popleft()
                if leftmost is None:
                    leftmost = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        #print(leftmost)
        return leftmost
                    