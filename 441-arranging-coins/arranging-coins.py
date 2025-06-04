class Solution:
    def arrangeCoins(self, n: int) -> int:
        c=0
        num=n
        for i in range(1,n+1):
            if num-i>=0:
                c+=1
                num=num-i
            else:
                break
        return c