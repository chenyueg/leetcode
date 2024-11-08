class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([int(s[11:13]) for s in details if int(s[11:13]) > 60])
        