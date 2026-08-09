from typing import List

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        best = self._scan(coins, k)
        mirror = sorted([[-r, -l, c] for l, r, c in coins])
        return max(best, self._scan(mirror, k))

    def _scan(self, segs: List[List[int]], k: int) -> int:
        n, ans, cur, j = len(segs), 0, 0, 0
        for i in range(n):
            e = segs[i][0] + k - 1
            while j < n and segs[j][0] <= e:
                l, r, c = segs[j]
                cur += (r - l + 1) * c
                j += 1
            total = cur
            ll, rr, cc = segs[j - 1]
            if rr > e:
                total -= (rr - e) * cc
            ans = max(ans, total)
            l0, r0, c0 = segs[i]
            cur -= (r0 - l0 + 1) * c0
        return ans