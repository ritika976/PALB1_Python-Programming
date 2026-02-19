class Solution:
    def isSubset(self, a, b):
        set_a = set(a)
        
        for num in b:
            if num not in set_a:
                return False
        
        return True
