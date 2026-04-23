from typing import List, Optional
from collections import deque

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
    
def build_tree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] != "null":
            current.left = TreeNode(int(values[i]))
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] != "null":
            current.right = TreeNode(int(values[i]))
            queue.append(current.right)
        i += 1

    return root
    
if __name__ == "__main__":
    user_input = input("Enter tree as list: ")
    
    user_input = user_input.strip()[1:-1].split(',')
    values = [x.strip() for x in user_input]

    root = build_tree(values)

    sol = Solution()
    print("Reverse Level Order:", sol.levelOrderBottom(root))
            