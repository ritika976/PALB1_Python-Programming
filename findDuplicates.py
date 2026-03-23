class Solution:
    def findDuplicates(self, arr):
        # code here
        freq = {}
        
        result = []
        
        for x in arr:
            freq[x] = freq.get(x,0) + 1
            
        for x in freq:
            if freq[x] > 1:
                result.append(x)
            
            
        return sorted(result)
