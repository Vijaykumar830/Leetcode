class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = s.count('0')
        
        if ones == 0:
            return ""  
        return '1' * (ones - 1) + '0' * zeros + '1'

        
        