class Solution:
    def intersectSize(self,a, b):
        # code here
        
        s1 = set(a)
        s2 = set(b)
        
        result = s1 & s2
        
        return len(result)
