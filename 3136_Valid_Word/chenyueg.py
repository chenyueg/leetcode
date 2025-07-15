class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = 0
        consonants = 0
        vowel_set = "aeiouAEIOU"

        for char in word:
            if char.isalpha():
                if char in vowel_set:
                    vowels += 1
                else:
                    consonants += 1
            elif not char.isdigit():
                return False

        return vowels >= 1 and consonants >= 1