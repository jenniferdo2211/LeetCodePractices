class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        diff = None
        
        nums.sort()
        i = 0
        j = i + 1
        k = len(nums) - 1
        
        print("nums = ", nums)
        
        while i < len(nums) - 2:
            while j < k:
                
                currSum = nums[i] + nums[j] + nums[k]
                
                if currSum == target:
                    return currSum
                
                currDiff = abs(currSum - target)

                if closest is None or currDiff < diff:
                    closest = currSum
                    diff = currDiff
                    
                if currSum < target:
                    j = self.findNext(nums, j)
                    continue
                    
                k = self.findPrev(nums, k)
            
            i = self.findNext(nums, i)
            j = i + 1
            k = len(nums) - 1
            
        return closest
    
            
    def findNext(self, nums, j):
        while j < len(nums) - 1 and nums[j] == nums[j + 1]:
            j += 1
        
        return j + 1
    
    def findPrev(self, nums, k):
        while k > 0 and nums[k] == nums[k - 1]:
            k -= 1
        
        return k - 1