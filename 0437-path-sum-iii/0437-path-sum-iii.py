# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        count = defaultdict(int); count[0] = 1
        ans = 0
        def dfs(node, cur):
            nonlocal ans                     # ← 关键字：改外层变量
            if node is None: return
            cur += node.val
            ans += count[cur - targetSum]
            count[cur] += 1
            dfs(node.left, cur); dfs(node.right, cur)
            count[cur] -= 1
        dfs(root, 0)
        return ans