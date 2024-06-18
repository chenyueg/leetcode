class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        head = ["type", "color", "name"]
        index = head.index(ruleKey)
        return len([l for l in items if l[index] == ruleValue])
