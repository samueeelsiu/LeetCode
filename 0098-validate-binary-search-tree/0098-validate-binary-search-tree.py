# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_all(node):
            if node is None:
                return []
            return get_all(node.left) + [node.val] + get_all(node.right)

        def check(node):
            if node is None:
                return True
            left_vals  = get_all(node.left)
            right_vals = get_all(node.right)
            if left_vals  and max(left_vals)  >= node.val:
                return False
            if right_vals and min(right_vals) <= node.val:
                return False
            return check(node.left) and check(node.right)
        return check(root)

        