class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        dict1 = {}
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1
        a = set(list(dict1.values()))
        if len(a) == 1:
            return True
        else:
            return False

        

            
