class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        start_c, start_r = start[0], int(start[1])
        end_c, end_r = end[0], int(end[1])
        result = []

        for c in range(ord(start_c), ord(end_c) + 1):
            for r in range(start_r, end_r + 1):
                result.append(chr(c) + str(r))

        return result
