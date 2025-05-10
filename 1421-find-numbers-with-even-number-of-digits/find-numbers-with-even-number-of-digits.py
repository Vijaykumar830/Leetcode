class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            numbers = len(str(i))
            if numbers %2==0:
                count += 1 
        return count