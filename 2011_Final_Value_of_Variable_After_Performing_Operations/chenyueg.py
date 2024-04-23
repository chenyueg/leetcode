class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for each in operations:
            if each == "++X" or each == "X++":
                x += 1
            elif each == "--X" or each == "X--":
                x -= 1
        return x