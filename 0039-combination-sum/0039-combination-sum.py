class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort() 
        
        def backtrack(start, path, current_sum):
            if current_sum == target:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):

                if current_sum + candidates[i] > target:
                    break

                path.append(candidates[i])

                backtrack(i, path, current_sum + candidates[i])
                path.pop() 

        backtrack(0, [], 0)
        return res