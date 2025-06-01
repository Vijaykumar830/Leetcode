class Solution:
    def minElement(self, nums: List[int]) -> int:
        for idx, el in enumerate(nums):
            n = str(nums[idx])
            sum_of_digits = 0
            for digit in n:
                sum_of_digits += int(digit)
                
            nums[idx] = sum_of_digits

        return min(nums)