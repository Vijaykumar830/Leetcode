class Solution(object):
    def isBalanced(self, num):
        even_sum = 0 
        odd_sum = 0 
        for i in range(len(num)):
            if i %2 == 0:
                odd_sum += int(num[i])
            else:
                even_sum += int(num[i])
        if even_sum == odd_sum:
            return True 
        else:
            return False