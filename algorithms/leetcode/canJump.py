from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        try:
	        zero_p = len(nums) - nums[len(nums)-2::-1].index(0) - 2
        except ValueError:
	        return True
        i = zero_p - 1
        while (zero_p > 0 and i >= 0):
            if(nums[i] > zero_p - i):
                if (i == 0):
                    return True
                try:
	                zero_p = i - nums[i-1::-1].index(0) - 1                    
                except ValueError:
	                return True
                i = zero_p - 1
            else:
                i = i - 1
        
        if(len(nums) == 1 and nums[0] == 0):
            return True
        else:
            return False

print (Solution().canJump([3,0,8,2,0,0,1]))