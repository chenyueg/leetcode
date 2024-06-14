class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        pair = 0
        xor = [0 for i in range(n+1)]
        
        for j in range(n):
            xor[j+1] = xor[j] ^ arr[j]

        for k in range(n):
            for l in range(k+1, n):
                if xor[k] == xor[l+1]:
                    pair += l-k
        
        return pair