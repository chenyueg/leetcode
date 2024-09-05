class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = [True for _ in range(len(l))]
        for i in range(len(l)):
            new_list = sorted(nums[l[i]:r[i]+1])
            diff = new_list[1] - new_list[0]
            for j in range(1, len(new_list)):
                if new_list[j] - new_list[j-1] != diff:
                    result[i] = False
                    break
        return result        