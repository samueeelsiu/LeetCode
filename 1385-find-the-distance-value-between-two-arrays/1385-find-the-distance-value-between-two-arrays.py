class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0
        
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            if idx == len(arr2) or arr2[idx] > x + d:
                ans += 1
                
        return ans