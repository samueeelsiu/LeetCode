class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)

        prefix_map[0] = 1

        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            count += prefix_map[current_sum - k]

            prefix_map[current_sum] += 1

        return count