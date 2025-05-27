class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr2 = []
        arr = []
        for i in range(1,n+1):
            if i%m != 0:
                arr.append(i)
            else:
                arr2.append(i)
        return sum(arr) - sum(arr2)


        