class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        place = word.find(ch)
        if place != -1:
            return word[:place+1][::-1] + word[place+1:]
        return word