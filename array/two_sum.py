class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #O(n^2)
        # for i in range(len(nums)):
        #     for k in range(len(nums)):
        #         if nums[i] + nums[k] == target and i != k:
        #             return [i,k]

        #O(n) one pass
        hsh = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hsh.keys() and hsh[pair] != i:
                return [i, hsh[pair]]
            hsh[nums[i]] = i

            
#       O(n) two pass
#         for i in range(len(nums)):
#             pair = target - nums[i]
#             if pair in hsh.keys() and hsh[pair] != i:
#                 return [i, hsh[pair]]
                        
    
