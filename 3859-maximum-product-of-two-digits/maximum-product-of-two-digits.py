class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        max_product = 0 

        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                product = digits[i] * digits[j]
                max_product = max(max_product,product)
        return max_product