class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        result = ['' for _ in words]
        for word in words:
            index = int(word[-1])
            result[index-1] = word[:len(word)-1]
        return ' '.join(result)
        