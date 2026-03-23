class Solution:
    def frequencyCount(self, arr,):
        N = len(arr)
        
        freq = [0] * N
        
        for x in arr:
            if x <= N:
                freq[x-1] += 1
                
        return freq
