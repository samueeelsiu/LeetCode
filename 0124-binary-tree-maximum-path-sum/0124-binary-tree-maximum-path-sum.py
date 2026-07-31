# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left_dfs = max(dfs(node.left), 0)

            right_dfs = max(dfs(node.right), 0)

            price_newpath = node.val + left_dfs + right_dfs

            self.max_sum = max(self.max_sum, price_newpath)

            return node.val + max(left_dfs, right_dfs)

        dfs(root)
        return self.max_sum
