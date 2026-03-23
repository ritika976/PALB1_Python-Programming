class Solution(object):
    def findDuplicate(self, nums):
        
        freq = {}

        for x in nums:
            if x in freq:
                return x
            freq[x] = 1
