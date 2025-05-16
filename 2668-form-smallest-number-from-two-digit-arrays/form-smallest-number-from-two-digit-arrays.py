class Solution(object):
    def minNumber(self, nums1, nums2):
        arr = []
        arr2 = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    arr2.append(nums1[i])
                else:
                    arr.append(int(str(nums1[i]) + str(nums2[j])))
                    arr.append(int(str(nums2[j]) + str(nums1[i])))
        if arr2:
            return min(arr2)
        return min(arr)