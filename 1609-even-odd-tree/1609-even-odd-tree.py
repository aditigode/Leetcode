# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        q = collections.deque()
        q.append([root])
        level = 0
        while q:
            nodeList = q.popleft()
            prev = None
            levelNodes = []
            #print(level,len(nodeList))
            for node in nodeList:
                # if level is even
                if node and level % 2 == 0:
                    # nodes should be in strictly increasing order
                    if node.val % 2 != 0 and (not prev or prev.val < node.val):
                        if node.left:
                            levelNodes.append(node.left)
                        if node.right:
                            levelNodes.append(node.right)
                        prev = node
                        
                    else:
                        #print(level,node,q,"even",node.val,prev.val)
                        return False
                    

                # if level is odd
                elif node and level % 2 != 0:
                    # nodes should be in stricly decreasing order
                    if node.val %2 == 0 and (not prev or prev.val > node.val):
                        if node.left:
                            levelNodes.append(node.left)
                        if node.right:
                            levelNodes.append(node.right)
                        prev = node
                        
                    else:
                        #print(level,node,q,"odd",node.val,prev.val)
                        return False
            
            if levelNodes:
                q.append(levelNodes)
            level += 1
        return True
                
            
            