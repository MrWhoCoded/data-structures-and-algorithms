from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum_path(node, rem_sum):
            if node is None:
                return False
            rem_sum -= node.val
            
            if (rem_sum == 0) and not node.left and not node.right:
                return True
            return sum_path(node.left, rem_sum) or sum_path(node.right, rem_sum)
            
        res = sum_path(root, targetSum)
        return res
 

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
    print("Reverse Level Order:", sol.hasPathSum(root, 22))