class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        result = 0
        for c in commands:
            if c == 'UP':
                result -= n
            if c == 'DOWN':
                result += n
            if c == 'LEFT':
                result -= 1
            if c == 'RIGHT':
                 result += 1
        return result