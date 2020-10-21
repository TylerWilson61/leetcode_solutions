class Solution(object):
    def climbStairs(self, n,m = {0:1,1:1}):
        """
        :type n: int
        :rtype: int
        """
        # O(n) bottom up approach
        hsh = {1:1, 2:2}
        
        if n in (1,2):
            return n
        for i in range(3,n+1):
            moves = hsh[i-1] + hsh[i-2]
            hsh[i] = moves
            
        return hsh[n]

        #O(n) bottom down approach
        if n in m.keys():
            return m[n]
    
        else:
            m[n] = self.climbStairs(n-1,m) + self.climbStairs(n-2,m)
            return m[n]
