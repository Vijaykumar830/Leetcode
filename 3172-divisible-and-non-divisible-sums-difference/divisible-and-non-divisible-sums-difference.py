class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr2 = 0
        arr = 0
        for i in range(1,n+1):
            if i%m != 0:
                arr += i
            else:
                arr2 += i
        return arr - arr2


        