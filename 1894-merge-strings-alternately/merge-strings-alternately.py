class Solution(object):
    def mergeAlternately(self, word1, word2):
        b = ""

        max_length = max(len(word1),len(word2))

        for i in range(max_length):
            if i<len(word1):
                b = b + word1[i]
            if i<len(word2):
                b = b + word2[i]
        return b
