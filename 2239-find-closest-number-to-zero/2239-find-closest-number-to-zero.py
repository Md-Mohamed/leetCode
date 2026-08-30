class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closeNumber = nums[0]

        for i in nums:
            if abs(i) < abs(closeNumber) :
                closeNumber = i
            #else:
            #    return closeNumber 
        
        if closeNumber < 0 and abs(closeNumber) in nums:
            #closeNumber = abs(closeNumber)
            return abs(closeNumber)
        else:
            return closeNumber
        