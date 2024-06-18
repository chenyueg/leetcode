class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        greater = []
        for each in nums:
            if each < pivot:
                smaller.append(each)
            elif each == pivot:
                equal.append(each)
            else:
                greater.append(each)
        return smaller + equal + greater