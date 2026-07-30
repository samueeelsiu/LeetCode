class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            cand1 = x
            cand2 = cur_max * x
            cand3 = cur_min * x
            cur_max = max(cand1, cand2, cand3)
            cur_min = min(cand1, cand2, cand3)
            ans = max(ans, cur_max)
        return ans