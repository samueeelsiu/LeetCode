class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            return total

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo