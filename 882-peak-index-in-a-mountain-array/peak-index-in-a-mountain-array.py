class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_num = max(arr)
        for i,ch in enumerate(arr):
            if ch == max_num:
                return i