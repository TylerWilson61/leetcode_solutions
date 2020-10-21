class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force
        
        # maxsum = float('-inf')
        # subarray = []
        # for i in range(len(nums)):
        #     length = 0
        #     while length < len(nums):
        #         length+=1
        #         temp_sum = 0
        #         for k in nums[i:length+i]:
        #             temp_sum += k
        #         # print('cur',nums[i:length+i])
        #         # print('cur sum', temp_sum)
        #         if temp_sum > maxsum:
        #             subarray = nums[i:length+i]
        #             maxsum = temp_sum
        #         temp_sum = 0
        # return maxsum
        
        #O(x*n)
        
        #iterate through dif sizes
        #for each size, find subarray with max sum
        #return subarray with largest sum
        # maxsum = float('-inf')
        # for i in range(1,len(nums)+1):
        #     start = 0
        #     end = i
        #     len_iter = end - start
        #     while len_iter <= len(nums):
        #         sub_a = nums[start:end]
        #         # print('cur subarray', sub_a)
        #         sub_v = sum(sub_a)
        #         # print('cur max sum',sub_v )
        #         if sub_v > maxsum:
        #             maxsum = sub_v
        #         start += 1
        #         end += 1
        #         len_iter += 1
        # return maxsum
        
        #O(n)
        #max(prev sum+index, index)
        max_sum = nums[0]
        prev_sum = nums[0]
        for i in nums[1:]:
            # print('options idx: ', i)
            # print('option idx+sum: ',prev_sum + i)
            if i > prev_sum + i:
                # print('chosen: ', i)
                prev_sum = i
                if prev_sum > max_sum:
                    max_sum = prev_sum
            else:
                prev_sum = prev_sum + i
                # print('chosen: ', prev_sum)
                if prev_sum > max_sum:
                    max_sum = prev_sum
        return max_sum
                
            
            
        
