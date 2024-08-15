class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = ""
        for each in words:
            acronym += each[0]
        return acronym == s