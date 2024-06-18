class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [arr[0]] * (len(arr)+1)
        for i in range(1, len(arr)+1):
            prefix[i] = prefix[i-1] ^ arr[i-1]
        result = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if prefix[i] == prefix[j+1]:
                    result += j-i
        return result