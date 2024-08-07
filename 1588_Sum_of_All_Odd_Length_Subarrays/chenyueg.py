class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for length in range(0, len(arr), 2):
            for each in range(0, len(arr)-length):
                res += sum(arr[each:each+length+1])
        return res