class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        new_list = [i for i in range(1,n+1)]
        index = 0
        k = k - 1
        while len(new_list) > 1:
            index = (index + k) % len(new_list)
            new_list.pop(index)
        return new_list[0]