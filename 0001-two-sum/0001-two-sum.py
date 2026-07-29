class Solution:
    def twoSum(self, nums, target):
        seen = {}                        
        for i in range(len(nums)):        
            x = nums[i]                  
            need = target - x            
            if need in seen:             
                return [seen[need], i]    
            seen[x] = i                   