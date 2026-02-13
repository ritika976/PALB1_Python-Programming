class Solution:
    def rotate(self, a):
        n = len(a)
        
        last = a[n - 1]
        
        for i in range(n - 1, 0, -1):
            a[i] = a[i - 1]
        
        a[0] = last
