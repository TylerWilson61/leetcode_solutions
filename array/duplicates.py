class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _set = set()
        for i in nums:
            _set.add(i)
            
        return len(_set) < len(nums)
