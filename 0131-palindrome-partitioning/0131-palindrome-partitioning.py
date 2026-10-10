class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
            
        def backtrack(start_index: int):
            if start_index == len(s):
                res.append(path[:])
                return
            
            for i in range(start_index, len(s)):
                sub = s[start_index:i+1]
                
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(i + 1)
                    path.pop()
                    
        backtrack(0)
        return res