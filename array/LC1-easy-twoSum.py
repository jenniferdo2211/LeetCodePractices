class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        
        for i, val in enumerate(nums):
            if target - val in numToIndex:
                return numToIndex[target - val], i
            
            numToIndex[val] = i
            
        return -1, -1



# class WorseSolution:
#     NUM = 0
#     INDEX = 1
        
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         if len(nums) < 2:
#             return -1, -1
        
#         numToIndex = [(val, i) for i, val in enumerate(nums)]
#         numToIndex.sort()
        
#         i = 0
#         j = len(numToIndex) - 1
        
#         while i < j:
#             sum = self.getNum(numToIndex, i) + self.getNum(numToIndex, j)
#             if sum == target:
#                 return self.getIndex(numToIndex, i), self.getIndex(numToIndex, j)
        
#             if sum < target:
#                 i += 1
#                 continue
            
#             j -= 1
            
#         return -1, -1
                
            
            
#     def getNum(self, numToIndex, i):
#         return numToIndex[i][WorseSolution.NUM]
    
#     def getIndex(self, numToIndex, i):
#         return numToIndex[i][WorseSolution.INDEX]