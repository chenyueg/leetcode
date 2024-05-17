class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for each in encoded:
            result.append(result[-1] ^ each)
        return result