class Solution(object):
    def twoSum(self, nums, target):
        
        d = {}

        for i in range(len(nums)):
            current = nums[i]
            required = target - current

            if required in d:
                return d[required], i
        
            d[current] = i
