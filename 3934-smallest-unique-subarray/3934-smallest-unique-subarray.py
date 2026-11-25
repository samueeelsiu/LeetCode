class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod1, mod2 = 10**9 + 7, 10**9 + 9
        base1, base2 = 131313, 131317

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i in range(n):
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + nums[i]) % mod1
            h2[i + 1] = (h2[i] * base2 + nums[i]) % mod2

        def check(length: int) -> bool:
            seen = set()
            dup = set()
            b1 = p1[length]
            b2 = p2[length]
            for i in range(n - length + 1):
                v1 = (h1[i + length] - h1[i] * b1) % mod1
                v2 = (h2[i + length] - h2[i] * b2) % mod2
                key = (v1 << 32) | v2
                if key in seen:
                    dup.add(key)
                else:
                    seen.add(key)
            return len(seen) > len(dup)

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left