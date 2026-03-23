class Solution:    
    def findUnion(self, a, b):
        # code here
        s = set(a)
        
        for x in b:
            s.add(x)
            
        return sorted(s)
