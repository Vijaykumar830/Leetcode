class Solution:
    def countBits(self, n: int) -> List[int]:
        bits_list = []
        for i in range(n+1):
            bits = bin(i).count('1')
            bits_list.append(bits)
        return bits_list


