class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * (n - x + 1)
        
        lower = SortedList()
        upper = SortedList()
        lower_sum = 0
        upper_sum = 0

        for i, val in enumerate(nums):
            if not lower or val <= lower[-1]:
                lower.add(val)
                lower_sum += val
            else:
                upper.add(val)
                upper_sum += val
                
            if i >= x:
                out_val = nums[i - x]
                if out_val <= lower[-1]:
                    lower.remove(out_val)
                    lower_sum -= out_val
                else:
                    upper.remove(out_val)
                    upper_sum -= out_val

            while len(lower) < len(upper):
                v = upper.pop(0)
                lower.add(v)
                upper_sum -= v
                lower_sum += v
            while len(lower) > len(upper) + 1:
                v = lower.pop(-1)
                upper.add(v)
                lower_sum -= v
                upper_sum += v
                
            if i >= x - 1:
                median = lower[-1]
                cost[i - x + 1] = (median * len(lower) - lower_sum) + (upper_sum - median * len(upper))

        dp = [0] * (n + 1)
        for j in range(1, k + 1):
            next_dp = [math.inf] * (n + 1)
            for i in range(j * x, n + 1):
                next_dp[i] = min(next_dp[i - 1], dp[i - x] + cost[i - x])
            dp = next_dp
            
        return dp[n]