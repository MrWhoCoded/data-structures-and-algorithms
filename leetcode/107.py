from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue, stack = [], []
        traversal = []
        queue.append(root)
        
        while queue:
            level = []

            for i in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                
            stack.append(level)
            
        while stack:
            traversal.append(stack.pop())
            
        return traversal        
    

prob = Solution()
print(prob.levelOrderBottom(3))
            