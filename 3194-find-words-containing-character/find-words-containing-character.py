class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index_list = []
        for i, ch in enumerate(words):
            if x in ch:
                index_list.append(i)
        return index_list