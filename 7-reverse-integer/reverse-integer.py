class Solution(object):
    def reverse(self, x):
        sign = -1 if x<0 else 1
        reverse_str = str(abs(x))[::-1]
        reverse_num = int(reverse_str)  * sign

        if reverse_num < -2**31 or reverse_num>2**31 - 1:
            return 0 
        return reverse_num
