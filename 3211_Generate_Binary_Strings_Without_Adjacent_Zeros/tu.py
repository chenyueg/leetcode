class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = ['0', '1']
        for i in range(1, n):
            visit_count = len(result)
            for i in range(visit_count):
                if result[i][-1] != '0':
                    result.append(result[i] + '0')
                result[i] = result[i] + '1'
        return result
