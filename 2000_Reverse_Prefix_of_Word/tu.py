class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                if i<len(word):
                    return word[i::-1] + word[i+1:]
                else:
                    return word[i::-1]
        return word