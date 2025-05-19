class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums

        if a + b <= c:
            return "none"
        
        nums_set = set(nums)
        if len(nums_set) == 1:
            return "equilateral"
        elif len(nums_set) == 2:
            return "isosceles"
        else:
            return "scalene"