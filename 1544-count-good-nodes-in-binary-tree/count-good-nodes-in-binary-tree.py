# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue):
            if not node:
                return 0
            
            maxVal = max(node.val, maxValue)
            cur = 1 if node.val >= maxValue else 0
            return cur + dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, root.val if root else 0)