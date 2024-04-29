class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        position = []
        for i in range(len(words)):
            if x in words[i]:
                position.append(i)
        return position