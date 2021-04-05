class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        
        count = 0
        nums.sort()
        
        i = 0
        j = i + 1
        k = len(nums) - 1
        
        while i < len(nums) - 2:
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                
                if sum < target:
                    count += (k - j)
                    j += 1
                    continue
                    
                k -= 1
                
            i += 1
            j = i + 1
            k = len(nums) - 1
            
        return count             