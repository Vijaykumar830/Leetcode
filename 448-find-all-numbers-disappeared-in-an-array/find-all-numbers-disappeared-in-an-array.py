class Solution(object):
    def findDisappearedNumbers(self, nums):
        num_set = set(nums)  # O(n) to create
        result = []

        for i in range(1, len(nums) + 1):
            if i not in num_set:
                result.append(i)

        return result
