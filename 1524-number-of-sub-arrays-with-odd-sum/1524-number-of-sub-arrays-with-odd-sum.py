class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1
        cur_sum = 0
        ans = 0
        
        for num in arr:
            cur_sum += num
            if cur_sum % 2 == 1:
                ans = (ans + even) % MOD
                odd += 1
            else:
                ans = (ans + odd) % MOD
                even += 1
                
        return ans