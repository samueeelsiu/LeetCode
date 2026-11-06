class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        
        ans = [0] * len(queries)
        cnt = [0] * (n + 1)
        active = 0
        
        left = 0
        right = 0
        m = len(logs)

        for q, idx in sorted_queries:
            while right < m and logs[right][1] <= q:
                s_id = logs[right][0]
                if cnt[s_id] == 0:
                    active += 1
                cnt[s_id] += 1
                right += 1
            while left < m and logs[left][1] < q - x:
                s_id = logs[left][0]
                cnt[s_id] -= 1
                if cnt[s_id] == 0:
                    active -= 1
                left += 1
            ans[idx] = n - active
            
        return ans