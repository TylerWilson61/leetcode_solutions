class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            result = int(str(x)[::-1])
        elif x < 0:
            result = -1 * int(str(x)[1:][::-1])
        _min = -2**31
        _max = 2**31
        if result > _max or result < _min:
            return 0
        else:
            return result
            
        
        
