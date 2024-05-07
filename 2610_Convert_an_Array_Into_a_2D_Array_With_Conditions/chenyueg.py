class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        met = []
        while nums:
            sub = []
            setNums = set(nums)
            for each in setNums:
                sub.append(each)
                nums.remove(each)
            met.append(sub)
        return met