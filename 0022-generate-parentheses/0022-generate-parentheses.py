class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(current_str, left, right):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            if left < n:
                dfs(current_str + "(", left + 1, right)
            if right < left:
                dfs(current_str + ")", left, right + 1)
        dfs("", 0, 0)
        return res