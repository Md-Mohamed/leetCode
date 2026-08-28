class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i , num in enumerate(nums):
            sum = target - num 
            if sum in seen:
                return [seen[sum], i]
    
            seen[num] = i
        
                