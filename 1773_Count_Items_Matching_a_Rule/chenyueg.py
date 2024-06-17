class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        index = {"type": 0, "color": 1, "name": 2}
        for each in items:
            if each[index[ruleKey]] == ruleValue:
                count += 1
        return count