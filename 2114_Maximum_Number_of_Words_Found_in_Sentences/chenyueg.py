class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxNum = 0
        for each in sentences:
            each = each.split()
            if len(each) >= maxNum:
                maxNum = len(each)
            else:
                continue
        return maxNum