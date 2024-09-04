class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        isOuter = False
        open = 0
        result = ""
        for c in s:
            if not isOuter:
                if c == '(': # find outer
                    isOuter = True
                    continue
                
            if isOuter:
                if c == '(':
                    open += 1
                    result+=c
                else:
                    if open > 0:
                        open -= 1
                        result+=c
                    else:
                        isOuter = False
                        continue
        return result
        