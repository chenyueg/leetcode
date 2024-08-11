class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = sum(x for x in nums if x >= 1 and x <= 9)
        double = sum(y for y in nums if y >= 10)
        return True if(single > double or double > single) else False