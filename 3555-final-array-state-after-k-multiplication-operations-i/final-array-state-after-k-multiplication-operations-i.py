class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(1,k+1):
            min_val = min(nums)
            for val in range(len(nums)):
                if min_val == nums[val]:
                    nums[val] = multiplier * min_val
                    break
        return nums