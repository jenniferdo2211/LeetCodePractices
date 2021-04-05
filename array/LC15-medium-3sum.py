class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        
        i = 0
        j = i + 1
        k = len(nums) - 1
        
        result = []
        
        while True:
            if i == len(nums) - 2:
                break
            
            if j >= k:
                i = self.pickNextIndex(nums, i)
                if i >= len(nums) - 2:
                    break
                j = i + 1
                k = len(nums) - 1
                continue
                
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                result.append([nums[i], nums[j], nums[k]])
                
            if sum > 0:
                k = self.pickPrevIndex(nums, k)
                continue
                
            j = self.pickNextIndex(nums, j)
            
        return result
            
        
    def pickNextIndex(self, nums, currIndex):
        if currIndex == len(nums) - 1:
            return currIndex + 1
        
        while nums[currIndex] == nums[currIndex + 1]:
            currIndex += 1
            
            if currIndex == len(nums) - 1:
                return currIndex + 1
        
        return currIndex + 1
    
    def pickPrevIndex(self, nums, currIndex):
        if currIndex == 0:
            return currIndex - 1
        
        while nums[currIndex] == nums[currIndex - 1]:
            currIndex -= 1
            
            if currIndex == 0:
                return currIndex - 1
        
        return currIndex - 1
            