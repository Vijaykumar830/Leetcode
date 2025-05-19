class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        binary_list = list(s)
        binary_list.sort(reverse=True)

        if '1' not in binary_list:
            return ""
        
        if binary_list[-1] == '1':
            return ''.join(binary_list)

        for i in range(len(binary_list)):
            if binary_list[i] == '1':
                binary_list.pop(i)
                break 
        binary_list.append('1')
        return ''.join(binary_list)
        