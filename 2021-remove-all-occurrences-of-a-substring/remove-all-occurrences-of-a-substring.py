class Solution(object):
    def removeOccurrences(self, s, part):
        remain_part = ""
        for i in range(len(s)):
            remain_part += s[i]
            if part in remain_part:
                remain_part = remain_part.replace(part, "")
        return remain_part

                