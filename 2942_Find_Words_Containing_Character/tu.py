class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            word = words[i]
            if x in word:
                result.append(i)
        return result
